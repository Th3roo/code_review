"""
This module defines Child and Parent classes, and a main function
to interact with them through a console menu. It allows creating
parents and children, viewing their information, and performing
actions like calming or feeding a child.
"""

class Child:
    """
    Represents a child with a name, age, and states of calmness and hunger.
    """
    def __init__(self, name: str, age: int):
        """
        Initializes a Child object.

        Args:
            name: The name of the child. Must be a non-empty string.
            age: The age of the child. Must be a non-negative integer.

        Raises:
            TypeError: If name is not a string or age is not an integer.
            ValueError: If name is empty or age is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Child's name must be a string.")
        if not name.strip():
            raise ValueError("Child's name cannot be empty.")
        if not isinstance(age, int):
            raise TypeError("Child's age must be an integer.")
        if age < 0:
            raise ValueError("Child's age cannot be negative.")

        self.name = name.strip()
        self.age = age
        self.is_calm = True  # Initial state: calm
        self.is_fed = True   # Initial state: fed

    def __str__(self) -> str:
        """
        Returns a string representation of the child's status.
        """
        calm_status = 'Да' if self.is_calm else 'Нет'
        fed_status = 'Да' if self.is_fed else 'Нет'
        return (f"Ребенок: {self.name}, Возраст: {self.age}, "
                f"Спокоен: {calm_status}, Сыт: {fed_status}")

class Parent:
    """
    Represents a parent with a name, age, and a list of their children.
    """
    def __init__(self, name: str, age: int):
        """
        Initializes a Parent object.

        Args:
            name: The name of the parent. Must be a non-empty string.
            age: The age of the parent. Must be a non-negative integer.

        Raises:
            TypeError: If name is not a string or age is not an integer.
            ValueError: If name is empty or age is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Parent's name must be a string.")
        if not name.strip():
            raise ValueError("Parent's name cannot be empty.")
        if not isinstance(age, int):
            raise TypeError("Parent's age must be an integer.")
        if age < 0:
            raise ValueError("Parent's age cannot be negative.")

        self.name = name.strip()
        self.age = age
        self.children: list[Child] = []

    def add_child(self, child: Child):
        """
        Adds a child to the parent's list of children.

        Args:
            child: An instance of the Child class.

        Raises:
            TypeError: If child is not an instance of Child.
            ValueError: If child's age is greater than or equal to parent's age.
        """
        if not isinstance(child, Child):
            raise TypeError("The object to add must be an instance of Child.")
        if child.age >= self.age:
            raise ValueError(
                f"Child '{child.name}' ({child.age} y.o.) "
                f"cannot be older than or same age as parent "
                f"'{self.name}' ({self.age} y.o.)."
            )
        self.children.append(child)

    def get_info(self) -> str: # Renamed from info for clarity
        """
        Returns a string with information about the parent.
        """
        return (f"Родитель: {self.name}, Возраст: {self.age}, "
                f"Количество детей: {len(self.children)}")

    def _validate_child_index(self, index: int) -> bool:
        """Helper to validate child index."""
        if not isinstance(index, int):
            print("Ошибка: Номер ребенка должен быть целым числом.")
            return False
        if not (0 <= index < len(self.children)):
            print("Ошибка: Неверный номер ребенка.")
            return False
        return True

    def calm_child(self, child_index: int):
        """
        Sets a specific child's state to calm.

        Args:
            child_index: The index of the child in the children list.
        """
        if self._validate_child_index(child_index):
            self.children[child_index].is_calm = True
            print(
                f"{self.name} успокоил(а) ребенка "
                f"{self.children[child_index].name}."
            )

    def feed_child(self, child_index: int):
        """
        Sets a specific child's state to fed.

        Args:
            child_index: The index of the child in the children list.
        """
        if self._validate_child_index(child_index):
            self.children[child_index].is_fed = True
            print(
                f"{self.name} покормил(а) ребенка "
                f"{self.children[child_index].name}."
            )

def get_int_input(prompt: str, non_negative: bool = False, positive: bool = False) -> int:
    """
    Prompts user for integer input and validates it.

    Args:
        prompt: The message displayed to the user.
        non_negative: If True, input must be >= 0.
        positive: If True, input must be > 0.

    Returns:
        The validated integer input.
    """
    while True:
        try:
            value_str = input(prompt).strip()
            value = int(value_str)
            if non_negative and value < 0:
                print("Ошибка: Значение не может быть отрицательным.")
            elif positive and value <= 0:
                print("Ошибка: Значение должно быть положительным.")
            else:
                return value
        except ValueError:
            print("Ошибка: Введите целое число.")

def get_string_input(prompt: str) -> str:
    """
    Prompts user for a non-empty string input.

    Args:
        prompt: The message displayed to the user.

    Returns:
        The validated string input.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: Ввод не может быть пустым.")

def main():
    """
    Main function to run the parent-child interaction program.
    """
    parents: list[Parent] = []
    num_parents = get_int_input(
        "Введите количество родителей: ", positive=True
    )

    for i in range(num_parents):
        print(f"\n--- Ввод данных для родителя {i + 1} ---")
        parent_name = get_string_input(f"Введите имя родителя {i + 1}: ")
        parent_age = get_int_input(
            f"Введите возраст родителя {parent_name}: ", non_negative=True
        )
        try:
            parent = Parent(parent_name, parent_age)
        except (TypeError, ValueError) as e:
            print(f"Ошибка создания родителя: {e}")
            continue # Skip to next parent if creation fails

        num_children = get_int_input(
            f"Введите количество детей для родителя {parent_name}: ",
            non_negative=True
        )
        for j in range(num_children):
            print(f"\n--- Ввод данных для ребенка {j + 1} родителя {parent_name} ---")
            child_name = get_string_input(f"Введите имя ребенка {j + 1}: ")
            child_age = get_int_input(
                f"Введите возраст ребенка {child_name}: ", non_negative=True
            )
            try:
                child = Child(child_name, child_age)
                parent.add_child(child)
            except (TypeError, ValueError) as e:
                print(f"Ошибка добавления ребенка: {e}")
        parents.append(parent)

    if not parents:
        print("Нет родителей для взаимодействия. Завершение программы.")
        return

    while True:
        print("\nМеню:")
        print("1. Информация о родителе")
        print("2. Информация о детях родителя")
        print("3. Выполнить действие с ребенком")
        print("4. Выход")

        menu_choice = get_int_input("Выберите действие (1-4): ")

        if menu_choice == 1:
            parent_idx = get_int_input(
                "Введите номер родителя (1-N): ", positive=True
            ) - 1
            if 0 <= parent_idx < len(parents):
                print(parents[parent_idx].get_info())
            else:
                print("Неверный номер родителя.")
        elif menu_choice == 2:
            parent_idx = get_int_input(
                "Введите номер родителя (1-N): ", positive=True
            ) - 1
            if 0 <= parent_idx < len(parents):
                selected_parent = parents[parent_idx]
                if not selected_parent.children:
                    print(f"У родителя {selected_parent.name} нет детей.")
                else:
                    print(f"Дети родителя {selected_parent.name}:")
                    for i, child_obj in enumerate(selected_parent.children):
                        print(f"{i + 1}. {child_obj}")
            else:
                print("Неверный номер родителя.")
        elif menu_choice == 3:
            parent_idx = get_int_input(
                "Введите номер родителя (1-N): ", positive=True
            ) - 1
            if 0 <= parent_idx < len(parents):
                selected_parent = parents[parent_idx]
                if not selected_parent.children:
                    print(f"У родителя {selected_parent.name} нет детей "
                          "для выполнения действий.")
                    continue
                child_idx = get_int_input(
                    f"Введите номер ребенка (1-{len(selected_parent.children)}): ",
                    positive=True
                ) - 1
                
                action = get_string_input(
                    "Введите действие (успокоить/покормить): "
                ).lower()
                if action == "успокоить":
                    selected_parent.calm_child(child_idx)
                elif action == "покормить":
                    selected_parent.feed_child(child_idx)
                else:
                    print("Неверное действие. Доступно: 'успокоить' или 'покормить'.")
            else:
                print("Неверный номер родителя.")
        elif menu_choice == 4:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")

if __name__ == "__main__":
    main()
