"""
Manages a database of countries and cities.

This script allows a user to input data about countries and the cities
located within them. It then allows the user to query for specific cities
to find out which country they belong to.
"""


def input_countries_data():
    """
    Inputs and stores data about countries and their cities.

    Prompts the user for the number of countries and then for each country,
    its name and a list of its cities. Handles input validation for the
    number of countries and for each country's data.

    Returns:
        dict: A dictionary where keys are country names (str) and values are
              lists of city names (list of str) belonging to that country.
              Returns an empty dictionary if 0 countries are entered.
    """
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
            valid_cities = [city for city in cities if city]
            if not valid_cities:
                print("Не указаны города для страны.")
                continue

            countries_map[country] = valid_cities
            break
    return countries_map


def find_country_for_city(city, countries_map):
    """
    Finds the country for a given city from the countries_map.

    Args:
        city (str): The name of the city to find.
        countries_map (dict): A dictionary where keys are country names (str)
                              and values are lists of city names (list of str).

    Returns:
        str or None: The name of the country if the city is found,
                     otherwise None.
    """
    for country, cities_in_country in countries_map.items():
        if city in cities_in_country:
            return country
    return None


def query_cities(countries_map):
    """
    Inputs three city names from the user and prints their country information.

    If the `countries_map` is empty, it informs the user that no data is
    available. Otherwise, it prompts for three city names and uses
    `find_country_for_city` to determine and print their respective countries
    or indicate if a city is not found.

    Args:
        countries_map (dict): A dictionary containing countries and their cities,
                              as returned by `input_countries_data`.
    """
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
