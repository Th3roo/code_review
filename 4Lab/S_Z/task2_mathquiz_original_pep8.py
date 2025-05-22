"""
A simple GUI application for a math quiz using Tkinter.
The quiz generates random multiplication problems.
"""

import tkinter as tk
from tkinter import messagebox
import random

DEFAULT_NUM_QUESTIONS = 5
MIN_RAND_NUM = 2
MAX_RAND_NUM = 10

class MathQuiz:
    """
    A class to create and manage a simple math quiz GUI.
    """
    def __init__(self, root: tk.Tk, num_questions: int = DEFAULT_NUM_QUESTIONS):
        """
        Initializes the MathQuiz application.

        Args:
            root: The main Tkinter window.
            num_questions: The number of questions to generate for the quiz.

        Raises:
            TypeError: If root is not a tkinter.Tk instance or
                       num_questions is not an integer.
            ValueError: If num_questions is not positive.
        """
        if not isinstance(root, tk.Tk):
            raise TypeError("The root window must be a tkinter.Tk instance.")
        if not isinstance(num_questions, int):
            raise TypeError("Number of questions must be an integer.")
        if num_questions <= 0:
            raise ValueError("Number of questions must be positive.")

        self.root = root
        self.root.title("Математический тест")
        self.root.geometry("600x400")  # Consider making this adaptable

        self.num_questions = num_questions
        self.questions_text = []  # Stores the string form of questions
        self.correct_answers = [] # Stores the numerical correct answers
        self.entry_fields = []    # Stores tk.Entry widgets

        self.generate_questions()
        self.create_interface()

    def generate_questions(self):
        """
        Generates a specified number of random multiplication questions.
        Populates self.questions_text and self.correct_answers.
        """
        self.questions_text.clear()
        self.correct_answers.clear()
        for _ in range(self.num_questions):
            num1 = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
            num2 = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
            question = f"{num1} × {num2} = "
            answer = num1 * num2
            self.questions_text.append(question)
            self.correct_answers.append(answer)

    def create_interface(self):
        """
        Creates the graphical user interface for the quiz.
        """
        # Title Label
        title_label = tk.Label(
            self.root, text="Решите примеры", font=("Arial", 16, "bold")
        )
        title_label.pack(pady=10)

        # Frame for questions
        questions_frame = tk.Frame(self.root)
        questions_frame.pack(pady=20)

        self.entry_fields.clear() # Ensure list is empty before repopulating
        for i in range(self.num_questions):
            # Frame for each question row (label + entry)
            frame = tk.Frame(questions_frame)
            frame.pack(pady=10, fill=tk.X, padx=20) # Fill for better spacing

            # Question Label
            question_label = tk.Label(
                frame, text=self.questions_text[i], font=("Arial", 12)
            )
            # Pack label to the left, allow expansion for alignment
            question_label.pack(side=tk.LEFT, padx=(0, 10))

            # Entry field for answer
            entry = tk.Entry(frame, width=10, font=("Arial", 12))
            # Pack entry to the right, allows label to determine width mostly
            entry.pack(side=tk.LEFT, padx=(0, 10))
            self.entry_fields.append(entry)

        # Check Answers Button
        check_button = tk.Button(
            self.root,
            text="Проверка",
            font=("Arial", 12, "bold"),
            command=self.check_answers
        )
        check_button.pack(pady=20)

    def check_answers(self):
        """
        Checks the user's answers against the correct ones.
        Updates UI to show correct/incorrect answers and displays a summary.
        """
        if len(self.entry_fields) != self.num_questions or \
           len(self.correct_answers) != self.num_questions:
            # This indicates an internal state error, should not happen in normal flow
            messagebox.showerror(
                "Ошибка",
                " несоответствие количества полей ввода и ответов."
            )
            return

        correct_count = 0
        for i in range(self.num_questions):
            entry_widget = self.entry_fields[i]
            try:
                user_answer_str = entry_widget.get()
                if not user_answer_str: # Handle empty input
                    entry_widget.config(bg="yellow") # Mark empty answers
                    continue

                user_answer = int(user_answer_str)
                if user_answer == self.correct_answers[i]:
                    correct_count += 1
                    entry_widget.config(bg="white")  # Correct: white
                else:
                    entry_widget.config(bg="red")    # Incorrect: red
            except ValueError:
                # If input is not a valid integer
                entry_widget.config(bg="red")
            except IndexError:
                # Should not happen if lists are managed correctly
                messagebox.showerror("Ошибка", "Ошибка при проверке ответов.")
                return


        messagebox.showinfo(
            "Результат",
            f"Правильных ответов: {correct_count} из {self.num_questions}"
        )

def main():
    """
    Creates the main window and starts the Tkinter event loop for the quiz.
    """
    try:
        root = tk.Tk()
        # One could pass a different number of questions here if desired
        app = MathQuiz(root, num_questions=DEFAULT_NUM_QUESTIONS)
        root.mainloop()
    except TypeError as te:
        print(f"Configuration Error: {te}")
        messagebox.showerror("Ошибка конфигурации", str(te))
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
        messagebox.showerror("Ошибка конфигурации", str(ve))
    except Exception as e:
        # Catch-all for other unexpected errors during setup
        print(f"An unexpected error occurred: {e}")
        messagebox.showerror(
            "Непредвиденная ошибка",
            "Произошла ошибка при запуске приложения."
        )

if __name__ == "__main__":
    main()
