# Задача 4: Высоты в генеалогическом древе

def get_height_recursive(person, parent_map, heights_cache):
    """
    Рекурсивная функция для определения высоты элемента дерева с кешированием.
    """
    if person not in heights_cache:
        if person not in parent_map:  # Это корень (нет родителя в карте)
            heights_cache[person] = 0
        else:
            parent = parent_map[person]
            # Рекурсивный вызов для родителя
            heights_cache[person] = get_height_recursive(
                parent, parent_map, heights_cache
            ) + 1
    return heights_cache[person]

def task_4_family_tree_heights():
    """
    Решение задачи 4: Высоты в генеалогическом древе.
    Программа получает количество человек N и N-1 пару "потомок родитель".
    Выводит список всех элементов древа в лексикографическом порядке
    с указанием их высоты. Родоначальник имеет высоту 0.
    """
    try:
        n_people = int(input("Введите количество человек: "))
        if n_people <= 0:
            print("Количество человек должно быть положительным.")
            return
    except ValueError:
        print("Некорректный ввод для количества человек.")
        return

    parent_map = {}
    all_people = set()

    if n_people == 1:
        name_of_single_person = input(
            "Введите имя единственного человека (родоначальника): "
        ).strip()
        if name_of_single_person:
            print("\n“Высота” каждого члена семьи:")
            print(f"{name_of_single_person} 0")
        else:
            print("Имя единственного человека не было введено.")
        return

    print("Введите N-1 пару связей (формат: имя_потомка имя_родителя):")
    for i in range(n_people - 1):
        try:
            pair_input = input(f"{i + 1} пара: ").split()
            if len(pair_input) != 2:
                print(f"Некорректный ввод для пары {i+1}. "
                      "Ожидается: имя_потомка имя_родителя.")
                continue
            child, parent = pair_input[0], pair_input[1]
            if child == parent:
                print(f"Ошибка в паре {i+1}: человек не может быть родителем сам себе ({child}).")
                continue
            if child in parent_map:
                print(f"Ошибка: у потомка {child} уже указан родитель {parent_map[child]}. "
                      f"Новая попытка указать родителя: {parent}. Используем первого.")
                continue

            parent_map[child] = parent
            all_people.add(child)
            all_people.add(parent)
        except Exception as e:
            print(f"Непредвиденная ошибка при вводе пары {i+1}: {e}")

    if not all_people and n_people > 1:
        print("Не было введено корректных данных о связях, "
              "невозможно построить дерево.")
        return
    if not parent_map and n_people > 1 : # Если нет связей, но людей > 1 (все пары некорректны)
        print("Не удалось установить ни одной связи между людьми.")
        return


    children_with_parents = set(parent_map.keys())
    roots = all_people - children_with_parents

    if not roots and all_people:
        print("Ошибка в структуре дерева: нет явного родоначальника "
              "(возможно, все являются чьими-то потомками, образуя цикл, "
              "или все N-1 связей были некорректны).")
        return
    if len(roots) > 1 and n_people > 1: # Для n_people=1 roots может быть пустым, если имя не ввели
        print(f"Ошибка в структуре дерева: найдено несколько "
              f"родоначальников: {', '.join(sorted(list(roots)))}. "
              "Ожидается один.")
        return

    heights = {}
    for person in sorted(list(all_people)): # Сортируем для консистентности
        get_height_recursive(person, parent_map, heights)

    if not heights and all_people:
        print("Не удалось рассчитать высоты для людей.")
        return
    if not all_people and n_people > 1: # Если после ввода пар множество людей пусто
        print("Нет данных о людях для расчета высот.")
        return


    print("\n“Высота” каждого члена семьи:")
    # Выводим в лексикографическом порядке имен
    for person_name in sorted(heights.keys()):
        print(f"{person_name} {heights[person_name]}")

if __name__ == '__main__':
    print("--- Задача 4: Высоты в генеалогическом древе ---")
    task_4_family_tree_heights()