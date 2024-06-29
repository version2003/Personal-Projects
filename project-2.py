import os
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# Function to view notes
def view_notes():
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        messagebox.showinfo("Notes", "No notes available.")
        return
    
    notes_window = tk.Toplevel(root)
    notes_window.title("View Notes")
    
    scroll_text = scrolledtext.ScrolledText(notes_window, width=40, height=20)
    scroll_text.pack(padx=10, pady=10)
    
    for filename in os.listdir(notes_dir):
        with open(os.path.join(notes_dir, filename), 'r') as file:
            content = file.read()
            scroll_text.insert(tk.END, f"{filename[:-4]}: {content}\n")
    scroll_text.config(state=tk.DISABLED)

# Function to add a note
def add_note():
    note_title = simpledialog.askstring("Input", "Enter the note title:")
    if note_title:
        note_content = simpledialog.askstring("Input", "Enter the note content:")
        
        notes_dir = 'notes'
        if not os.path.exists(notes_dir):
            os.makedirs(notes_dir)
        
        note_path = os.path.join(notes_dir, f"{note_title}.txt")
        with open(note_path, 'a') as file:
            file.write(f"{note_content}\n")
        messagebox.showinfo("Success", f"Note '{note_title}' added successfully.")

# Function to delete a note
def delete_note():
    note_title = simpledialog.askstring("Input", "Enter the title of the note to delete:")
    if note_title:
        notes_dir = 'notes'
        note_path = os.path.join(notes_dir, f"{note_title}.txt")
        
        if os.path.exists(note_path):
            os.remove(note_path)
            messagebox.showinfo("Success", f"Note '{note_title}' deleted successfully.")
        else:
            messagebox.showwarning("Error", f"Note '{note_title}' not found.")

# Function to exit the application
def exit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Notes App")

# Create buttons
view_button = tk.Button(root, text="View Notes", width=20, command=view_notes)
view_button.pack(pady=5)

add_button = tk.Button(root, text="Add Notes", width=20, command=add_note)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Notes", width=20, command=delete_note)
delete_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=20, command=exit_app)
exit_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
