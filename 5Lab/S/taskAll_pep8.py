"""
A collection of interactive programs.

This module provides a menu-driven interface to access various interactive
programs, including:
- City locator: Finds the country of a city based on user input.
- Pizza order tracker: Manages pizza orders for multiple customers.
- Number guessing game: Allows the user to play a number guessing game.
- Genealogy tree builder: Calculates the height of individuals in a family tree.
- Translation test: Tests the user's knowledge of Russian-English word pairs.
"""


def locate_cities():
    """
    Locates the country of a given city based on user-provided data.

    The user first inputs a number of countries, followed by the country name
    and a list of cities in that country. Then, the user can input city names
    to find out their respective countries.
    """
    while True:
        try:
            k = int(input("Кол-во стран: "))
            if k > 0:
                break
            else:
                print("Количество стран должно быть положительным числом.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    country_data = {}

    for i in range(k):
        while True:
            entry_str = input(f"{i + 1} страна: ")
            entry = entry_str.split()
            if len(entry) >= 2:
                country = entry[0]
                cities = entry[1:]
                for city in cities:
                    country_data[city] = country
                break
            else:
                print("Введите страну и хотя бы один город через пробел.")

    for i in range(3):
        city = input(f"{i + 1} город: ").strip()
        if not city:
            print("Название города не может быть пустым.")
            continue
        if city in country_data:
            print(f"Город {city} расположен в стране {country_data[city]}.")
        else:
            print(f"По городу {city} данных нет.")


def pizza_orders():
    """
    Manages pizza orders for multiple customers.

    The user inputs the number of orders, and for each order, provides the
    customer's name, pizza name, and quantity. The program then prints
    a summary of all orders, grouped by customer and sorted alphabetically.
    """
    while True:
        try:
            n = int(input("Введите кол-во заказов: "))
            if n > 0:
                break
            else:
                print("Количество заказов должно быть положительным числом.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    orders = {}

    for i in range(n):
        while True:
            entry_str = input(f"{i + 1} заказ: ")
            entry = entry_str.split(' ', 2)
            if len(entry) == 3:
                try:
                    buyer, pizza, amount_str = entry[0], entry[1], entry[2]
                    amount = int(amount_str)
                    if amount > 0:
                        if buyer not in orders:
                            orders[buyer] = {}
                        if pizza in orders[buyer]:
                            orders[buyer][pizza] += amount
                        else:
                            orders[buyer][pizza] = amount
                        break
                    else:
                        print(
                            "Количество пиццы должно быть положительным числом."
                        )
                except ValueError:
                    print("Количество пиццы должно быть целым числом.")
            else:
                print(
                    "Введите данные заказа в формате: Имя Покупателя НазваниеПиццы Количество"
                )

    for buyer in sorted(orders):
        print(f"{buyer}:")
        for pizza, amount in sorted(orders[buyer].items()):
            print(f"  {pizza}: {amount}")


def guess_the_number():
    """
    Plays a number guessing game with the user.

    The user first specifies a maximum number. The program then tries to guess
    a number chosen by the user (conceptually) by asking if the number is in
    a presented set. The user responds 'Да' (Yes) or 'Нет' (No).
    The program continues until it identifies the number or the user asks for help.
    """
    while True:
        try:
            n = int(input("Введите максимальное число: "))
            if n > 0:
                break
            else:
                print("Максимальное число должно быть положительным.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    possible_numbers = set(range(1, n + 1))

    while True:
        guess_str = input(
            "Нужное число есть среди вот этих чисел (или введите 'Помогите!'): "
        ).strip()
        if guess_str.lower() == "помогите!":
            print(
                f"Иван мог загадать следующие числа: {' '.join(map(str, sorted(list(possible_numbers))))}"
            )
            break

        try:
            guess_set = set(map(int, guess_str.split()))
            if not guess_set:
                print("Введите хотя бы одно число.")
                continue
        except ValueError:
            print(
                "Пожалуйста, введите числа, разделенные пробелом, или 'Помогите!'."
            )
            continue

        while True:
            response = input("Ответ Ивана ('Да' или 'Нет'): ").strip().lower()
            if response in ["да", "нет"]:
                break
            else:
                print("Неверный ответ. Пожалуйста, введите 'Да' или 'Нет'.")

        if response == "да":
            possible_numbers &= guess_set
        else:
            possible_numbers -= guess_set

        if not possible_numbers:
            print("Что-то пошло не так, возможные числа закончились!")
            break
        if len(possible_numbers) == 1:
            print(f"Иван загадал число: {list(possible_numbers)[0]}")
            break


def genealogy_tree():
    """
    Calculates the "height" of individuals in a genealogy tree.

    The user inputs the number of people and then pairs of child-parent
    relationships. The program then calculates and prints the height of each
    person in the tree, where height is defined as the distance from the
     furthest ancestor (root of their part of the tree).
    Handles cases of cycles or missing parents in the input data.
    """
    while True:
        try:
            n = int(input("Введите количество человек: "))
            if n > 1:  # Need at least 2 people for a pair
                break
            else:
                print("Количество человек должно быть больше 1.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    tree = {}
    heights = {}
    all_people = set()

    for i in range(n - 1):
        while True:
            pair_str = input(f"{i + 1} пара (ребенок родитель): ").split()
            if len(pair_str) == 2:
                child, parent = pair_str[0], pair_str[1]
                if child == parent:
                    print(
                        "Ребенок и родитель не могут быть одним и тем же лицом."
                    )
                    continue
                tree[child] = parent
                all_people.add(child)
                all_people.add(parent)
                break
            else:
                print("Введите два имени через пробел (ребенок родитель).")


    def compute_height(person):
        """
        Recursively computes the height of a person in the genealogy tree.

        Args:
            person (str): The name of the person.

        Returns:
            int: The height of the person in the tree.
                 0 for a root (no parent in the provided data).

        Raises:
            ValueError: If a cycle is detected in the parent chain.
        """
        if person not in heights:
            if person not in tree:  # This person is a root
                heights[person] = 0
            else:
                # Prevent infinite recursion on cycles if any (though input validation should minimize this)
                if tree[person] in heights and heights[
                        tree[person]] == -1:  # Cycle detected
                    raise ValueError(
                        f"Обнаружен цикл с участием {person} и {tree[person]}")
                heights[person] = -1  # Mark as visiting
                heights[person] = compute_height(tree[person]) + 1
        return heights[person]


    sorted_people = sorted(list(all_people))

    final_heights = {}
    for person in sorted_people:
        try:
            final_heights[person] = compute_height(person)
        except ValueError as e:
            print(e)
            final_heights[person] = "Ошибка (цикл)"
        except KeyError as e:
            print(
                f"Ошибка: Родитель для {e} не найден. Проверьте структуру дерева."
            )
            final_heights[person] = "Ошибка (нет родителя)"

    for person in sorted_people:
        if isinstance(final_heights.get(person), int):
            print(f"{person} {final_heights[person]}")
        elif final_heights.get(person):
            print(f"{person} {final_heights[person]}")


def translation_test():
    """
    Tests the user's knowledge of Russian-to-English word translations.

    Reads word pairs from "russian.txt" and "english.txt".
    It then prompts the user to translate Russian words and provides feedback,
    finally giving a score based on the number of correct answers.
    Handles file errors and mismatches in word counts between the files.
    """
    try:
        with open("russian.txt", "r", encoding="utf-8") as rus_file, open(
                "english.txt", "r", encoding="utf-8") as eng_file:
            rus_words = [
                line.strip() for line in rus_file.readlines() if line.strip()
            ]
            eng_words = [
                line.strip() for line in eng_file.readlines() if line.strip()
            ]
    except FileNotFoundError:
        print(
            "Ошибка: Один или оба файла словарей не найдены (russian.txt, english.txt)."
        )
        return

    if not rus_words or not eng_words:
        print("Один из файлов словаря пуст. Тест не может быть проведен.")
        return

    if len(rus_words) != len(eng_words):
        print("Количество слов в словарях не совпадает. Проверьте файлы.")
        return

    correct_answers = 0
    total_questions = len(rus_words)

    for rus, eng in zip(rus_words, eng_words):
        user_translation = input(f"Переведите слово '{rus}': ").strip()
        if not user_translation:
            print("Вы не ввели перевод.")
            # Decide if this counts as wrong or allow retry - current is like wrong
        if user_translation.lower() == eng.lower():
            print("Верно")
            correct_answers += 1
        else:
            print(f"Неверно. Правильный перевод: {eng}")

    print(f"Оценка: {correct_answers}/{total_questions}")


def main():
    """
    Presents a menu to the user to choose and run one of the available programs.
    """
    print("Выберите задание:")
    print("1 - Поиск городов по странам")
    print("2 - Учет заказов пиццы")
    print("3 - Угадайка")
    print("4 - Генеалогическое древо")
    print("5 - Проверка переводов")

    while True:
        try:
            choice_str = input("Введите номер задания: ")
            choice = int(choice_str)
            if 1 <= choice <= 5:
                break
            else:
                print("Неверный выбор. Введите число от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите номер задания (число).")

    if choice == 1:
        locate_cities()
    elif choice == 2:
        pizza_orders()
    elif choice == 3:
        guess_the_number()
    elif choice == 4:
        genealogy_tree()
    elif choice == 5:
        translation_test()


if __name__ == "__main__":
    main()
