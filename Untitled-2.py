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