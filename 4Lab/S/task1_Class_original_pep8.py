"""
This module defines Parent and Child classes, along with functions
to create and interact with them through a menu-driven interface.
"""

class Parent:
    """
    Represents a parent with a name, age, and a list of children.
    """
    def __init__(self, name: str, age: int):
        """
        Initializes a Parent object.

        Args:
            name: The name of the parent.
            age: The age of the parent.

        Raises:
            TypeError: If name is not a string or age is not an integer.
            ValueError: If age is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Parent name must be a string.")
        if not isinstance(age, int):
            raise TypeError("Parent age must be an integer.")
        if age < 0:
            raise ValueError("Parent age cannot be negative.")
        
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        """
        Adds a child to the parent's list of children.

        Args:
            child: An instance of the Child class.

        Raises:
            TypeError: If child is not an instance of Child.
        """
        if not isinstance(child, Child):
            raise TypeError("Child must be an instance of the Child class.")
        self.children.append(child)

    def get_info(self) -> str:
        """
        Returns a string with information about the parent.
        """
        return (f"Родитель: {self.name}, Возраст: {self.age}, "
                f"Количество детей: {len(self.children)}")

    def calm_child(self, child_index: int):
        """
        Calms a specific child.

        Args:
            child_index: The index of the child in the children list.
        
        Raises:
            IndexError: If child_index is out of bounds.
        """
        if not 0 <= child_index < len(self.children):
            raise IndexError("Некорректный номер ребёнка.")
        self.children[child_index].calm()
        print(f"{self.children[child_index].name} успокоен.")

    def feed_child(self, child_index: int):
        """
        Feeds a specific child.

        Args:
            child_index: The index of the child in the children list.

        Raises:
            IndexError: If child_index is out of bounds.
        """
        if not 0 <= child_index < len(self.children):
            raise IndexError("Некорректный номер ребёнка.")
        self.children[child_index].feed()
        print(f"{self.children[child_index].name} накормлен.")


class Child:
    """
    Represents a child with a name, age, and states of calmness and hunger.
    """
    def __init__(self, name: str, age: int):
        """
        Initializes a Child object.

        Args:
            name: The name of the child.
            age: The age of the child.

        Raises:
            TypeError: If name is not a string or age is not an integer.
            ValueError: If age is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Child name must be a string.")
        if not isinstance(age, int):
            raise TypeError("Child age must be an integer.")
        if age < 0:
            raise ValueError("Child age cannot be negative.")

        self.name = name
        self.age = age
        self.is_calm = False
        self.is_hungry = True

    def calm(self):
        """Sets the child's state to calm."""
        self.is_calm = True

    def feed(self):
        """Sets the child's state to not hungry."""
        self.is_hungry = False

    def get_info(self) -> str:
        """
        Returns a string with information about the child.
        """
        calm_state = "спокоен" if self.is_calm else "беспокоен"
        hunger_state = "голоден" if self.is_hungry else "сыт"
        return (f"Ребёнок: {self.name}, Возраст: {self.age}, "
                f"Состояние: {calm_state}, Голод: {hunger_state}")


def create_parents() -> list[Parent]:
    """
    Prompts the user to create a list of parents and their children.

    Returns:
        A list of Parent objects.
    """
    parents = []
    while True:
        try:
            num_parents_str = input("Введите количество родителей: ")
            num_parents = int(num_parents_str)
            if num_parents <= 0:
                print("Количество родителей должно быть положительным числом.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    for i in range(num_parents):
        while True:
            name = input(f"Введите имя родителя {i + 1}: ").strip()
            if name:
                break
            print("Имя родителя не может быть пустым.")
        
        while True:
            try:
                age_str = input(f"Введите возраст родителя {i + 1}: ")
                age = int(age_str)
                parent = Parent(name, age)  # Validation done in Parent constructor
                break
            except (ValueError, TypeError) as e:
                print(f"Ошибка: {e}. Пожалуйста, введите корректный возраст.")
        
        while True:
            try:
                num_children_str = input(
                    f"Введите количество детей у родителя {name}: "
                )
                num_children = int(num_children_str)
                if num_children < 0:
                    print("Количество детей не может быть отрицательным.")
                    continue
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

        for j in range(num_children):
            while True:
                child_name = input(
                    f"Введите имя ребёнка {j + 1} родителя {name}: "
                ).strip()
                if child_name:
                    break
                print("Имя ребёнка не может быть пустым.")

            while True:
                try:
                    child_age_str = input(
                        f"Введите возраст ребёнка {child_name}: "
                    )
                    child_age = int(child_age_str)
                    # Validation for child_age (e.g. child_age < parent.age)
                    # can be added here if needed.
                    child = Child(child_name, child_age) # Validation in Child
                    parent.add_child(child)
                    break
                except (ValueError, TypeError) as e:
                    print(f"Ошибка: {e}. Пожалуйста, введите корректный возраст.")
        parents.append(parent)
    return parents


def show_menu(parents_list: list[Parent]):
    """
    Displays a menu to interact with the list of parents and children.

    Args:
        parents_list: A list of Parent objects.
    
    Raises:
        TypeError: If parents_list is not a list of Parent objects.
    """
    if not isinstance(parents_list, list) or \
       not all(isinstance(p, Parent) for p in parents_list):
        raise TypeError("show_menu expects a list of Parent objects.")

    if not parents_list:
        print("Список родителей пуст. Нечего отображать.")
        return

    while True:
        print("\nМеню:")
        print("1. Сообщить информацию о родителе")
        print("2. Сообщить информацию о всех детях родителя")
        print("3. Выполнить действие с ребенком")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            try:
                parent_idx_str = input("Введите номер родителя: ")
                parent_idx = int(parent_idx_str) - 1
                if 0 <= parent_idx < len(parents_list):
                    print(parents_list[parent_idx].get_info())
                else:
                    print("Некорректный номер родителя.")
            except ValueError:
                print("Некорректный ввод. Введите номер.")
        
        elif choice == '2':
            try:
                parent_idx_str = input("Введите номер родителя: ")
                parent_idx = int(parent_idx_str) - 1
                if 0 <= parent_idx < len(parents_list):
                    if not parents_list[parent_idx].children:
                        print(f"У родителя {parents_list[parent_idx].name} нет детей.")
                    else:
                        for i, child_obj in enumerate(
                            parents_list[parent_idx].children, start=1
                        ):
                            print(f"{i}. {child_obj.get_info()}")
                else:
                    print("Некорректный номер родителя.")
            except ValueError:
                print("Некорректный ввод. Введите номер.")

        elif choice == '3':
            try:
                parent_idx_str = input("Введите номер родителя: ")
                parent_idx = int(parent_idx_str) - 1
                if not 0 <= parent_idx < len(parents_list):
                    print("Некорректный номер родителя.")
                    continue

                if not parents_list[parent_idx].children:
                    print(f"У родителя {parents_list[parent_idx].name} нет детей, "
                          "невозможно выполнить действие.")
                    continue

                child_idx_str = input("Введите номер ребёнка: ")
                child_idx = int(child_idx_str) - 1
                
                action = input(
                    "Введите действие (успокоить/накормить): "
                ).strip().lower()

                if action == "успокоить":
                    parents_list[parent_idx].calm_child(child_idx)
                elif action == "накормить":
                    parents_list[parent_idx].feed_child(child_idx)
                else:
                    print("Некорректное действие.")
            except ValueError:
                print("Некорректный ввод. Введите номер.")
            except IndexError as e: # Catching specific error from methods
                print(f"Ошибка: {e}")
        
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 4.")

if __name__ == "__main__":
    # This part runs only when the script is executed directly
    try:
        created_parents = create_parents()
        if created_parents: # Only show menu if parents were created
            show_menu(created_parents)
        else:
            print("Родители не были созданы. Завершение программы.")
    except Exception as main_exception:
        # Catch any unexpected errors during setup or menu operation
        print(f"Произошла непредвиденная ошибка: {main_exception}")
        print("Рекомендуется перезапустить программу.")
