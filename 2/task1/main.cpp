/*
Дано число D и указатель P1 на вершину непустого стека. 
Добавить элемент со значением D в стек и вывести адрес P2 новой вершины стека.

Для каждой динамической структуры должен быть предусмотрен стандартный набор методов - 
добавления/удаления/вывода элементов. 
Во всех задачах обязательно наличие дружественного интерфейса. Ввод данных с клавиатуры.

В заданиях подгруппы структура «стек» (stack) моделируется цепочкой связанных
узлов-записей типа TNode. Поле Next последнего элемента цепочки равно nullptr. Вершиной
стека (top) считается первый элемент цепочки. Для доступа к стеку используется указатель на
его вершину (для пустого стека данный указатель полагается равным nullptr). Значением
элемента стека считается значение его поля Data
*/

#include <iostream>
#include "Stack.h"
#include <locale.h> // Required for setlocale
#include <limits>   // Required for numeric_limits

using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");

    Stack my_stack;

    int num_elements = 0;
    int element_value = 0;

    cout << "Сколько чисел вы хотите, чтобы было в стеке? ";
    while (!(cin >> num_elements)) {
        cout << "Ошибка ввода! Пожалуйста, введите целое число: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    for (int i = 0; i < num_elements; ++i) {
        cout << "Введите число " << i + 1 << ": ";
        while (!(cin >> element_value)) {
            cout << "Ошибка ввода! Пожалуйста, введите целое число: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        my_stack.Push(element_value);
    }

    my_stack.ShowAddress();

    cout << "Элементы в стеке: ";
    my_stack.Show();

    int value_to_add = 0;

    cout << "Введите значение D для добавления в стек: ";
    while (!(cin >> value_to_add)) {
        cout << "Ошибка ввода! Пожалуйста, введите целое число: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    my_stack.Push(value_to_add);

    cout << "Элементы в новом стеке: ";
    my_stack.Show();
    my_stack.ShowAddress();

    if (!my_stack.IsEmpty()) {
        cout << "Значение новой вершины: " << my_stack.GetTopValue() << endl;
    } else {
        cout << "Стек пуст!" << endl;
    }

    return 0;
}