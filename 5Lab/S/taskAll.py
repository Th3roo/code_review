# Задание 1
def locate_cities():
    k = int(input("Кол-во стран: "))
    country_data = {}

    for i in range(k):
        entry = input(f"{i + 1} страна: ").split()
        country = entry[0]
        cities = entry[1:]
        for city in cities:
            country_data[city] = country

    for i in range(3):
        city = input(f"{i + 1} город: ")
        if city in country_data:
            print(f"Город {city} расположен в стране {country_data[city]}.")
        else:
            print(f"По городу {city} данных нет.")

# Задание 2
def pizza_orders():
    n = int(input("Введите кол-во заказов: "))
    orders = {}

    for i in range(n):
        entry = input(f"{i + 1} заказ: ").split(' ', 2)
        buyer, pizza, amount = entry[0], entry[1], int(entry[2])
        if buyer not in orders:
            orders[buyer] = {}
        if pizza in orders[buyer]:
            orders[buyer][pizza] += amount
        else:
            orders[buyer][pizza] = amount

    for buyer in sorted(orders):
        print(f"{buyer}:")
        for pizza, amount in orders[buyer].items():
            print(f"  {pizza}: {amount}")

# Задание 3
def guess_the_number():
    n = int(input("Введите максимальное число: "))
    possible_numbers = set(range(1, n + 1))

    while True:
        guess = input("Нужное число есть среди вот этих чисел: ")
        if guess == "Помогите!":
            print(f"Иван мог загадать следующие числа: {' '.join(map(str, sorted(possible_numbers)))}")
            break
        guess_set = set(map(int, guess.split()))
        response = input("Ответ Ивана: ")
        if response == "Да":
            possible_numbers &= guess_set
        else:
            possible_numbers -= guess_set

# Задание 4
def genealogy_tree():
    n = int(input("Введите количество человек: "))
    tree = {}
    heights = {}

    for i in range(n - 1):
        child, parent = input(f"{i + 1} пара: ").split()
        tree[child] = parent

    def compute_height(person):
        if person not in heights:
            heights[person] = compute_height(tree[person]) + 1 if person in tree else 0
        return heights[person]

    people = set(tree.keys()).union(tree.values())
    for person in sorted(people):
        compute_height(person)
        print(f"{person} {heights[person]}")

# Задание 5
def translation_test():
    with open("russian.txt", "r", encoding="utf-8") as rus_file, open("english.txt", "r", encoding="utf-8") as eng_file:
        rus_words = rus_file.readlines()
        eng_words = eng_file.readlines()

    correct_answers = 0
    for rus, eng in zip(rus_words, eng_words):
        rus, eng = rus.strip(), eng.strip()
        user_translation = input(f"Переведите слово '{rus}': ")
        if user_translation.lower() == eng.lower():
            print("Верно")
            correct_answers += 1
        else:
            print(f"Неверно. Правильный перевод: {eng}")

    total = len(rus_words)
    print(f"Оценка: {correct_answers}/{total}")

# Основная функция
def main():
    print("Выберите задание:")
    print("1 - Поиск городов по странам")
    print("2 - Учет заказов пиццы")
    print("3 - Угадайка")
    print("4 - Генеалогическое древо")
    print("5 - Проверка переводов")

    choice = int(input("Введите номер задания: "))
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
    else:
        print("Неверный выбор.")

# Запуск программы
if __name__ == "__main__":
    main()
