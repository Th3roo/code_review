# Задача 1: Страны и города

def task_1_countries_and_cities():
    """
    Решение задачи 1: Страны и города.
    С клавиатуры вводится количество стран К. Затем вводится К
    строк, в каждой из которых указывается название страны и список
    городов в этой стране через пробел. Затем пользователь вводит 3
    названия городов, после чего программа сообщает, в какой стране они
    находятся. Если такого города нет, то вывести соответствующее
    сообщение.
    """
    try:
        k = int(input("Кол-во стран: "))
        if k < 0:
            print("Количество стран не может быть отрицательным.")
            return
    except ValueError:
        print("Некорректный ввод для количества стран.")
        return

    country_city_map = {}
    print("Введите данные по странам (формат: Страна Город1 Город2 ...):")
    for i in range(k):
        try:
            line = input(f"{i + 1} страна: ").split()
            if not line or len(line) < 2:
                print(f"Некорректный ввод для страны {i+1}. "
                      "Ожидается название страны и хотя бы один город.")
                continue  # Пропускаем эту страну
            country = line[0]
            cities = line[1:]
            for city in cities:
                country_city_map[city] = country
        except Exception as e:
            print(f"Ошибка при вводе данных для страны {i+1}: {e}")
            # Пропускаем эту страну, чтобы не прерывать весь ввод

    print("\nВведите 3 города для поиска:")
    for i in range(3):
        city_to_find = input(f"{i + 1} город: ")
        if city_to_find in country_city_map:
            print(f"Город {city_to_find} расположен в стране "
                  f"{country_city_map[city_to_find]}.")
        else:
            print(f"По городу {city_to_find} данных нет.")

if __name__ == '__main__':
    print("--- Задача 1: Страны и города ---")
    task_1_countries_and_cities()