"""
Manages pizza orders for a pizzeria.

This script allows a user to input a number of pizza orders, detailing
the customer, pizza name, and quantity for each. It then aggregates
these orders and prints a summary, sorted by customer name and then
by pizza name.
"""
from collections import defaultdict


def get_number_of_orders():
    """
    Gets a valid non-negative integer for the number of orders from the user.

    Continuously prompts the user until a non-negative integer is entered.
    Handles ValueError for non-integer inputs and prompts again if a
    negative number is entered.

    Returns:
        int: The non-negative number of orders entered by the user.
    """
    while True:
        try:
            n = int(input("Введите кол-во заказов: "))
            if n >= 0:
                return n
            else:
                print("Количество заказов не может быть отрицательным.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def input_pizza_orders(num_orders):
    """
    Inputs pizza order data from the user for a specified number of orders.

    For each order, prompts for customer name, pizza name, and quantity.
    Validates that quantity is a positive integer. Orders are aggregated
    if a customer orders the same pizza multiple times.

    Args:
        num_orders (int): The total number of orders to input.

    Returns:
        defaultdict: A nested defaultdict where the outer keys are customer
                     names (str), and the inner keys are pizza names (str),
                     with values being the total quantity (int) of that pizza
                     ordered by the customer. Returns an empty defaultdict
                     if num_orders is 0.
    """
    orders = defaultdict(lambda: defaultdict(int))
    if num_orders == 0:
        print("Количество заказов равно 0, ввод данных пропускается.")
        return orders

    print("Введите заказы (формат: Покупатель НазваниеПиццы Количество):")
    for i in range(1, num_orders + 1):
        while True:
            order_str = input(f"{i} заказ: ").strip()
            if not order_str:
                print("Ввод не может быть пустым.")
                continue

            order_parts = order_str.split()
            if len(order_parts) != 3:
                print("Некорректный формат. Ожидается: "
                      "Покупатель НазваниеПиццы Количество (3 слова).")
                continue

            customer, pizza, quantity_str = order_parts
            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("Количество пицц должно быть положительным числом.")
                    continue
            except ValueError:
                print("Количество пицц должно быть целым числом.")
                continue

            orders[customer][pizza] += quantity
            break
    return orders


def print_customer_orders(orders_data):
    """
    Prints formatted pizza orders sorted by customer and pizza name.

    If there are no orders, it prints a message indicating that.
    Otherwise, it iterates through the sorted customer names, and for each
    customer, prints their ordered pizzas (sorted by pizza name) along
    with the quantities.

    Args:
        orders_data (defaultdict): A nested defaultdict containing the pizza
                                   orders, as returned by `input_pizza_orders`.
    """
    if not orders_data:
        print("\nНет заказов для отображения.")
        return

    print("\nДетализированные заказы по клиентам:")
    for customer in sorted(orders_data.keys()):
        print(f"{customer}:")
        sorted_pizzas = sorted(orders_data[customer].items())
        for pizza, quantity in sorted_pizzas:
            print(f"  {pizza}: {quantity}")
        print()


def main():
    """Main function to manage pizza orders."""
    print("--- Обработка заказов пиццы ---")
    num_orders = get_number_of_orders()
    customer_orders = input_pizza_orders(num_orders)
    print_customer_orders(customer_orders)


if __name__ == "__main__":
    main()
