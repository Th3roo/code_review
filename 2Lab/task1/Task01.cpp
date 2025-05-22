/*Дано число D и указатель P1 на вершину непустого стека. 
Добавить элемент со значением D в стек и вывести адрес P2 новой вершины стека.

Для каждой динамической структуры должен быть предусмотрен стандартный набор методов - 
добавления/удаления/вывода элементов. 
Во всех задачах обязательно наличие дружественного интерфейса. Ввод данных с клавиатуры.

В заданиях подгруппы структура «стек» (stack) моделируется цепочкой связанных
узлов-записей типа TNode. Поле Next последнего элемента цепочки равно nullptr. Вершиной
стека (top) считается первый элемент цепочки. Для доступа к стеку используется указатель на
его вершину (для пустого стека данный указатель полагается равным nullptr). Значением
элемента стека считается значение его поля Data*/

#include <iostream>
#include <Windows.h>
using namespace std;

class Node 
{
public:
    int x;          // Значение узла
    Node* next;     // Указатель на следующий узел

    Node(int d) : x(d), next(nullptr) {} 
};
class Stack 
{
private:
    Node* top; // Указатель на вершину стека

public:
    Stack() : top(nullptr) {}

    void push(int d) 
    {
        Node* newNode = new Node(d); // Создаем новый узел
        newNode->next = top; // Новый узел указывает на старую вершину
        top = newNode; // Новый узел становится вершиной стека
    }

    void show() const 
    {
        Node* current = top;
        while (current != nullptr) 
        {
            cout << current->x << " ";
            current = current->next;
        }
        cout << endl;
    }

    void showAddress() const 
    {
        cout << "Адрес вершины стека: " << top << endl;
    }
    int getTopValue() const 
    {
        if (top != nullptr) 
        {
            return top->x; 
        }
        return 1; 
    }
    bool isEmpty() const 
    {
        return top == nullptr;
    }
};
int main() {
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    Stack stack;
    int N, n;
    cout << "Сколько чисел вы хотите, чтобы было в стеке? ";
    cin >> N;
    for (int i = 0; i < N; i++) 
    {
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
    if (!stack.isEmpty()) 
    {
        cout << "Значение новой вершины: " << stack.getTopValue() << endl;
    }
    else 
    {
        cout << "Стек пуст!" << endl;
    }

    return 0;
}