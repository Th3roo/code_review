"""
A simple GUI application for a math test using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox

class MathTest:
    """
    A class to create and manage a simple math test GUI.
    """
    def __init__(self, root: tk.Tk):
        """
        Initializes the MathTest application.

        Args:
            root: The main Tkinter window.

        Raises:
            TypeError: If root is not a tkinter.Tk instance.
        """
        if not isinstance(root, tk.Tk):
            raise TypeError("The root window must be a tkinter.Tk instance.")

        self.root = root
        self.root.title("Математический тест")

        # List of questions and their correct answers
        # Each tuple: (question_text: str, correct_answer: int)
        self.questions = [
            ("7 × 8 = ", 56),
            ("12 + 15 = ", 27),
            ("9 × 6 = ", 54),
            ("20 - 7 = ", 13),
            ("4 × 7 = ", 28)
        ]

        self.entries = []  # List to store tk.Entry widgets

        # Create and place question labels and entry fields
        for i, (question_text, _) in enumerate(self.questions):
            label = tk.Label(self.root, text=question_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        # Button to check answers
        check_button = tk.Button(
            self.root, text="Проверка", command=self.check_answers
        )
        check_button.grid(
            row=len(self.questions), column=0, columnspan=2, pady=10
        )

    def check_answers(self):
        """
        Checks the user's answers against the correct ones and updates UI.
        Displays the number of correct answers in a messagebox.
        """
        correct_count = 0

        # Validate each answer
        for i, entry_widget in enumerate(self.entries):
            # The second element of self.questions[i] is the correct answer
            _, correct_answer = self.questions[i]
            try:
                user_answer_str = entry_widget.get()
                if not user_answer_str: # Handle empty input
                    entry_widget.config(bg="yellow") # Mark empty answers
                    continue

                user_answer = int(user_answer_str)
                if user_answer == correct_answer:
                    correct_count += 1
                    entry_widget.config(bg="white")  # Correct: white background
                else:
                    entry_widget.config(bg="red")    # Incorrect: red background
            except ValueError:
                # If input is not a valid integer
                entry_widget.config(bg="red")

        # Display the result
        messagebox.showinfo(
            "Результат",
            f"Правильных ответов: {correct_count} из {len(self.questions)}"
        )

def main():
    """
    Creates the main window and starts the Tkinter event loop.
    """
    try:
        root = tk.Tk()
        app = MathTest(root)
        root.mainloop()
    except Exception as e:
        # Log the error or show a user-friendly message
        print(f"An error occurred: {e}")
        messagebox.showerror(
            "Ошибка приложения",
            "Произошла непредвиденная ошибка. Пожалуйста, перезапустите приложение."
        )

if __name__ == "__main__":
    main()
