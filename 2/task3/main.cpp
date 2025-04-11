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
#include <limits>
#include <string>
#include "LinkedList.h"
#include "InputUtils.h

using namespace std; 

int main() {
	LinkedList list;
	int numberOfElements = 0;
	int elementValue = 0;
	int valueToInsert = 0;

	numberOfElements = getValidatedNonNegativeIntInput("Введите количество элементов в списке: "); 

	cout << "Введите элементы списка: " << endl;
	for (int i = 0; i < numberOfElements; ++i) {
        string prompt = "Введите число " + to_string(i + 1) + ": "; 
		elementValue = getValidatedIntInput(prompt); 
		list.add(elementValue);
	}

	valueToInsert = getValidatedIntInput("Введите значение M для вставки: "); 

	insertBeforeEverySecond(list, valueToInsert);

	cout << "Список после вставки: ";
	list.print();

	Node* lastNode = list.getLastNode();

	if (lastNode != nullptr) {
		cout << "Указатель на последний элемент списка: " << lastNode << endl;
		cout << "Значение последнего элемента: " << lastNode->data << endl;
	} else {
		cout << "Список пуст." << endl;
	}
    
    cout << "Очистка списка..." << endl;
	list.clearList();

	cout << "Проверка списка после очистки: ";
	list.print();

	return 0;
}
