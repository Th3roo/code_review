# Recursive function to determine the height of a person with memoization
def get_height_recursive(person, parent_map, heights_cache):
    if person not in heights_cache:
        if person not in parent_map:  # This person is a root
            heights_cache[person] = 0
        else:
            parent = parent_map[person]
            # Check for simple cycle before recursion to prevent RecursionError
            # This is a basic check; more complex cycle detection might be needed for arbitrary graphs
            if parent in heights_cache and heights_cache[
                    parent] == -1:  # -1 indicates "currently visiting"
                raise ValueError(
                    f"Обнаружен цикл, включающий {person} и {parent}")
            heights_cache[person] = -1  # Mark as visiting
            heights_cache[person] = get_height_recursive(
                parent, parent_map, heights_cache) + 1
    elif heights_cache[
            person] == -1:  # Should be caught by the check above, but as a safeguard
        raise ValueError(
            f"Обнаружен цикл при попытке получить высоту для {person}")
    return heights_cache[person]


def task_4_family_tree_heights():
    while True:
        try:
            n_people = int(input("Введите количество человек: "))
            if n_people > 0:
                break
            else:  # n_people == 0 or n_people < 0
                print(
                    "Количество человек должно быть положительным целым числом."
                )
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    parent_map = {}
    all_people = set()

    if n_people == 1:
        while True:
            name_of_single_person = input(
                "Введите имя единственного человека (родоначальника): ").strip(
                )
            if name_of_single_person:
                break
            else:
                print("Имя не может быть пустым.")
        print("\n“Высота” каждого члена семьи:")
        print(f"{name_of_single_person} 0")
        return

    print("Введите N-1 пару связей (формат: имя_потомка имя_родителя):")
    # Ensure we collect exactly n_people - 1 valid pairs
    collected_pairs = 0
    attempted_pairs = 0
    max_attempts = (n_people -
                    1) * 2  # Allow some leeway for errors but not infinite

    while collected_pairs < n_people - 1 and attempted_pairs < max_attempts:
        attempted_pairs += 1
        pair_input_str = input(f"Пара {collected_pairs + 1}: ").strip()
        if not pair_input_str:
            print("Ввод не может быть пустым.")
            continue

        pair_input = pair_input_str.split()
        if len(pair_input) != 2:
            print(
                f"Некорректный ввод для пары {collected_pairs + 1}. "
                "Ожидается: имя_потомка имя_родителя (два слова через пробел)."
            )
            continue
        child, parent = pair_input[0], pair_input[1]

        if child == parent:
            print(
                f"Ошибка в паре {collected_pairs + 1}: человек не может быть родителем сам себе ({child})."
            )
            continue
        if child in parent_map:
            print(
                f"Ошибка: у потомка {child} уже указан родитель {parent_map[child]}. "
                f"Повторная связь ({child} {parent}) не будет добавлена.")
            # Not necessarily an error that stops collection, but this specific pair is skipped.
            # If we need exactly N-1 unique child-parent links, this logic might need adjustment
            # or we assume the user provides N-1 *valid* and *unique child* links.
            # For now, we just skip this redundant/conflicting pair.
            continue

        parent_map[child] = parent
        all_people.add(child)
        all_people.add(parent)
        collected_pairs += 1

    if collected_pairs < n_people - 1:
        print(
            f"Было введено только {collected_pairs} корректных пар из необходимых {n_people -1}. Расчет высот может быть неполным или неверным."
        )
        # Decide if to proceed or return
        if not parent_map and n_people > 1:  # No valid pairs at all
            print("Не удалось установить ни одной связи. Завершение.")
            return

    # Determine roots (people who are not children in any pair)
    # This also implies they must be in all_people if they are part of any relationship
    children_with_parents = set(parent_map.keys())

    # Potential roots are those in all_people but not in children_with_parents
    # If a person was only mentioned as a parent, they are a root.
    # If n_people = 1, all_people contains that one person, children_with_parents is empty.
    roots = all_people - children_with_parents

    if not all_people and n_people > 1:  # Should be caught by collected_pairs check earlier
        print("Нет данных о людях для построения дерева.")
        return

    if not roots and all_people:  # No person is without a recorded parent, implies a cycle or incomplete data
        print("Ошибка в структуре дерева: нет явного родоначальника. "
              "Это может указывать на цикл во всех введенных связях.")
        return

    # The problem implies a single connected tree, so there should be one root.
    # However, the input N-1 pairs might not guarantee this if user input is arbitrary.
    # For now, we proceed if there's at least one root and calculate heights.
    # A strict interpretation might require exactly one root.

    heights = {}
    calculation_errors = False
    sorted_all_people = sorted(list(all_people))

    for person in sorted_all_people:
        try:
            # Ensure all potential roots are initialized if not in parent_map
            if person in roots and person not in heights:
                heights[
                    person] = 0  # Explicitly set root height before potential recursion

            get_height_recursive(person, parent_map, heights)
        except ValueError as e:  # Catches cycles from get_height_recursive
            print(f"Ошибка при расчете высоты для {person}: {e}")
            heights[person] = "Ошибка (цикл)"  # Mark as error
            calculation_errors = True
        except RecursionError:
            print(
                f"Ошибка: Превышена глубина рекурсии при расчете для {person}. Возможно, очень глубокое дерево или неперехваченный цикл."
            )
            heights[person] = "Ошибка (рекурсия)"
            calculation_errors = True

    if not heights and all_people and not calculation_errors:
        print(
            "Не удалось рассчитать высоты для людей (возможно, из-за структуры данных)."
        )
        return

    if not all_people and n_people > 1:  # Should have been caught earlier
        print("Нет данных о людях для вывода высот.")
        return

    print("\n“Высота” каждого члена семьи:")
    for person_name in sorted_all_people:  # Iterate over all known people
        height_val = heights.get(person_name)
        if height_val is not None:
            print(f"{person_name} {height_val}")
        else:
            # This case might happen if a person was in all_people but never processed
            # due to not being a key in parent_map and not being a detected root (e.g. isolated person)
            # or if get_height_recursive was not called for them for some reason.
            # For a valid tree from N-1 pairs for N people, all should be covered.
            print(
                f"{person_name} (высота не рассчитана, возможно изолирован или ошибка структуры)"
            )


if __name__ == '__main__':
    print("--- Задача 4: Высоты в генеалогическом древе ---")
    task_4_family_tree_heights()
