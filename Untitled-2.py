import csv
import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for image handling
import os

# Constants
WINDOW_TITLE = "Recipe App"
CSV_FILE_PATH = "recipes.csv"

class RecipeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x600")  # Set window size
        self.window.configure(bg="#9ddfd3")
        self.window.title(WINDOW_TITLE)

        # Search UI
        self.search_label = tk.Label(self.window, text="Search Recipe", bg="#ea86b6")
        self.search_label.grid(column=0, row=0, padx=5)

        self.search_entry = tk.Entry(master=self.window, width=40)
        self.search_entry.grid(column=1, row=0, padx=5, pady=10) 

        self.search_button = tk.Button(self.window, text="Search", highlightbackground="#ea86b6",
                                       command=self.run_search_query)
        self.search_button.grid(column=2, row=0, padx=5)

        