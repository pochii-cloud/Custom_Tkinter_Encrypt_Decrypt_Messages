from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk

key = Fernet.generate_key()
f = Fernet(key)

def encrypt_message():
    input_string = input_text.get()  # Get the input message from the Entry widget
    encrypted_message = f.encrypt(input_string.encode())
    encrypted_label.config(text="Encrypted Message: " + encrypted_message.decode())

def decrypt_message():
    encrypted_message = encrypted_label.cget("text").split(": ")[1]
    decrypted_message = f.decrypt(encrypted_message.encode())
    decrypted_label.config(text="Decrypted Message: " + decrypted_message.decode())

# Create the tkinter window
window = tk.Tk()
window.title("Message Encryption")

# Create the input message Entry widget
input_label = ttk.Label(window, text="Enter Message:")
input_label.pack()
input_text = ttk.Entry(window)
input_text.pack()

# Create the Encrypt button
encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_message)
encrypt_button.pack()

# Create the encrypted message label
encrypted_label = ttk.Label(window, text="Encrypted Message:")
encrypted_label.pack()

# Create the Decrypt button
decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt_message)
decrypt_button.pack()

# Create the decrypted message label
decrypted_label = ttk.Label(window, text="Decrypted Message:")
decrypted_label.pack()

window.mainloop()

