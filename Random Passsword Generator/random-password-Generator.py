import tkinter as tk
import random
import string
import pyperclip
from PIL import Image, ImageTk

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        # Create a Canvas widget
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        # Load background image
        self.bg_image = Image.open("p_g-2.jpg")
        self.bg_image = self.bg_image.resize((500, 500))  # Resize the image to fit the canvas
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        # Password length label and entry
        self.label_length = tk.Label(root, text="Password Length:", bg="white")
        self.label_length_window = self.canvas.create_window(100, 50, anchor="nw", window=self.label_length)
        self.entry_length = tk.Entry(root)
        self.entry_length_window = self.canvas.create_window(250, 50, anchor="nw", window=self.entry_length)

        # Checkboxes for character types
        self.var_lower = tk.IntVar()
        self.check_lower = tk.Checkbutton(root, text="Lowercase", variable=self.var_lower)
        self.check_lower_window = self.canvas.create_window(100, 100, anchor="nw", window=self.check_lower)

        self.var_upper = tk.IntVar()
        self.check_upper = tk.Checkbutton(root, text="Uppercase", variable=self.var_upper)
        self.check_upper_window = self.canvas.create_window(250, 100, anchor="nw", window=self.check_upper)

        self.var_digits = tk.IntVar()
        self.check_digits = tk.Checkbutton(root, text="Digits", variable=self.var_digits)
        self.check_digits_window = self.canvas.create_window(100, 150, anchor="nw", window=self.check_digits)

        self.var_symbols = tk.IntVar()
        self.check_symbols = tk.Checkbutton(root, text="Symbols", variable=self.var_symbols)
        self.check_symbols_window = self.canvas.create_window(250, 150, anchor="nw", window=self.check_symbols)

        # Generate password button
        self.button_generate = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.button_generate_window = self.canvas.create_window(100, 200, anchor="nw", window=self.button_generate)

        # Display generated password
        self.generated_password = tk.StringVar()
        self.label_password = tk.Label(root, textvariable=self.generated_password, wraplength=300, bg="white")
        self.label_password_window = self.canvas.create_window(100, 250, anchor="nw", window=self.label_password)

        # Copy password button
        self.button_copy = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.button_copy_window = self.canvas.create_window(100, 300, anchor="nw", window=self.button_copy)

    def generate_password(self):
        length = int(self.entry_length.get())
        if length <= 0:
            self.generated_password.set("Please enter a valid password length.")
            return

        character_sets = []
        if self.var_lower.get():
            character_sets.append(string.ascii_lowercase)
        if self.var_upper.get():
            character_sets.append(string.ascii_uppercase)
        if self.var_digits.get():
            character_sets.append(string.digits)
        if self.var_symbols.get():
            character_sets.append(string.punctuation)

        if not character_sets:
            self.generated_password.set("Please select at least one character type.")
            return

        password = ''.join(random.choice(''.join(character_set)) for character_set in character_sets for _ in range(length))
        self.generated_password.set(password)

    def copy_to_clipboard(self):
        password = self.generated_password.get()
        if password:
            pyperclip.copy(password)
            self.generated_password.set("Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
