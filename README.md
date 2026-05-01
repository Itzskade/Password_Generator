# Password Tool

A small Python CLI project that generates secure passwords with configurable length. It supports mixed character sets (letters, numbers, and symbols), regeneration using the last used length, and basic input validation with retry limits.

This tool is lightweight, modular, and designed for learning purposes.

---

## 📦 Requirements

- Python 3.10+

No external dependencies are required. The project uses only Python standard libraries.

---

## 🔧 Features

- Random secure password generation
- Configurable length (10–128 characters)
- Includes uppercase, lowercase, numbers, and symbols
- Regenerate password using last selected length
- Input validation with retry limits
- Simple CLI menu system
- Modular architecture (UI, logic, configuration)

---

## ▶️ Usage

Run the program and follow the interactive menu:

- Generate a new password by selecting a length
- Regenerate the last generated password
- Exit the application

---

## 🧪 Behavior Examples

✔ Generate a password of 12 characters  
→ Returns a random secure password like `aF3!kL9@pQ2x`

✔ Generate a password of 20 characters  
→ Returns a longer mixed-character password

✔ Regenerate last password  
→ Creates a new password using the previous length without re-entering it

✘ Invalid input (e.g. 5 or 200)  
→ Shows validation error and requests a valid length

✘ Non-numeric input  
→ Prompts user to enter a valid number

---

## 📝 Notes

- Built for learning Python modular design
- Focused on CLI interaction and user input handling
- Demonstrates basic secure random generation techniques
- Fully terminal-based, no GUI required
