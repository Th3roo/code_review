"""
Manages pizza orders for a pizzeria.

This script prompts the user for the number of orders, then for the details
of each order (customer name, pizza name, quantity). It stores this
information and then prints a summary of all orders, grouped by customer
and sorted alphabetically by customer name and then by pizza name.
Input validation is performed at each step.
"""


def task_2_pizzeria_orders():
    """
    Collects pizza order data from the user and prints a summary.

    The function first asks for the total number of orders. If this number is
    positive, it then prompts for each order's details: customer name,
    pizza name (which can contain spaces), and quantity.
    It aggregates orders for the same customer and pizza.
    Finally, it prints a list of all customers in alphabetical order,
    and for each customer, their ordered pizzas (also in alphabetical order)
    along with the total quantity for each pizza.
    Handles various input errors like non-integer inputs for counts,
    negative or zero quantities, and incorrectly formatted order strings.
    """
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
