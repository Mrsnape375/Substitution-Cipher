import string
import random

# STEP 1: Create character set (punctuation + letters + digits + space)
chars = list(string.punctuation + string.ascii_letters + string.digits + " ")

# STEP 2: Shuffle a copy of the character set to make the encryption key
key = chars.copy()
random.shuffle(key)

# STEP 3: Ask the user for a message to encrypt
message = input("🔐 Enter your message to encrypt: ")
cipher_text = ''

# STEP 4: Encrypt the message
for letter in message:
    index = chars.index(letter)
    cipher_text += key[index]

print("\n🧾 Encrypted message:")
print(cipher_text)

# STEP 5: Ask if the user wants to decrypt
choice = input("\n🔓 Do you want to decrypt the message? (Y/N): ").strip().upper()

if choice == 'Y':
    decrypted_text = ''
    for letter in cipher_text:
        index = key.index(letter)
        decrypted_text += chars[index]

    print("\n📜 Decrypted message:")
    print(decrypted_text)

