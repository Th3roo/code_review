import tkinter as tk
from tkinter import messagebox
import random

class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Математический тест")
        self.root.geometry("600x400")
        
        # Список для хранения вопросов, правильных ответов и полей ввода
        self.questions = []
        self.correct_answers = []
        self.entry_fields = []
        
        # Генерация вопросов
        self.generate_questions()
        
        # Создание интерфейса
        self.create_interface()
        
    def generate_questions(self):
        """Генерация 5 случайных вопросов из таблицы умножения"""
        for _ in range(5):
            num1 = random.randint(2, 10)
            num2 = random.randint(2, 10)
            question = f"{num1} × {num2} = "
            answer = num1 * num2
            self.questions.append(question)
            self.correct_answers.append(answer)
    
    def create_interface(self):
        """Создание графического интерфейса"""
        # Заголовок
        title_label = tk.Label(self.root, text="Решите примеры", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Создание рамки для вопросов
        questions_frame = tk.Frame(self.root)
        questions_frame.pack(pady=20)
        
        # Создание вопросов и полей ввода
        for i in range(5):
            # Рамка для каждого вопроса
            frame = tk.Frame(questions_frame)
            frame.pack(pady=10)
            
            # Текст вопроса
            question_label = tk.Label(frame, text=self.questions[i], font=("Arial", 12))
            question_label.pack(side=tk.LEFT, padx=10)
            
            # Поле ввода ответа
            entry = tk.Entry(frame, width=10, font=("Arial", 12))
            entry.pack(side=tk.LEFT, padx=10)
            self.entry_fields.append(entry)
            
        # Кнопка проверки
        check_button = tk.Button(self.root, text="Проверка", font=("Arial", 12, "bold"),
                               command=self.check_answers)
        check_button.pack(pady=20)
    
    def check_answers(self):
        """Проверка ответов пользователя"""
        correct_count = 0
        
        # Проверка каждого ответа
        for i in range(5):
            try:
                user_answer = int(self.entry_fields[i].get())
                if user_answer == self.correct_answers[i]:
                    correct_count += 1
                    self.entry_fields[i].config(bg="white")  # Правильный ответ - белый фон
                else:
                    self.entry_fields[i].config(bg="red")    # Неправильный ответ - красный фон
            except ValueError:
                self.entry_fields[i].config(bg="red")        # Если введено не число - красный фон
        
        # Вывод результата
        messagebox.showinfo("Результат", f"Правильных ответов: {correct_count} из 5")

# Создание главного окна
if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuiz(root)
    root.mainloop()
