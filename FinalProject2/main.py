import tkinter as tk
from vote_app import VotingApp

def main():
    window = tk.Tk()
    window.geometry("250x250")
    app = VotingApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()