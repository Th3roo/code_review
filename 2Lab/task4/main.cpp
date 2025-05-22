/*
Дан циклический двусвязный линейный список и указатель первый
элемент этого списка. Необходимо удалить в списке все элементы, у которых правый и
левый сосед совпадают. Если таких элементов нет, то оставить список без изменений.
Первый и последний элементы считать соседями. В результате вернуть ссылку на
последний элемент полученного списка.
Все динамические структуры данных реализовывать через классы. Не использовать STL.  
Для каждой динамической структуры должен быть предусмотрен стандартный
набор методов - добавления/удаления/вывода элементов. Во всех задачах обязательно наличие 
дружественного интерфейса. Ввод данных с клавиатуры.
*/

#include "DoubleList.h"
#include "InputUtils.h"
#include <iostream>


int main() {
	DoubleList number_list;
	int number_count = 0;
	int input_value = 0;

	number_count = getValidatedNonNegativeIntInput("Сколько чисел необходимо ввести?: ");

	if (number_count > 0) {
		std::cout << "Введите " << number_count << " чисел:" << std::endl;
		for (int i = 0; i < number_count; ++i) {
			input_value = getValidatedIntInput("");
			number_list.push_back(input_value);
		}
	} else {
		std::cout << "Введено 0 чисел, список будет пустым." << std::endl;
	}


	std::cout << "Исходный список: ";
	number_list.printList();

	DoubleList::Node* tail_node = number_list.removeNodesWithMatchingNeighbors();

	std::cout << "Обработанный список: ";
	number_list.printList();

	if (tail_node) {
		std::cout << "Последний элемент: " << tail_node->data << std::endl;
	} else {
		std::cout << "Список пуст после обработки." << std::endl;
	}

	return 0;
}
