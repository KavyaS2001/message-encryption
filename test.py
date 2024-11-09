import tkinter as tk
from tkinter import ttk

# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to handle the Encrypt button click
def handle_encrypt():
    text = input_text.get()
    shift = int(shift_value.get())
    result = encrypt(text, shift)
    output_text.set(result)

# Function to handle the Decrypt button click
def handle_decrypt():
    text = input_text.get()
    shift = int(shift_value.get())
    result = decrypt(text, shift)
    output_text.set(result)

# Set up the main application window
root = tk.Tk()
root.title("Simple Encryption and Decryption Tool")

# Input message label and entry
ttk.Label(root, text="Enter Message:").grid(row=0, column=0, padx=10, pady=10)
input_text = tk.StringVar()
ttk.Entry(root, textvariable=input_text, width=30).grid(row=0, column=1, padx=10, pady=10)

# Shift value label and entry
ttk.Label(root, text="Enter Shift Value:").grid(row=1, column=0, padx=10, pady=10)
shift_value = tk.StringVar()
ttk.Entry(root, textvariable=shift_value, width=10).grid(row=1, column=1, padx=10, pady=10)

# Buttons for encryption and decryption
ttk.Button(root, text="Encrypt", command=handle_encrypt).grid(row=2, column=0, padx=10, pady=10)
ttk.Button(root, text="Decrypt", command=handle_decrypt).grid(row=2, column=1, padx=10, pady=10)

# Output label and display
ttk.Label(root, text="Output Message:").grid(row=3, column=0, padx=10, pady=10)
output_text = tk.StringVar()
ttk.Entry(root, textvariable=output_text, width=30, state='readonly').grid(row=3, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()

