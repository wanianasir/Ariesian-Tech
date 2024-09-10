from tkinter import *
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    include_special = special_var.get()
    include_numbers = numbers_var.get()

    characters = string.ascii_letters  # Add letters (lowercase and uppercase)

    if include_numbers:
        characters += string.digits  # Add digits (0-9)
    if include_special:
        characters += string.punctuation  # Add special characters

    # Randomly select characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(text=password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_display['text']
    if password:
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(password)  # Add the password to the clipboard
        copied_label.config(text="Password copied to clipboard!", fg="green")
    else:
        copied_label.config(text="No password to copy!", fg="red")

# Main window
root = Tk()
root.title('Password Generator')
root.geometry('400x300')
root.resizable(False, False)

# Title label
title_label = Label(root, text="Password Generator", font=("Helvetica", 18))
title_label.pack(pady=10)

# Length label and entry
length_label = Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = Entry(root, width=10)
length_entry.pack()

# Options for complexity
special_var = BooleanVar()
numbers_var = BooleanVar()

special_check = Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack(pady=5)

numbers_check = Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack(pady=5)

# Generate password button
generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_display = Label(root, text="", font=("Helvetica", 12), bg="white", relief="sunken", width=30)
password_display.pack(pady=10)

# Copy to clipboard button
copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Label to show the copy status
copied_label = Label(root, text="")
copied_label.pack()

# Start the Tkinter main loop
root.mainloop()
