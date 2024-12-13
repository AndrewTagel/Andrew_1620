from tkinter import simpledialog, messagebox


def admin_login():
    """
    Prompt for admin ID and validate it.

    Returns:
        bool: True if the admin ID is valid, False otherwise.
    """
    admin_id = simpledialog.askstring("Admin Login", "Enter Admin ID:")
    if admin_id == "12345678":
        return True
    messagebox.showerror("Access Denied", "Invalid Admin ID.")
    return False


def manage_candidates(candidates, save_candidates):
    """
    Allow the admin to add or remove candidates.

    Args:
        candidates (list): Current list of candidates.
        save_candidates (function): Function to save updated candidates to file.

    Returns:
        list: Updated list of candidates.
    """
    action = simpledialog.askstring("Admin Panel", "Choose Action: Add / Remove Candidate").strip().lower()
    if action == "add":
        new_candidate = simpledialog.askstring("Add Candidate", "Enter Candidate Name:")
        if new_candidate and new_candidate not in candidates:
            candidates.append(new_candidate)
            save_candidates()
            messagebox.showinfo("Success", f"{new_candidate} added successfully!")
        else:
            messagebox.showerror("Error", "Invalid or duplicate candidate.")
    elif action == "remove":
        candidate_to_remove = simpledialog.askstring("Remove Candidate", "Enter Candidate Name:")
        if candidate_to_remove in candidates:
            candidates.remove(candidate_to_remove)
            save_candidates()
            messagebox.showinfo("Success", f"{candidate_to_remove} removed successfully!")
        else:
            messagebox.showerror("Error", "Candidate not found.")
    else:
        messagebox.showerror("Error", "Invalid action.")
    return candidates