def task_2_pizzeria_orders():
    while True:
        try:
            num_orders = int(input("Введите кол-во заказов: "))
            if num_orders >= 0:
                break
            else:
                print("Количество заказов не может быть отрицательным.")
        except ValueError:
            print(
                "Некорректный ввод. Пожалуйста, введите целое число для количества заказов."
            )

    if num_orders == 0:
        print("Количество заказов равно 0, данные вводить не требуется.")
        return

    orders = {}
    print("Введите заказы (формат: Покупатель Название_пиццы Количество):")
    for i in range(num_orders):
        while True:
            order_input_str = input(f"{i + 1} заказ: ").strip()
            if not order_input_str:
                print("Ввод не может быть пустым.")
                continue

            order_input = order_input_str.split()
            if len(order_input) < 3:
                print(f"Некорректный ввод для заказа {i + 1}. "
                      "Ожидается: Покупатель Название_пиццы Количество.")
                continue

            customer = order_input[0]
            try:
                quantity_str = order_input[-1]
                quantity = int(quantity_str)
                if quantity <= 0:
                    print(f"Количество пицц в заказе {i + 1} "
                          "должно быть положительным.")
                    continue
            except ValueError:
                print(f"Некорректное количество пицц в заказе {i + 1}. "
                      "Ожидается целое число.")
                continue

            pizza_name_parts = order_input[1:-1]
            if not pizza_name_parts:
                print(f"Не указано название пиццы в заказе {i + 1}.")
                continue
            pizza_name = " ".join(pizza_name_parts)

            if customer not in orders:
                orders[customer] = {}

            orders[customer][pizza_name] = \
                orders[customer].get(pizza_name, 0) + quantity
            break

    if not orders:
        print("Нет данных для вывода (возможно, все вводы были некорректны).")
        return

    print("\nСписок заказов по покупателям (отсортировано):")
    sorted_customers = sorted(orders.keys())

    for customer in sorted_customers:
        print(f"{customer}:")
        sorted_pizzas = sorted(orders[customer].keys())
        for pizza in sorted_pizzas:
            print(f"  {pizza}: {orders[customer][pizza]}")


if __name__ == '__main__':
    print("--- Задача 2: Заказы в пиццерии ---")
    task_2_pizzeria_orders()
