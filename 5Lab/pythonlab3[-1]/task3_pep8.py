"""
Implements the "Guess the Number" game logic.

This script facilitates a game where one person (Ivan, conceptually) thinks
of a number up to a maximum N, and another person (Sergey, the user)
tries to guess it by providing sets of numbers and receiving 'Да' (Yes) or
'Нет' (No) answers from Ivan. The script helps Sergey narrow down the
possibilities until he asks for help or the possibilities are exhausted.
"""


def get_max_number():
    """
    Gets a positive integer for the maximum possible number (N) from the user.

    Continuously prompts until a positive integer is entered. Handles
    ValueError for non-integer inputs and prompts again if a non-positive
    number is entered.

    Returns:
        int: The positive maximum number N.
    """
    while True:
        try:
            n_val = int(input("Введите максимальное число (N): "))
            if n_val > 0:
                return n_val
            else:
                print("Максимальное число должно быть положительным.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def get_sergeys_guess(max_n):
    """
    Gets Sergey's (user's) guess: a set of numbers or the command 'Помогите!'.

    Prompts the user to input space-separated numbers or 'Помогите!'.
    Validates that numbers are within the range [1, max_n].

    Args:
        max_n (int): The maximum possible number in the game, for validation.

    Returns:
        set or str: A set of integers representing Sergey's guessed numbers,
                    or the string "помогите!" if entered by the user.
    """
    while True:
        guess_input_str = input(
            "Нужное число есть среди вот этих чисел (или 'Помогите!'): "
        ).strip()

        if guess_input_str.lower() == "помогите!":
            return "помогите!"

        if not guess_input_str:
            print("Ввод не может быть пустым. Введите числа или 'Помогите!'.")
            continue

        try:
            guessed_numbers_set = set(map(int, guess_input_str.split()))
            if not guessed_numbers_set:
                print("Вы не ввели числа для угадывания.")
                continue

            valid_range = True
            for num in guessed_numbers_set:
                if not (1 <= num <= max_n):
                    print(
                        f"Ошибка: число {num} выходит за пределы диапазона [1, {max_n}]."
                    )
                    valid_range = False
                    break
            if not valid_range:
                continue

            return guessed_numbers_set
        except ValueError:
            print(
                "Некорректный ввод. Пожалуйста, введите числа, разделенные пробелом, или 'Помогите!'."
            )


def get_ivan_answer():
    """
    Gets Ivan's (conceptual other player's) answer ('Да' or 'Нет').

    Continuously prompts until 'да' or 'нет' (case-insensitive) is entered.

    Returns:
        str: Ivan's answer, either "да" or "нет".
    """
    while True:
        answer_str = input("Ответ Ивана ('Да'/'Нет'): ").strip().lower()
        if answer_str in ["да", "нет"]:
            return answer_str
        else:
            print("Некорректный ответ. Пожалуйста, введите 'Да' или 'Нет'.")


def play_guess_the_number():
    """
    Manages the main logic for the 'Guess the Number' game.

    Initializes the set of possible numbers based on user input N.
    Enters a loop where it gets Sergey's guess and Ivan's answer,
    updating the set of possible numbers accordingly.
    The loop breaks when Sergey types 'Помогите!' or if no possible numbers remain.
    Finally, prints the list of possible numbers Ivan could have thought of.
    """
    max_n = get_max_number()
    possible_numbers = set(range(1, max_n + 1))

    while True:
        sergeys_numbers = get_sergeys_guess(max_n)

        if sergeys_numbers == "помогите!":
            break

        if not isinstance(sergeys_numbers, set) or not sergeys_numbers:
            print("Произошла ошибка с вводом чисел Сергея, попробуйте снова."
                  )
            continue

        ivan_response = get_ivan_answer()

        if ivan_response == "да":
            possible_numbers.intersection_update(sergeys_numbers)
        elif ivan_response == "нет":
            possible_numbers.difference_update(sergeys_numbers)

        if not possible_numbers:
            print("Кажется, Иван ошибся в ответах, или такого числа нет.")

    if possible_numbers:
        print("\nИван мог загадать следующие числа:",
              " ".join(map(str, sorted(list(possible_numbers)))))
    else:
        print(
            "\nНет возможных чисел, которые мог загадать Иван, исходя из ответов."
        )


def main():
    """
    Main function to start the 'Guess the Number' game.
    Prints a welcome message and calls the core game logic function.
    """
    print("--- Игра 'Угадай число' ---")
    play_guess_the_number()


if __name__ == "__main__":
    main()
