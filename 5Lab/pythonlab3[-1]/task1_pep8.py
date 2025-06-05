def input_countries_data():
    """Inputs and stores data about countries and their cities."""
    countries_map = {}
    while True:
        try:
            k = int(input("Кол-во стран: "))
            if k >= 0:
                break
            else:
                print("Количество стран не может быть отрицательным.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    if k == 0:
        print("Количество стран равно 0, ввод данных о странах пропускается.")
        return countries_map

    print("Введите данные по странам (формат: Страна Город1 Город2 ...):")
    for i in range(k):
        while True:
            entry_str = input(f"{i + 1} страна: ").strip()
            if not entry_str:
                print("Ввод не может быть пустым. Пожалуйста, введите данные.")
                continue

            data = entry_str.split()
            if len(data) < 2:
                print("Некорректный ввод. "
                      "Требуется название страны и хотя бы один город.")
                continue

            country = data[0]
            cities = data[1:]
            # Ensure no city is an empty string if multiple spaces were used
            valid_cities = [city for city in cities if city]
            if not valid_cities:
                print("Не указаны города для страны.")
                continue

            # If country already exists, this will overwrite.
            # To add cities to existing country, logic would need to change.
            # For this task, assuming each country entry is unique or overwriting is fine.
            countries_map[country] = valid_cities
            break
    return countries_map


def find_country_for_city(city, countries_map):
    """Finds the country for a given city from the countries_map."""
    for country, cities_in_country in countries_map.items():
        if city in cities_in_country:
            return country
    return None


def query_cities(countries_map):
    """Inputs three city names and prints their country information."""
    if not countries_map:
        print("\nНет данных о странах для поиска городов.")
        return

    print("\nВведите 3 города для поиска их стран:")
    for i in range(3):
        while True:
            city_name = input(f"{i + 1} город: ").strip()
            if city_name:
                break
            else:
                print("Название города не может быть пустым.")

        country = find_country_for_city(city_name, countries_map)
        if country:
            print(f"Город {city_name} расположен в стране {country}.")
        else:
            print(f"По городу {city_name} данных нет.")


def main():
    """Main function to run the country and city management task."""
    print("--- Управление данными о городах и странах ---")
    countries_data = input_countries_data()
    query_cities(countries_data)


if __name__ == "__main__":
    main()
