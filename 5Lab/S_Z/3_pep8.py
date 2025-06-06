"""
Implements a number guessing game helper.

This script helps determine a number that "Ivan" has thought of, up to a
user-defined maximum. "Sergey" (the user of this script) inputs sets of
numbers, and "Ivan" (another person, conceptually) responds whether his
chosen number is within that set ('Да' - Yes) or not ('Нет' - No).
The script narrows down the possibilities until Sergey types 'Помогите!'
(Help!), at which point it lists all remaining possible numbers.
Input validation is performed for user inputs.
"""


def task_3_guess_the_number():
    """
    Interactively helps a user determine a number based on yes/no questions.

    The function first prompts for the maximum possible number (N).
    Then, it enters a loop where the user (Sergey) inputs a set of numbers
    he guesses might contain Ivan's secret number. The user also inputs
    Ivan's response ('Да' or 'Нет').
    The set of possible numbers is updated based on Ivan's answers.
    The loop continues until the user types 'Помогите!', at which point
    the script prints all numbers that could still be Ivan's secret number,
    sorted in ascending order.
    Handles various input errors, such as non-integer inputs, empty inputs,
    and invalid responses from Ivan.
    """
    while True:
        try:
            n_max = int(input("Введите максимальное число (N): "))
            if n_max > 0:
                break
            else:
                print("Максимальное число должно быть положительным.")
        except ValueError:
            print(
                "Некорректный ввод. Пожалуйста, введите целое число для максимального числа."
            )

    possible_numbers = set(range(1, n_max + 1))

    while True:
        guess_input_str = input(
            "Нужное число есть среди вот этих чисел (или 'Помогите!'): "
        ).strip()

        if guess_input_str.lower() == "помогите!":
            break

        if not guess_input_str:
            print("Ввод не может быть пустым. Введите числа или 'Помогите!'.")
            continue

        try:
            sergey_guesses = set(map(int, guess_input_str.split()))
            if not sergey_guesses:
                print("Вы не ввели числа для угадывания.")
                continue
            if not all(1 <= num <= n_max for num in sergey_guesses):
                print(f"Числа должны быть в диапазоне от 1 до {n_max}.")
                continue
        except ValueError:
            print(
                "Некорректный ввод чисел. Вводите числа через пробел или 'Помогите!'."
            )
            continue

        while True:
            ivan_answer = input("Ответ Ивана ('Да'/'Нет'): ").strip().lower()
            if ivan_answer in ["да", "нет"]:
                break
            else:
                print("Некорректный ответ Ивана. Введите 'Да' или 'Нет'.")

        if ivan_answer == "да":
            possible_numbers.intersection_update(sergey_guesses)
        elif ivan_answer == "нет":
            possible_numbers.difference_update(sergey_guesses)

        if not possible_numbers:
            print("Иван, кажется, ты ошибся в своих ответах, "
                  "или такого числа не существует среди возможных.")

    if possible_numbers:
        print("Иван мог загадать следующие числа:",
              " ".join(map(str, sorted(list(possible_numbers)))))
    else:
        print("Нет возможных чисел, которые мог загадать Иван, "
              "исходя из предоставленных ответов.")


if __name__ == '__main__':
    print("--- Задача 3: Игра Угадайка ---")
    task_3_guess_the_number()
