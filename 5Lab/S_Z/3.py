# Задача 3: Игра "Угадайка"


def task_3_guess_the_number():
    """
    Решение задачи 3: Игра "Угадайка".
    Иван загадал натуральное число от 1 до N. Сергей пытается угадать.
    Программа имитирует диалог и в конце выводит, какие числа мог
    задумать Иван.
    """
    try:
        n_max = int(input("Введите максимальное число (N): "))
        if n_max <= 0:
            print("Максимальное число должно быть положительным.")
            return
    except ValueError:
        print("Некорректный ввод для максимального числа.")
        return

    possible_numbers = set(range(1, n_max + 1))

    while True:
        guess_input_str = input("Нужное число есть среди вот этих чисел "
                                "(или 'Помогите!'): ")
        if guess_input_str.strip().lower() == "помогите!":
            break

        try:
            sergey_guesses = set(map(int, guess_input_str.split()))
            if not sergey_guesses:
                print("Вы не ввели числа для угадывания.")
                continue
            # Проверка, что все числа Сергея в допустимом диапазоне
            if not all(1 <= num <= n_max for num in sergey_guesses):
                print(f"Числа должны быть в диапазоне от 1 до {n_max}.")
                continue
        except ValueError:
            print("Некорректный ввод чисел. Вводите числа через пробел.")
            continue

        ivan_answer = input("Ответ Ивана ('Да'/'Нет'): ").strip().lower()

        if ivan_answer == "да":
            possible_numbers.intersection_update(sergey_guesses)
        elif ivan_answer == "нет":
            possible_numbers.difference_update(sergey_guesses)
        else:
            print("Некорректный ответ Ивана. Введите 'Да' или 'Нет'.")
            continue  # Повторяем запрос ответа Ивана для тех же чисел Сергея

        if not possible_numbers:
            print("Иван, кажется, ты ошибся в своих ответах, "
                  "или такого числа не существует среди возможных.")
            return  # Завершаем, если не осталось вариантов

        # Если после ответа "Да" осталось одно число,
        # и это число было единственным в предположении Сергея,
        # то Сергей угадал. Но по условию мы ждем "Помогите!".

    if possible_numbers:
        print("Иван мог загадать следующие числа:",
              " ".join(map(str, sorted(list(possible_numbers)))))
    else:
        # Эта ситуация обычно возникает, если введено "Помогите!"
        # после того, как множество стало пустым из-за противоречивых ответов.
        print("Нет возможных чисел, которые мог загадать Иван, "
              "исходя из предоставленных ответов.")


if __name__ == '__main__':
    print("--- Задача 3: Игра Угадайка ---")
    task_3_guess_the_number()
