import tkinter as tk
from tkinter import messagebox

class MathTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Математический тест")
        
        # Создаем список вопросов и правильных ответов
        self.questions = [
            ("7 × 8 = ", 56),
            ("12 + 15 = ", 27),
            ("9 × 6 = ", 54),
            ("20 - 7 = ", 13),
            ("4 × 7 = ", 28)
        ]
        
        self.entries = []  # Список для хранения полей ввода
        
        # Создаем вопросы и поля для ввода
        for i, (question, _) in enumerate(self.questions):
            label = tk.Label(root, text=question)
            label.grid(row=i, column=0, padx=5, pady=5)
            
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)
        
        # Кнопка проверки
        check_button = tk.Button(root, text="Проверка", command=self.check_answers)
        check_button.grid(row=len(self.questions), column=0, columnspan=2, pady=10)

    def check_answers(self):
        correct_count = 0
        
        # Проверяем каждый ответ
        for i, (entry, (_, correct_answer)) in enumerate(zip(self.entries, self.questions)):
            try:
                user_answer = int(entry.get())
                if user_answer == correct_answer:
                    correct_count += 1
                    entry.config(bg="white")  # Правильный ответ - белый фон
                else:
                    entry.config(bg="red")    # Неправильный ответ - красный фон
            except ValueError:
                entry.config(bg="red")        # Если введено не число - красный фон
        
        # Выводим результат
        messagebox.showinfo("Результат", f"Правильных ответов: {correct_count} из {len(self.questions)}")

# Создаем и запускаем приложение
root = tk.Tk()
app = MathTest(root)
root.mainloop()
