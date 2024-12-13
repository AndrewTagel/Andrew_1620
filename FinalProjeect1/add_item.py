import tkinter as tk
from tkinter import messagebox
import list_manager

def add_to_list(parent_window, options_list, options_csv):
    """
    Open a new window to allow the user to add an item to the options list.

    This function creates a popup window where the user can enter a new item.
    The item is added to the options list and saved to the specified csv file.
    Appropriate success or error messages are displayed.
    """
    def add_item():
        """
        Add the entered item to the options list and save the list.

        Validates the input to ensure it is not empty, adds it to the list,
        saves the updated list to the specified csv file, and displays a success
        message. Displays an error or warning if the operation fails.
        """
        item = entry.get()
        if item.strip():
            try:
                list_manager.add_item(options_list, item)
                list_manager.save_options(options_csv, options_list)
                messagebox.showinfo("Success", f"Added '{item}' to the list!")
                entry.delete(0, tk.END)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please enter a valid item.")

    # Create a popup window for adding a new item
    add_window = tk.Toplevel(parent_window)
    add_window.title("Add to List")
    tk.Label(add_window, text="Enter item:").pack(pady=5)
    entry = tk.Entry(add_window)
    entry.pack(pady=5)
    tk.Button(add_window, text="Add", command=add_item).pack(pady=5)
