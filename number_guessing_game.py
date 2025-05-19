# Importing necessary libraries
import random
import time
import json
import os
from colorama import Fore, Style, init

# Initializing colorama for colored output
init()

def load_high_scores():
    try:
        with open("high_scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_high_score(player_name, difficulty, score):
    high_scores = load_high_scores()
    
    if difficulty not in high_scores:
        high_scores[difficulty] = {}
    
    if player_name in high_scores[difficulty]:
        if score > high_scores[difficulty][player_name]:
            high_scores[difficulty][player_name] = score
    else:
        high_scores[difficulty][player_name] = score
    
    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file)

def display_high_scores():
    high_scores = load_high_scores()
    if not high_scores:
        print(Fore.YELLOW + "No high scores yet!" + Style.RESET_ALL)
        return
    
    print(Fore.CYAN + "\n===== HIGH SCORES =====" + Style.RESET_ALL)
    for difficulty in high_scores:
        print(Fore.MAGENTA + f"\n{difficulty.upper()} LEVEL:" + Style.RESET_ALL)
        # Sort by score (highest first)
        sorted_scores = sorted(high_scores[difficulty].items(), key=lambda x: x[1], reverse=True)
        for i, (name, score) in enumerate(sorted_scores[:5], 1):  # Show top 5
            print(f"{i}. {name}: {score}")

def play_game():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(Fore.GREEN + "\n===== NUMBER GUESSING GAME =====" + Style.RESET_ALL)
    
    player_name = input("Enter your name: ")
    
    # Difficulty selection
    print("\nSelect difficulty:")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-200)")
    
    while True:
        difficulty = input("Choose difficulty (1-3): ")
        if difficulty in ["1", "2", "3"]:
            break
        print(Fore.RED + "Please enter 1, 2, or 3" + Style.RESET_ALL)
    
    if difficulty == "1":
        max_number = 50
        difficulty_name = "easy"
        max_hints = 3
    elif difficulty == "3":
        max_number = 200
        difficulty_name = "hard"
        max_hints = 1
    else: 
        max_number = 100
        difficulty_name = "medium"
        max_hints = 2
    
    number = random.randrange(1, max_number + 1)
    attempts = 0
    hints_remaining = max_hints
    
    print(f"\n{Fore.YELLOW}I'm thinking of a number between 1 and {max_number}.{Style.RESET_ALL}")
    print(f"You have {hints_remaining} hints available. Type 'hint' to use one.")
    
    start_time = time.time()
    
    while True:
        try:
            guess_input = input("\nEnter your guess (or 'hint' for a hint): ")
            
            if guess_input.lower() == 'hint':
                if hints_remaining > 0:
                    hints_remaining -= 1
                    if number % 2 == 0:
                        print(Fore.CYAN + f"HINT: The number is even. ({hints_remaining} hints left)" + Style.RESET_ALL)
                    else:
                        print(Fore.CYAN + f"HINT: The number is odd. ({hints_remaining} hints left)" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hints remaining!" + Style.RESET_ALL)
                continue
                
            guess = int(guess_input)
            attempts += 1
            
            if guess < 1 or guess > max_number:
                print(f"{Fore.RED}Please enter a number between 1 and {max_number}.{Style.RESET_ALL}")
                attempts -= 1
                continue
                
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number or 'hint'.{Style.RESET_ALL}")
            continue
        
        if guess < number:
            print(f"{Fore.BLUE}Your guess is too low!{Style.RESET_ALL}")
        elif guess > number:
            print(f"{Fore.RED}Your guess is too high!{Style.RESET_ALL}")
        else:
            elapsed_time = time.time() - start_time
            print(f"\n{Fore.GREEN}Congratulations {player_name}! You guessed the number {number} correctly!{Style.RESET_ALL}")
            print(f"It took you {attempts} attempt{'s' if attempts > 1 else ''} and {elapsed_time:.2f} seconds.")
            
            # Calculating score - fewer attempts and time = higher score
            score = int(1000 * (max_number/50) / (attempts + elapsed_time/10))
            print(f"{Fore.YELLOW}Your score: {score}{Style.RESET_ALL}")
            
            # Saving high score
            save_high_score(player_name, difficulty_name, score)
            break

def main():
    while True:
        play_game()
        display_high_scores()
        
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower() != 'y':
            print(Fore.GREEN + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()