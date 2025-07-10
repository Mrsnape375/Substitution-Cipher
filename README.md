# 🔐 Substitution Cipher - Encryption & Decryption Program

This is a beginner-friendly Python program that performs **substitution cipher encryption and decryption**.  
It works by replacing each character in a message with a different, randomly chosen character, creating a simple but effective encrypted version of the original message.

---

## 📌 Features

- Encrypt any message using a randomly shuffled key
- Decrypt the encrypted message using the same key
- Supports letters, digits, punctuation, and spaces
- Clean and easy-to-read code with comments
- Console-based user interface

---

## 🧠 How It Works

1. A list of all allowed characters is created (`chars`)
2. A copy of that list is shuffled to create a random encryption key (`key`)
3. During encryption:
   - Each character in the message is replaced using `key[index]`
4. During decryption:
   - Each character is translated back using the original `chars[index]`

---

## 🖥️ How to Run

1. Make sure you have Python 3.x installed.
2. Download or clone this repository.
3. Open the terminal (or IDE) and run:

```bash
python encryption.py
