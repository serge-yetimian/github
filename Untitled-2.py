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

            # Sort recipes by selected criterion
            if sort_by == "readyinminutes":
                recipes.sort(key=lambda x: int(x['readyInMinutes']))
            elif sort_by == "servings":
                recipes.sort(key=lambda x: int(x['servings']))
            else:
                recipes.sort(key=lambda x: x['title'].strip().lower())  # Default to title sorting

            print(f"Sorted recipes: {recipes}")  # Debug: check sorted recipes
            return recipes
        except FileNotFoundError:
            self.show_error("CSV file not found.")
            return []
    
    
    def show_recipe(self, recipe):
        title = recipe['title']
        ready_in_minutes = recipe['readyInMinutes']
        servings = recipe['servings']
        instructions = recipe['recipe']
        image_path = recipe['image_path']

        self.clear_previous_output()

        # Recipe Title
        self.recipe_label = tk.Label(self.window, text=f"Recipe: {title}", bg="#9ddfd3", font=("Helvetica", 14, "bold"))
        self.recipe_label.grid(column=1, row=2, pady=5)

         # Recipe Details Text
        self.details_text = tk.Text(master=self.window, height=10, width=50, bg="#ffdada")
        self.details_text.grid(column=1, row=3, pady=10)
        self.details_text.insert(tk.END, f"Ready in Minutes: {ready_in_minutes}\n")
        self.details_text.insert(tk.END, f"Servings: {servings}\n\n")
        self.details_text.insert(tk.END, f"Instructions:\n{instructions}\n")

        # Load and display the image
        self.display_image(image_path)

    def display_image(self, image_path):
        try:
            if os.path.exists(image_path):
                # Open image using Pillow
                image = Image.open(image_path)
                image = image.resize((300, 200))  # Resize the image to fit within the UI
                img = ImageTk.PhotoImage(image)  # Convert image to Tkinter format

                # Create label for the image and display it
                self.image_label = tk.Label(self.window, image=img)
                self.image_label.image = img  # Keep a reference to the image
                self.image_label.grid(column=1, row=4, pady=10)
            
            else:
                self.show_error(f"Image not found: {image_path}")
        except Exception as e:
            self.show_error(f"Error loading image: {e}")
    
    def clear_previous_output(self):
        for widget in self.window.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()

    def show_error(self, message):
        self.clear_previous_output()
        error_label = tk.Label(self.window, text=message, fg="red", bg="#9ddfd3")
        error_label.grid(column=1, row=2, pady=10)

    def run_app(self):
        self.window.mainloop()

# Run the App
if __name__ == "__main__":
    recipe_app = RecipeApp()
    recipe_app.run_app()