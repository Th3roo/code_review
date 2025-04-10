#include <iostream>
#include <Windows.h>
#include "Stack.h"

using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    Stack stack;

    int N, n;

    cout << "Сколько чисел вы хотите, чтобы было в стеке? ";
    cin >> N;

    for (int i = 0; i < N; i++) {
        cout << "Введите число " << i + 1 << ": ";
        cin >> n;
        stack.push(n);
    }

    stack.showAddress();

    cout << "Элементы в стеке: ";
    stack.show();

    int D;
    cout << "Введите значение D для добавления в стек: ";
    cin >> D;

    stack.push(D);
    cout << "Элементы в новом стеке: ";
    stack.show();

    stack.showAddress();

    if (!stack.isEmpty()) {
        cout << "Значение новой вершины: " << stack.getTopValue() << endl;
    } else {
        cout << "Стек пуст!" << endl;
    }
    
    return 0;
}