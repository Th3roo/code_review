/*
Все динамические структуры данных реализовывать через классы. Не использовать STL.  
Для каждой динамической структуры должен быть предусмотрен
стандартный набор методов - добавления/удаления/вывода элементов. Во всех задачах обязательно
наличие дружественного интерфейса. Ввод данных с клавиатуры.

 Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вставить значение M перед каждым вторым элементом списка, и вывести ссылку на последний
элемент полученного списка P2. При нечетном числе элементов исходного списка в конец
списка вставлять не надо.
*/

#include <iostream>
using namespace std;
class Node {
public:
    int data;       
    Node* next;     
    Node(int value) : data(value), next(nullptr) {}
};

class LinkedList {
private:
    Node* head; 

public:
    
    LinkedList() : head(nullptr) {}

    void add(int value) {
        Node* newNode = new Node(value); 
        if (head == nullptr) {           
            head = newNode;              
        }
        else {
            Node* current = head;        
            while (current->next != nullptr) { 
                current = current->next;
            }
            current->next = newNode;   
        }
    }

    // Метод для вставки значения M перед каждым вторым элементом
    void insertBeforeEverySecond(int M) {
        Node* current = head;          
        int count = 1;                  // Счетчик для отслеживания позиции

        while (current != nullptr && current->next != nullptr) {
            if (count % 2 == 1) {       // Если текущий элемент — первый в паре
                Node* newNode = new Node(M); // Создаем новый узел со значением M
                newNode->next = current->next; // Новый узел указывает на следующий элемент
                current->next = newNode; // Текущий узел указывает на новый узел
                current = newNode->next; // Переходим к следующему элементу
            }
            else {
                current = current->next; 
            }
            count++;                  
        }
    }

    
    void print() {
        Node* current = head;           // Начинаем с головы списка
        while (current != nullptr) {    // Пока не дойдем до конца списка
            cout << current->data << " "; // Выводим данные текущего узла
            current = current->next;    // Переходим к следующему узлу
        }
        cout << endl;         // Переход на новую строку после вывода
    }

    // Метод для получения указателя на последний элемент списка
    Node* getLastNode() {
        Node* current = head;           // Начинаем с головы списка
        while (current != nullptr && current->next != nullptr) { // Идем до последнего узла
            current = current->next;
        }
        return current;                 // Возвращаем указатель на последний узел
    }
    void clearList() {
        while (head != nullptr) {       // Пока список не пуст
            Node* temp = head;          // Сохраняем текущую голову
            head = head->next;          // Перемещаем голову на следующий узел
            delete temp;                // Удаляем узел
        }
        cout << "Список очищен." << endl;
    }
    
    friend void insertBeforeEverySecond(LinkedList& list, int M);
};


void insertBeforeEverySecond(LinkedList& list, int M) {
    list.insertBeforeEverySecond(M);
}

int main() {
    LinkedList list;                     // Создаем список
    int n, value, M;

    
    cout << "Введите количество элементов в списке: ";
    cin >> n;
    cout << "Введите элементы списка: ";
    for (int i = 0; i < n; ++i) {
        cin >> value;               // Вводим значение элемента
        list.add(value);                 // Добавляем элемент в список
    }

   
    cout << "Введите значение M для вставки: ";
    cin >> M;

    // Вставка значения M перед каждым вторым элементом
    insertBeforeEverySecond(list, M);

    
    cout << "Список после вставки: ";
    list.print();

    // Получение указателя на последний элемент списка
    Node* lastNode = list.getLastNode();

    // Вывод результата
    if (lastNode != nullptr) {
        cout << "Указатель на последний элемент списка: " << lastNode << endl;
        cout << "Значение последнего элемента: " << lastNode->data <<endl;
    }
    else {
        cout << "Список пуст." << endl;

    }
    list.clearList();

    // Проверка, что список пуст
    cout << "Проверка списка после очистки: ";
    list.print();


    return 0;                           
}