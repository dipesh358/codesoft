import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(entry_length.get())

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x250")

# Set background color
root.configure(bg="#5c9ce0")

# Entry for password length
length_label = tk.Label(root, text="Enter Password Length:", bg="#5c9ce0", font=("Arial", 14))
length_label.grid(row=0, column=0, padx=20, pady=10)

entry_length = tk.Entry(root, font=("Arial", 14))
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#D4AC0D', font=("Arial", 14))
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Label to display generated password
result_label = tk.Label(root, bg="#5c9ce0", font=("Arial", 16))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
