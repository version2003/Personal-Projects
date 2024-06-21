import tkinter as tk
from tkinter import messagebox
import random
import string

# Initialize the main window
app = tk.Tk()
app.title("Advanced Password Generator")
app.geometry("400x400")  # Set the size of the window

# Define the frames for organization
frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

# Add widgets for password length
tk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky='w')
entry_length = tk.Entry(frame)
entry_length.grid(row=0, column=1)

# Add checkboxes for character types
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
var_ambiguous = tk.BooleanVar(value=False)

tk.Checkbutton(frame, text="Include Letters", variable=var_letters).grid(row=1, column=0, sticky='w')
tk.Checkbutton(frame, text="Include Digits", variable=var_digits).grid(row=1, column=1, sticky='w')
tk.Checkbutton(frame, text="Include Symbols", variable=var_symbols).grid(row=2, column=0, sticky='w')
tk.Checkbutton(frame, text="Avoid Ambiguous Characters", variable=var_ambiguous).grid(row=2, column=1, sticky='w')

# Add a button to generate the password
tk.Button(frame, text="Generate Password", command=lambda: generate_password_gui()).grid(row=3, column=0, columnspan=2, pady=10)

# Add an entry box to display the generated password
entry_password = tk.Entry(frame, width=40)
entry_password.grid(row=4, column=0, columnspan=2, pady=5)

# Add buttons to copy password to clipboard and save to file
tk.Button(frame, text="Copy to Clipboard", command=lambda: copy_to_clipboard()).grid(row=5, column=0, columnspan=1, pady=5)
tk.Button(frame, text="Save to File", command=lambda: save_to_file()).grid(row=5, column=1, columnspan=1, pady=5)

# Add a label to display the strength of the password
label_strength = tk.Label(frame, text="Password Strength: N/A")
label_strength.grid(row=6, column=0, columnspan=2)

# Function to generate password
def generate_password_gui():
    length = int(entry_length.get())
    use_letters = var_letters.get()
    use_digits = var_digits.get()
    use_symbols = var_symbols.get()
    avoid_ambiguous = var_ambiguous.get()

    password = generate_password(length, use_letters, use_digits, use_symbols, avoid_ambiguous)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    evaluate_strength(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(entry_password.get())
    messagebox.showinfo("Info", "Password copied to clipboard!")

# Function to save password to a file
def save_to_file():
    password = entry_password.get()
    if password:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Info", "Password saved to passwords.txt")
    else:
        messagebox.showwarning("Warning", "No password to save!")

# Function to evaluate password strength
def evaluate_strength(password):
    strength = "Weak"
    if len(password) >= 12:
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    
    label_strength.config(text=f"Password Strength: {strength}")

# Function to generate password based on the options selected
def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True, avoid_ambiguous=False):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if avoid_ambiguous:
        ambiguous_characters = 'Il1O0'
        characters = ''.join([ch for ch in characters if ch not in ambiguous_characters])
    
    if not characters:
        raise ValueError("No characters available to generate password. Please enable at least one character type.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Run the Tkinter event loop
app.mainloop()
