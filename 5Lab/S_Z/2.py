# Задача 2: Заказы в пиццерии

def task_2_pizzeria_orders():
    """
    Решение задачи 2: Заказы в пиццерии.
    В пиццерии хранится информация о том, кто, что и сколько
    заказывал у них в определённый период. Нужно структурировать эту
    информацию, а также понять сколько всего пицц купил каждый
    заказчик. На вход в программу подаётся N заказов. Каждый заказ
    представляет собой строку вида Покупатель - название пиццы -
    количество заказанных пицц. Реализуйте код, который выводит список
    покупателей и их заказов по алфавиту. Учитывайте, что один человек
    может заказать одно и то же несколько раз.
    """
    try:
        num_orders = int(input("Введите кол-во заказов: "))
        if num_orders < 0:
            print("Количество заказов не может быть отрицательным.")
            return
    except ValueError:
        print("Некорректный ввод для количества заказов.")
        return

    orders = {}
    print("Введите заказы (формат: Покупатель Название_пиццы Количество):")
    for i in range(num_orders):
        try:
            order_input = input(f"{i + 1} заказ: ").split()
            if len(order_input) < 3:
                print(f"Некорректный ввод для заказа {i+1}. "
                      "Ожидается: Покупатель Название_пиццы Количество.")
                continue

            customer = order_input[0]
            # Название пиццы может состоять из нескольких слов
            pizza_name = " ".join(order_input[1:-1])
            if not pizza_name:  # Проверка если название пиццы пустое
                print(f"Некорректное название пиццы в заказе {i+1}.")
                continue
            try:
                quantity = int(order_input[-1])
                if quantity <= 0:
                    print(f"Количество пицц в заказе {i+1} "
                          "должно быть положительным.")
                    continue
            except ValueError:
                print(f"Некорректное количество пицц в заказе {i+1}.")
                continue

            if customer not in orders:
                orders[customer] = {}

            orders[customer][pizza_name] = \
                orders[customer].get(pizza_name, 0) + quantity
        except Exception as e:
            print(f"Ошибка при обработке заказа {i+1}: {e}")

    if not orders:
        print("Нет данных для вывода.")
        return

    print("\nСписок заказов по покупателям (отсортировано):")
    sorted_customers = sorted(orders.keys())

    for customer in sorted_customers:
        print(f"{customer}:")
        # Сортируем пиццы по названию для каждого покупателя
        sorted_pizzas = sorted(orders[customer].keys())
        for pizza in sorted_pizzas:
            print(f"  {pizza}: {orders[customer][pizza]}")

if __name__ == '__main__':
    print("--- Задача 2: Заказы в пиццерии ---")
    task_2_pizzeria_orders()