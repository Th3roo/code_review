"""
A simple GUI application for a math quiz using Tkinter.
The quiz generates random addition or multiplication problems.
"""

import tkinter as tk
from tkinter import messagebox # Though not used in original, good for consistency
import random

DEFAULT_NUM_QUESTIONS = 5
RAND_NUM_MIN = 1
RAND_NUM_MAX = 10
OPERATIONS = ['+', '*']

class MathQuizApp:
    """
    A class to create and manage a simple math quiz GUI.
    """
    def __init__(self, root: tk.Tk, num_questions: int = DEFAULT_NUM_QUESTIONS):
        """
        Initializes the MathQuizApp.

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
        self.root.title("Тест по математике")
        # Consider making geometry more dynamic or configurable
        # self.root.geometry("350x300") # Example

        self.num_questions = num_questions
        self.questions_data = [] # List of tuples (question_str, answer_int)
        self.entry_widgets = []  # List to store tk.Entry widgets
        # self.label_widgets = [] # Not strictly needed if not modifying labels later

        self.result_label = None # Placeholder for the result label

        self._generate_questions()
        self._create_widgets()

    def _generate_questions(self):
        """
        Generates a list of questions, each with a text string and
        the correct numerical answer.
        Populates self.questions_data.
        """
        self.questions_data.clear()
        for _ in range(self.num_questions):
            num1 = random.randint(RAND_NUM_MIN, RAND_NUM_MAX)
            num2 = random.randint(RAND_NUM_MIN, RAND_NUM_MAX)
            operation = random.choice(OPERATIONS)
            question_str = f"{num1} {operation} {num2}"
            
            # Using eval() here. While generally a security risk if the string
            # is from an untrusted source, it's used here on an internally
            # generated string, making it relatively safe for this context.
            # Alternatives would be direct calculation based on 'operation'.
            try:
                answer = eval(question_str)
            except Exception as e:
                # Fallback or error logging if eval fails unexpectedly
                print(f"Error evaluating question '{question_str}': {e}")
                answer = 0 # Default or error indicator
            self.questions_data.append((question_str, answer))

    def _create_widgets(self):
        """
        Creates and places the GUI widgets (labels, entries, button)
        for the quiz.
        """
        self.entry_widgets.clear()
        # self.label_widgets.clear()

        for i, (question_text, _) in enumerate(self.questions_data):
            label = tk.Label(self.root, text=f"{question_text} = ")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            # self.label_widgets.append(label)

            entry = tk.Entry(self.root, width=10) # Set a fixed width for entries
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entry_widgets.append(entry)

        check_btn = tk.Button(
            self.root, text="Проверка", command=self._check_answers
        )
        check_btn.grid(
            row=self.num_questions, column=0, columnspan=2, pady=10
        )

        # Create result label once and keep a reference to update it
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(
            row=self.num_questions + 1, column=0, columnspan=2, pady=5
        )

    def _check_answers(self):
        """
        Checks the user's answers against the correct ones, updates entry
        backgrounds, and displays the score.
        """
        if len(self.entry_widgets) != self.num_questions:
            messagebox.showerror("Ошибка", "Несоответствие полей ввода!")
            return

        correct_count = 0
        for i in range(self.num_questions):
            _, correct_answer = self.questions_data[i]
            entry_widget = self.entry_widgets[i]
            user_answer_str = entry_widget.get().strip()

            try:
                if not user_answer_str: # Handle empty input
                    entry_widget.config(bg="yellow") # Mark empty
                    continue

                user_answer_int = int(user_answer_str)
                if user_answer_int == correct_answer:
                    entry_widget.config(bg="lightgreen") # Correct
                    correct_count += 1
                else:
                    entry_widget.config(bg="salmon")  # Incorrect
            except ValueError:
                entry_widget.config(bg="salmon")  # Not an integer
            except IndexError:
                # Should not happen if lists are managed correctly
                messagebox.showerror("Ошибка", "Ошибка при проверке ответов.")
                return

        self.result_label.config(
            text=f"Правильных ответов: {correct_count}/{self.num_questions}"
        )
        # Optional: Display result in a messagebox as well or instead
        # messagebox.showinfo("Результат",
        # f"Правильных ответов: {correct_count}/{self.num_questions}")


def main():
    """
    Sets up the main Tkinter window and starts the MathQuizApp.
    """
    try:
        root = tk.Tk()
        app = MathQuizApp(root, num_questions=DEFAULT_NUM_QUESTIONS)
        root.mainloop()
    except TypeError as te:
        print(f"Configuration Error: {te}")
        messagebox.showerror("Ошибка конфигурации", str(te))
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
        messagebox.showerror("Ошибка конфигурации", str(ve))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        messagebox.showerror(
            "Непредвиденная ошибка",
            "Произошла ошибка при запуске приложения."
        )

if __name__ == "__main__":
    main()
