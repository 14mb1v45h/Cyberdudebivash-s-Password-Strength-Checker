# main.py - Cyberdudebivash's Password Strength Checker
# This GUI app checks password strength using zxcvbn, displays percentage, checks against cybersecurity guidelines (NIST-inspired: 8+ chars, mix of upper/lower/digit/special, not common), and suggests strong passwords.
# Features: Real-time feedback, generation of secure passwords via secrets.
# Note: For educational purposes. Use responsibly.

import tkinter as tk
from tkinter import messagebox
import zxcvbn  # For strength analysis
import secrets
import string

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyberdudebivash's Password Strength Checker")
        self.root.geometry("500x400")
        
        # UI Elements
        tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
        self.pass_entry = tk.Entry(root, show="*", width=50)
        self.pass_entry.pack(pady=5)
        
        self.check_btn = tk.Button(root, text="Check Strength", command=self.check_strength)
        self.check_btn.pack(pady=10)
        
        self.strength_label = tk.Label(root, text="", font=("Arial", 12))
        self.strength_label.pack(pady=5)
        
        self.percent_label = tk.Label(root, text="", font=("Arial", 12))
        self.percent_label.pack(pady=5)
        
        self.guidelines_label = tk.Label(root, text="", font=("Arial", 12))
        self.guidelines_label.pack(pady=5)
        
        self.feedback_text = tk.Label(root, text="", font=("Arial", 10), wraplength=400)
        self.feedback_text.pack(pady=10)
        
        self.suggest_btn = tk.Button(root, text="Suggest Strong Password", command=self.suggest_password)
        self.suggest_btn.pack(pady=10)
        
        self.suggested_pass_label = tk.Label(root, text="", font=("Arial", 12))
        self.suggested_pass_label.pack(pady=5)

    def check_strength(self):
        password = self.pass_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter a password.")
            return
        
        result = zxcvbn.zxcvbn(password)
        score = result['score']  # 0-4
        percent = (score / 4) * 100
        strength = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"][score]
        
        # Cybersecurity Guidelines Check (NIST SP 800-63B inspired)
        meets_guidelines = (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password) and
            result['guesses_log10'] > 10  # Not easily guessable
        )
        
        guidelines_status = "Meets Cybersecurity Guidelines" if meets_guidelines else "Does Not Meet Cybersecurity Guidelines"
        
        feedback = result['feedback']['warning'] or "No specific warnings."
        suggestions = ", ".join(result['feedback']['suggestions']) or "No suggestions."
        
        self.strength_label.config(text=f"Strength: {strength}")
        self.percent_label.config(text=f"Percentage: {percent:.2f}%")
        self.guidelines_label.config(text=guidelines_status)
        self.feedback_text.config(text=f"Feedback: {feedback}\nSuggestions: {suggestions}")

    def suggest_password(self):
        length = 16  # Recommended minimum
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(chars) for _ in range(length))
        
        self.suggested_pass_label.config(text=f"Suggested Password: {password}")
        messagebox.showinfo("Suggestion", f"Generated strong password: {password}\nCopy and use it securely.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()