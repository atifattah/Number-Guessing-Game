# 🎯 Number Guessing Game

A **fun and interactive Python terminal game** where players try to guess a randomly generated number across **three difficulty levels**. With colorful visuals, smart hints, and high score tracking, it's a great way to test your luck and logic!

---

## 🕹️ Game Overview

Guess the secret number within a custom range based on your chosen difficulty. Use hints wisely, race against the clock, and compete for the highest score!

---

## ✨ Features

### 🔢 Multiple Difficulty Levels

- **Easy:** 1 to 50  
- **Medium:** 1 to 100  
- **Hard:** 1 to 200

### 💡 Smart Hint System

Hints reveal if the number is **odd or even**, with limits based on difficulty:

- **Easy:** 3 hints  
- **Medium:** 2 hints  
- **Hard:** 1 hint

### 🧠 Scoring System

Scores are based on:

- Number of attempts  
- Time taken  
- Difficulty level (higher difficulty = more points)

### 🏆 High Score Tracking

- Persistent storage using **JSON**  
- View **top 5 scores** for each difficulty  
- Track **multiple players** on the same machine

### 🎨 User-Friendly Interface

- Colorful text using **Colorama**  
- Clear instructions and feedback  
- Smooth and intuitive gameplay

---

## ▶️ How to Play

1. Enter your **player name**
2. Select a **difficulty level**
3. Start **guessing the number**
4. Use **hints** strategically
5. Try to beat the **high score!**

---

## ⚙️ Technical Highlights

- 🔁 Random number generation  
- 📂 File I/O with JSON  
- ⏱️ Time tracking  
- 🎨 Colorama terminal design  
- ❗ Exception handling  
- 🧾 Game state management  

---

## 🧑‍💻 Learning Goals

This project helps you practice:

- Python basics (`input()`, `if-else`, loops)  
- Working with libraries (`random`, `json`, `colorama`)  
- Handling errors with `try-except`  
- Creating an interactive command-line tool  
- Managing data persistence with JSON

---

## 🚀 Getting Started

```bash
python number_guessing_game.py
