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

         # Sorting UI
        self.sort_label = tk.Label(self.window, text="Sort By", bg="#ea86b6")
        self.sort_label.grid(column=0, row=1, padx=5)

        self.sort_options = ["Title", "Ready Time", "Servings"]
        self.sort_var = tk.StringVar()
        self.sort_var.set(self.sort_options[0])  # Default to "Title"

        self.sort_menu = tk.OptionMenu(self.window, self.sort_var, *self.sort_options)
        self.sort_menu.grid(column=1, row=1, padx=5)

        def run_search_query(self):
        query = self.search_entry.get().lower().strip()
        sort_method = self.sort_var.get().lower().replace(" ", "")  # Normalize to match sort keys
        
        if not query:
            self.show_error("Please enter a recipe name.")
            return

        print(f"Searching for: {query}")
        print(f"Sorting by: {sort_method}")

        if sorted_recipes:
            print(f"Found recipes: {sorted_recipes}")
            self.show_recipe(sorted_recipes[0])  # Display the first sorted recipe
        else:
            self.show_error("No recipes found.")

    def get_sorted_recipes_from_csv(self, query, sort_by="title"):
        try:
            with open(CSV_FILE_PATH, mode='r') as file:
                reader = csv.DictReader(file)
                recipes = [row for row in reader if query in row['title'].strip().lower()]
            
            print(f"Recipes matching query '{query}': {recipes}") 