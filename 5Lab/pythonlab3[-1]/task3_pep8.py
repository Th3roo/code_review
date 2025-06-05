def get_max_number():
    """Gets a positive integer for the maximum possible number."""
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
    """Gets Sergey's guess as a set of numbers, or 'Помогите!'."""
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
    """Gets Ivan's answer ('Да' or 'Нет')."""
    while True:
        answer_str = input("Ответ Ивана ('Да'/'Нет'): ").strip().lower()
        if answer_str in ["да", "нет"]:
            return answer_str
        else:
            print("Некорректный ответ. Пожалуйста, введите 'Да' или 'Нет'.")


def play_guess_the_number():
    """Main logic for the 'Guess the Number' game."""
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
    print("--- Игра 'Угадай число' ---")
    play_guess_the_number()


if __name__ == "__main__":
    main()
