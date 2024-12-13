import tkinter as tk
from tkinter import messagebox
import bingo
import list_manager
import add_item

# Path to the csv file where the bingo card will be saved
Bingo_csv = "bingo_card.csv"

# Path to the csv file where the options list is stored
Options_csv = "options_list.csv"

# Load the list of options from the csv file
options_list = list_manager.load_options(Options_csv)

def generate_bingo_card():
    """
    Generate a bingo card using the options list and save it to a csv file.

    This function calls the `generate_bingo_card` function from the `bingo` module,
    saves the generated bingo card to the `Bingo_csv` file, and displays a success
    or error message based on the outcome.
    """
    try:
        card = bingo.generate_bingo_card(options_list)
        bingo.save_bingo_card(Bingo_csv, card)
        messagebox.showinfo("Success", f"Bingo card generated and saved to {Bingo_csv}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Main tkinter window setup
window = tk.Tk()
window.geometry("500x300")
window.title("Bingo App")

# Add main window components
tk.Label(window, text="Choose an action:", font=("Arial", 14)).pack(pady=10)
tk.Button(window, text="Generate Bingo Card", command=generate_bingo_card).pack(pady=10)
tk.Button(window, text="Add to List", command=lambda: add_item.add_to_list(window, options_list, Options_csv)).pack(pady=10)

# Run the tkinter main loop
window.mainloop()
