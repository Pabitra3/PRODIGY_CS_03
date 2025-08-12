import tkinter as tk
from tkinter import messagebox
import re

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        # Title
        self.title_label = tk.Label(root, text="Password Complexity Checker", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Password input with eye toggle
        self.password_label = tk.Label(root, text="Enter Password:", font=("Helvetica", 12), bg="#f0f0f0")
        self.password_label.pack(pady=5)
        
        self.password_frame = tk.Frame(root, bg="#f0f0f0")
        self.password_frame.pack(pady=5)
        
        self.password_entry = tk.Entry(self.password_frame, show="*", width=30, font=("Helvetica", 12))
        self.password_entry.pack(side="left")
        
        self.show_password = tk.BooleanVar()
        self.eye_button = tk.Button(self.password_frame, text="👁", command=self.toggle_password, font=("Helvetica", 12), bg="#f0f0f0", relief="flat")
        self.eye_button.pack(side="left", padx=5)

        # Check button
        self.check_button = tk.Button(root, text="Check Strength", command=self.check_password, bg="#3b82f6", fg="white", font=("Helvetica", 12))
        self.check_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        self.result_label.pack(pady=5)
        self.feedback_text = tk.Text(root, height=10, width=40, font=("Helvetica", 10), wrap="word")
        self.feedback_text.pack(pady=5)
        self.feedback_text.config(state="disabled")

    def toggle_password(self):
        if self.show_password.get():
            self.password_entry.config(show="*")
            self.show_password.set(False)
            self.eye_button.config(text="👁")
        else:
            self.password_entry.config(show="")
            self.show_password.set(True)
            self.eye_button.config(text="👁‍🗨")

    def check_password(self):
        password = self.password_entry.get()
        score = 0
        feedback = []

        # Check length
        if len(password) < 8:
            feedback.append("Password is too short. Minimum length is 8 characters.")
        elif len(password) <= 12:
            score += 1
            feedback.append("Password length is acceptable (8-12 characters).")
        else:
            score += 2
            feedback.append("Password length is strong (>12 characters).")

        # Check for uppercase letters
        if re.search(r"[A-Z]", password):
            score += 1
            feedback.append("Contains uppercase letters: Good!")
        else:
            feedback.append("Add uppercase letters for better strength.")

        # Check for lowercase letters
        if re.search(r"[a-z]", password):
            score += 1
            feedback.append("Contains lowercase letters: Good!")
        else:
            feedback.append("Add lowercase letters for better strength.")

        # Check for numbers
        if re.search(r"[0-9]", password):
            score += 1
            feedback.append("Contains numbers: Good!")
        else:
            feedback.append("Add numbers for better strength.")

        # Check for special characters
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
            feedback.append("Contains special characters: Good!")
        else:
            feedback.append("Add special characters for better strength.")

        # Cap score at 5
        score = min(score, 5)

        # Determine strength
        if score <= 2:
            strength = "Weak"
            color = "red"
        elif score <= 4:
            strength = "Moderate"
            color = "orange"
        else:
            strength = "Strong"
            color = "green"

        # Update GUI
        self.result_label.config(text=f"Password Strength: {strength} (Score: {score}/5)", fg=color)
        self.feedback_text.config(state="normal")
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(tk.END, "Feedback:\n" + "\n".join(f"- {item}" for item in feedback))
        self.feedback_text.config(state="disabled")

def main():
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()