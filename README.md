# Number-Guessing-Game
A Python terminal game where players guess a randomly generated number across three difficulty levels, featuring colorful UI, hint system, and persistent high scores to track the best performances.

A dynamic Python game where players guess a randomly generated number within a specified range. 

The game features:
Three difficulty levels (Easy, Medium, Hard) with different number ranges
Hints system with limited hints based on difficulty
Score calculation based on attempts and time taken
Persistent high score tracking using JSON
Colorful console interface using Colorama
Player statistics including attempts and completion time
The game provides a simple yet engaging experience where players can compete to achieve the highest scores across different difficulty levels. High scores are stored locally, allowing multiple players to challenge each other on the same machine.

This project demonstrates fundamentals of Python programming including random number generation, file I/O with JSON, exception handling, conditional logic, and creating an interactive command-line interface.

**Summary:**

A fun and interactive Python console game where players attempt to guess a randomly generated number within a custom range. The game features multiple difficulty levels, a hint system, and persistent high score tracking to challenge yourself and compete with friends.

Features
Multiple Difficulty Levels:

Easy (1-50)
Medium (1-100)
Hard (1-200)
Smart Hint System: Players receive a limited number of hints based on difficulty level:

Easy: 3 hints
Medium: 2 hints
Medium: 1 hint
Hints reveal whether the number is odd or even
Score System: Scores are calculated based on:

Number of attempts taken
Time elapsed to complete the game
Difficulty level (higher difficulties award more points)
High Score Tracking:

Persistent storage using JSON
View top 5 scores for each difficulty level
Track multiple players on the same machine
User-Friendly Interface:

Colorful text output using Colorama
Clear instructions and feedback
Intuitive gameplay flow
How to Play
Enter your player name
Select a difficulty level
Guess the secret number
Use hints strategically when stuck
Try to achieve the highest possible score!
Technical Details
Built entirely in Python, the game demonstrates:

Random number generation
File I/O operations with JSON
Time tracking functionality
Text-based UI design with Colorama
Exception handling
Game state management
This project showcases fundamental programming concepts while providing an enjoyable gaming experience suitable for players of all ages.
