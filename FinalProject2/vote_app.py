import tkinter as tk
from tkinter import messagebox
from voter import validate_voter_id, id_used
from admin import admin_login, manage_candidates
import csv
import os


class VotingApp:
    """Main class for the voting application."""

    def __init__(self, root):
        """
        Initialize the voting application.

        Args:
            root (Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Voting System")
        self.root.geometry("500x400")

        self.votes_file = "votes.csv"
        self.candidates_file = "candidates.csv"

        self.initialize_files()
        self.candidates = self.load_candidates()

        self.vote_menu_frame = tk.Frame(root)
        self.vote_menu_frame.pack()

        tk.Label(self.vote_menu_frame, text="VOTE MENU", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.vote_menu_frame, text="Start Voting", command=self.show_id_input, font=("Arial", 12)).pack(
            pady=5)
        tk.Button(self.vote_menu_frame, text="Login as Admin", command=self.admin_login, font=("Arial", 12)).pack(
            pady=5)
        tk.Button(self.vote_menu_frame, text="Exit", command=self.exit_app, font=("Arial", 12)).pack(pady=5)

        self.id_input_frame = tk.Frame(root)
        tk.Label(self.id_input_frame, text="Enter Your ID (8 digits):", font=("Arial", 12)).pack(pady=10)
        self.id_entry = tk.Entry(self.id_input_frame, font=("Arial", 12))
        self.id_entry.pack(pady=5)
        tk.Button(self.id_input_frame, text="Submit", command=self.validate_id, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.id_input_frame, text="Back", command=self.show_vote_menu, font=("Arial", 12)).pack(pady=5)

        self.candidate_menu_frame = tk.Frame(root)

    def initialize_files(self):
        """Create the necessary csv files if they do not exist."""
        if not os.path.exists(self.votes_file):
            with open(self.votes_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Candidate"])
        if not os.path.exists(self.candidates_file):
            with open(self.candidates_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Candidate"])
                writer.writerow(["John"])
                writer.writerow(["Jane"])

    def load_candidates(self):
        """Load candidates from the candidates csv file."""
        candidates = []
        with open(self.candidates_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                candidates.append(row["Candidate"])
        return candidates

    def save_candidates(self):
        """Save the updated list of candidates to the csv file."""
        with open(self.candidates_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Candidate"])
            for candidate in self.candidates:
                writer.writerow([candidate])

    def show_vote_menu(self):
        """Display the main vote menu."""
        self.id_input_frame.pack_forget()
        self.candidate_menu_frame.pack_forget()
        self.vote_menu_frame.pack()

    def show_id_input(self):
        """Display the ID input menu."""
        self.vote_menu_frame.pack_forget()
        self.id_input_frame.pack()

    def validate_id(self):
        """Validate the user's ID and proceed to the candidate menu."""
        user_id = self.id_entry.get().strip()
        if not validate_voter_id(user_id):
            messagebox.showerror("Invalid ID", "ID must be exactly 8 digits.")
            return
        if id_used(user_id, self.votes_file):
            messagebox.showerror("Duplicate ID", "This ID has already been used.")
            return
        self.current_id = user_id
        self.id_entry.delete(0, tk.END)
        self.show_candidate_menu()

    def show_candidate_menu(self):
        """Display the candidate menu for voting."""
        self.id_input_frame.pack_forget()
        for widget in self.candidate_menu_frame.winfo_children():
            widget.destroy()
        tk.Label(self.candidate_menu_frame, text="CANDIDATE MENU", font=("Arial", 16)).pack(pady=10)
        for candidate in self.candidates:
            tk.Button(self.candidate_menu_frame, text=f"Vote {candidate}",
                      command=lambda c=candidate: self.vote(c), font=("Arial", 12)).pack(pady=5)
        tk.Button(self.candidate_menu_frame, text="Back", command=self.show_vote_menu, font=("Arial", 12)).pack(pady=5)
        self.candidate_menu_frame.pack()

    def vote(self, candidate):
        """Record the user's vote."""
        with open(self.votes_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.current_id, candidate])
        messagebox.showinfo("Vote Recorded", f"You voted for {candidate}.")
        self.current_id = None
        self.show_vote_menu()

    def admin_login(self):
        """Handle admin login and candidate management."""
        if admin_login():
            self.candidates = manage_candidates(self.candidates, self.save_candidates)

    def exit_app(self):
        """Exit the application and display voting results."""
        votes_count = {candidate: 0 for candidate in self.candidates}
        total_votes = 0
        with open(self.votes_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                candidate = row["Candidate"]
                if candidate in votes_count:
                    votes_count[candidate] += 1
                    total_votes += 1
        results_message = "Results:\n" + "\n".join([f"{candidate} - {count} votes"
                                                    for candidate, count in votes_count.items()])
        results_message += f"\nTotal Votes - {total_votes}"
        messagebox.showinfo("Voting Results", results_message)
        self.root.destroy()
