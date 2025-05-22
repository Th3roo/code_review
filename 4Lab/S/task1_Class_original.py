class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_info(self):
        return f"Родитель: {self.name}, Возраст: {self.age}, Количество детей: {len(self.children)}"
    
    def calm_child(self, child_index):
        if 0 <= child_index < len(self.children):
            self.children[child_index].calm()
            print(f"{self.children[child_index].name} успокоен.")
        else:
            print("Некорректный номер ребёнка.")
    
    def feed_child(self, child_index):
        if 0 <= child_index < len(self.children):
            self.children[child_index].feed()
            print(f"{self.children[child_index].name} накормлен.")
        else:
            print("Некорректный номер ребёнка.")


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_calm = False
        self.is_hungry = True
    
    def calm(self):
        self.is_calm = True
    
    def feed(self):
        self.is_hungry = False
    
    def get_info(self):
        calm_state = "спокоен" if self.is_calm else "беспокоен"
        hunger_state = "голоден" if self.is_hungry else "сыт"
        return f"Ребёнок: {self.name}, Возраст: {self.age}, Состояние: {calm_state}, Голод: {hunger_state}"
def create_parents():
    parents = []
    num_parents = int(input("Введите количество родителей: "))
    for i in range(num_parents):
        name = input(f"Введите имя родителя {i + 1}: ")
        age = int(input(f"Введите возраст родителя {i + 1}: "))
        parent = Parent(name, age)
        
        num_children = int(input(f"Введите количество детей у родителя {name}: "))
        for j in range(num_children):
            child_name = input(f"Введите имя ребёнка {j + 1} родителя {name}: ")
            child_age = int(input(f"Введите возраст ребёнка {child_name}: "))
            child = Child(child_name, child_age)
            parent.add_child(child)
        
        parents.append(parent)
    
    return parents


def show_menu(parents):
    while True:
        print("\nМеню:")
        print("1. Сообщить информацию о родителе")
        print("2. Сообщить информацию о всех детях родителя")
        print("3. Выполнить действие с ребенком")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            parent_index = int(input("Введите номер родителя: ")) - 1
            if 0 <= parent_index < len(parents):
                print(parents[parent_index].get_info())
            else:
                print("Некорректный номер родителя.")
        
        elif choice == '2':
            parent_index = int(input("Введите номер родителя: ")) - 1
            if 0 <= parent_index < len(parents):
                for i, child in enumerate(parents[parent_index].children, start=1):
                    print(f"{i}. {child.get_info()}")
            else:
                print("Некорректный номер родителя.")
        
        elif choice == '3':
            parent_index = int(input("Введите номер родителя: ")) - 1
            if 0 <= parent_index < len(parents):
                child_index = int(input("Введите номер ребёнка: ")) - 1
                action = input("Введите действие (успокоить/накормить): ").strip().lower()
                
                if action == "успокоить":
                    parents[parent_index].calm_child(child_index)
                elif action == "накормить":
                    parents[parent_index].feed_child(child_index)
                else:
                    print("Некорректное действие.")
            else:
                print("Некорректный номер родителя.")
        
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")

parents = create_parents()
show_menu(parents)