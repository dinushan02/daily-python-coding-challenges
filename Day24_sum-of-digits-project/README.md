# 🔢 Sum of Digits Project (Day 24)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

---

## ✨ Overview

This project is part of my **Daily Python Coding Challenge (Day 24)**.  
It demonstrates how to calculate the **sum of digits of a number** using both:

- 💻 CLI (Console Application)
- 🖥️ GUI (Tkinter Desktop Application)

It helps strengthen understanding of:
- Loops
- Number manipulation
- Functions
- GUI development using Tkinter

---

## 📁 Project Structure
Day24_sum-of-digits-project/
├── cli_app.py
├── gui_app.py
└── README.md


---

## 🧩 Problem Statement

Create a Python program that:
- 🔢 Takes a number as input
- ➕ Calculates the sum of all digits
- 🖨 Displays the result clearly

---

## 💻 CLI Version Features

- Takes user input from terminal
- Uses loop-based digit extraction
- Handles invalid input safely

### ▶️ Example
Enter a number: 1234
Sum of all digits: 10


---

## 🖥️ GUI Version Features (Tkinter)

- User-friendly input box
- Button-based interaction
- Real-time result display
- Error handling using popup messages

---

## 🧠 Tkinter Components Used

- `tk.Tk()` → Creates main window  
- `Entry()` → Input field  
- `Button()` → Triggers calculation  
- `Label()` → Displays output  
- `messagebox` → Shows error alerts  

---

## 🔢 Core Logic

- `% 10` → Extract last digit  
- `// 10` → Remove last digit  
- `while loop` → Repeat until number becomes 0  
- `try-except` → Handle invalid inputs safely  

---

## 📸 Screenshots

### 🖥️ CLI Version
> *(Add your terminal screenshot here)*
Enter a number: 456
Sum of all digits: 15


---

### 🪟 GUI Version
> *(Add your Tkinter app screenshot here)*  

🟦 Input box  
🟩 Calculate button  
🟨 Result display area  

---

## 🚀 How to Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/Day24_sum-of-digits-project.git

2️⃣ Run CLI App
python cli_app.py

3️⃣ Run GUI App
python gui_app.py
```

💡 Key Learnings
Building CLI applications in Python
Creating GUI apps using Tkinter
Reusing logic across different interfaces
Improving code structure and readability

📌 Future Improvements
Add dark mode UI 🌙
Add reset/clear button 🔄
Convert to executable (.exe) 📦
Add more math utilities (factorial, reverse number, etc.)

👨‍💻 Author
Python Learning Journey – Day 24 Challenge
Built as part of my consistent Python practice to become an AI Engineer 🚀

⭐ Support
If you like this project:
⭐ Star the repository
🍴 Fork it
🔄 Share it with others
