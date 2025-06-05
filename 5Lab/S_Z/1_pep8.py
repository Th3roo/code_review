def task_1_countries_and_cities():
    while True:
        try:
            k = int(input("Кол-во стран: "))
            if k > 0:
                break
            elif k == 0:
                print("Количество стран равно 0, данные вводить не требуется.")
                return
            else:
                print("Количество стран не может быть отрицательным.")
        except ValueError:
            print(
                "Некорректный ввод. Пожалуйста, введите целое число для количества стран."
            )

    country_city_map = {}
    print("Введите данные по странам (формат: Страна Город1 Город2 ...):")
    for i in range(k):
        while True:
            line_input = input(f"{i + 1} страна: ").strip()
            if not line_input:
                print("Ввод не может быть пустым.")
                continue
            line = line_input.split()
            if len(line) < 2:
                print(f"Некорректный ввод для страны {i + 1}. "
                      "Ожидается название страны и хотя бы один город.")
                continue
            country = line[0]
            cities = line[1:]
            # Дополнительная проверка, что города не пустые строки (если они были введены с множественными пробелами)
            valid_cities = [city for city in cities if city]
            if not valid_cities:
                print(f"Некорректный ввод для страны {i + 1}. "
                      "Не указаны города.")
                continue
            for city in valid_cities:
                country_city_map[city] = country
            break

    if k > 0:  # Только если были введены страны, запрашиваем города для поиска
        print("\nВведите 3 города для поиска:")
        for i in range(3):
            while True:
                city_to_find = input(f"{i + 1} город: ").strip()
                if city_to_find:
                    break
                else:
                    print("Название города не может быть пустым.")

            if city_to_find in country_city_map:
                print(f"Город {city_to_find} расположен в стране "
                      f"{country_city_map[city_to_find]}.")
            else:
                print(f"По городу {city_to_find} данных нет.")


if __name__ == '__main__':
    print("--- Задача 1: Страны и города ---"
          )  # Оставим для ясности запуска конкретного файла
    task_1_countries_and_cities()
