import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# Function to open browser
def open_browser():
    os.system("start https://www.google.com")  # Opens the default web browser with Google

# Function to show logo
def show_logo():
    messagebox.showinfo("Jarvis", "Yes sir")
    root = tk.Tk()
    root.title("Jarvis")
    root.geometry("400x400")

    # Load and display the GIF logo
    logo_path = "jarvis_logo.gif"
    logo = Image.open(logo_path)
    logo = logo.resize((400, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(logo)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

    root.mainloop()

# Main function
def main():
    wakeup_call = "hey jarvis"
    query = input("Waiting for wakeup call...\n").lower()
    if query == wakeup_call:
        show_logo()
        action = input("What can I do for you, sir?\n").lower()
        if "open browser" in action:
            open_browser()
        elif "exit" in action or "quit" in action:
            print("Goodbye sir.")
        else:
            print("Sorry sir, I didn't understand your command.")

if __name__ == "__main__":
    main()
