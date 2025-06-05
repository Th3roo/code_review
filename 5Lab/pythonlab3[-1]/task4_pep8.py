def get_number_of_people():
    """Gets a positive integer for the number of people."""
    while True:
        try:
            n_val = int(input("Введите количество человек: "))
            if n_val > 0:
                return n_val
            else:
                print("Количество человек должно быть положительным.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def input_relationships(num_people):
    """Inputs parent-descendant relationships."""
    # relationships map: parent -> [list of children]
    relationships = {}
    all_people = set()
    children_set = set()  # People who are listed as descendants

    if num_people == 1:
        # Special case: if only one person, they are the root with height 0.
        # No relationships to input.
        name = input("Введите имя единственного человека: ").strip()
        if not name:
            print("Имя не может быть пустым.")
            return None, None, None  # Indicate error or incomplete input
        all_people.add(name)
        return relationships, all_people, children_set

    print("Введите N-1 пару связей (формат: имя_потомка имя_родителя):")
    # We expect num_people - 1 relationships for a tree
    expected_relations_count = num_people - 1
    actual_relations_count = 0

    # Loop to ensure correct number of valid relationships are entered
    # This is a simplified loop; a more robust version might count attempts or handle errors more gracefully.
    for i in range(expected_relations_count):
        while True:
            entry_str = input(f"Пара {i + 1}: ").strip()
            if not entry_str:
                print("Ввод не может быть пустым.")
                continue

            parts = entry_str.split()
            if len(parts) != 2:
                print(
                    "Некорректный формат. Ожидается: имя_потомка имя_родителя (два слова)."
                )
                continue

            descendant, parent = parts[0], parts[1]

            if descendant == parent:
                print(
                    f"Ошибка: человек ({descendant}) не может быть своим же родителем."
                )
                continue

            # Check if descendant is already a child of another parent (optional, depends on interpretation)
            # For a strict tree, a child has one parent. Here, we build parent->children.
            # If a descendant is listed under multiple parents, it's more of a graph.
            # The problem structure implies a tree, so `children_set` will help find roots.

            if parent not in relationships:
                relationships[parent] = []

            # Avoid adding the same child multiple times to the same parent (though set conversion later would handle it for `all_people`)
            if descendant not in relationships[parent]:
                relationships[parent].append(descendant)

            all_people.add(parent)
            all_people.add(descendant)
            children_set.add(descendant)
            actual_relations_count += 1
            break  # Valid pair processed

    if actual_relations_count != expected_relations_count and num_people > 1:
        print(
            f"Предупреждение: Введено {actual_relations_count} связей, ожидалось {expected_relations_count}."
        )
        # Potentially an issue for forming a single tree.

    return relationships, all_people, children_set


def find_roots(all_people, children_set):
    """Finds potential roots (people who are not children)."""
    if not all_people:
        return []
    potential_roots = list(all_people - children_set)
    return potential_roots


def calculate_node_heights_recursive(tree_adj, node, heights_map, current_h,
                                     visited_path):
    """
    Recursively calculates heights of all descendants.
    tree_adj: Adjacency list (parent -> [children]).
    node: Current node to process.
    heights_map: Dictionary to store heights.
    current_h: Current height for 'node'.
    visited_path: Set to detect cycles during current recursion path.
    """
    if node in visited_path:
        # Cycle detected
        raise ValueError(
            f"Обнаружен цикл, включающий {node}. Невозможно рассчитать высоты."
        )

    heights_map[node] = current_h
    visited_path.add(node)

    for child in tree_adj.get(node, []):
        calculate_node_heights_recursive(tree_adj, child, heights_map,
                                         current_h + 1, visited_path)

    visited_path.remove(
        node
    )  # Backtrack: remove node from path after visiting all its children


def manage_genealogy_tree():
    """Main function to manage genealogy tree height calculation."""
    num_people = get_number_of_people()

    if num_people == 1:
        # Handled by input_relationships, but let's assume it returns valid data for a single person
        name = ""  # Placeholder, actual name handling is inside input_relationships
        # Re-prompt if input_relationships indicated an error (e.g. returned None for name)
        while not name:
            name = input("Введите имя единственного человека: ").strip()
            if not name: print("Имя не может быть пустым.")
        print("\n“Высота” каждого члена семьи:")
        print(f"{name} 0")
        return

    relationships, all_people_set, children_ident_set = input_relationships(
        num_people)

    if relationships is None:  # Indicates an issue during input like empty name for N=1
        print("Не удалось получить данные о связях.")
        return

    if not all_people_set and num_people > 1:
        print("Нет данных о людях для построения дерева.")
        return

    potential_roots = find_roots(all_people_set, children_ident_set)

    if not potential_roots:
        if all_people_set:  # People exist but no one is without a parent
            print(
                "Ошибка: В структуре нет явного родоначальника (возможно, цикл)."
            )
        else:  # No people were defined (e.g. N > 1 but all inputs were invalid)
            print("Ошибка: Нет людей в дереве.")
        return

    if len(potential_roots) > 1:
        print(
            f"Ошибка: Обнаружено несколько ({len(potential_roots)}) возможных родоначальников: {', '.join(sorted(potential_roots))}."
        )
        print("Для простой иерархии ожидается один родоначальник.")
        # Could pick one, or ask user, or terminate. For now, terminate.
        return

    root_node = potential_roots[0]
    calculated_heights = {}

    try:
        calculate_node_heights_recursive(relationships, root_node,
                                         calculated_heights, 0, set())
    except ValueError as e:  # Cycle detected
        print(f"Ошибка при расчете высот: {e}")
        return
    except RecursionError:
        print(
            "Ошибка: Превышена глубина рекурсии. Возможно, очень глубокое дерево или неперехваченный цикл."
        )
        return

    print("\n“Высота” каждого члена семьи:")
    # Ensure all people involved are printed, even if somehow missed by recursion (should not happen in a connected tree)
    # For people not reachable from the root, height won't be in calculated_heights.
    # The problem implies a single connected tree.
    for person in sorted(list(all_people_set)):
        height = calculated_heights.get(
            person, "Неизвестно (не достигнут от корня или ошибка)")
        print(f"{person} {height}")


def main():
    print("--- Расчет высот в генеалогическом древе ---")
    manage_genealogy_tree()


if __name__ == "__main__":
    main()
