/*
Даны указатели P1 и P2 на начало и конец очереди, содержащей не менее пяти
элементов. Используя тип TQueue (см. задание Dynamic26), описать функцию Dequeue(Q)
целого типа, которая извлекает из очереди первый (начальный) элемент, возвращает его
значение и освобождает память, занимаемую извлеченным элементом (Q — входной и
выходной параметр типа TQueue). С помощью функции Dequeue извлечь из исходной очереди
пять начальных элементов и вывести их значения. Вывести также адреса начала и конца
результирующей очереди (если очередь окажется пустой, то эти адреса должны быть равны
nullptr).

Dynamic26. Даны указатели P1 и P2 на начало и конец очереди (если очередь является пустой,
то P1 = P2 = nullptr). Также дано число N (> 0) и набор из N чисел. Описать тип TQueue — запись
с двумя полями Head и Tail типа PNode (поля указывают на начало и конец очереди) — и
процедуру Enqueue(Q, D), которая добавляет в конец очереди Q новый элемент со значением D
(Q — входной и выходной параметр типа TQueue, D — входной параметр целого типа). С
помощью процедуры Enqueue добавить в исходную очередь данный набор чисел и вывести
новые адреса ее начала и конца.

Для каждой динамической структуры должен быть предусмотрен стандартный набор методов - 
добавления/удаления/вывода элементов. 
Во всех задачах обязательно наличие дружественного интерфейса. Ввод данных с клавиатуры.

В заданиях данной подгруппы структура «очередь» (queue) моделируется цепочкой связанных
узлов-записей типа TNode. Поле Next последнего элемента цепочки равно nullptr. Началом
очереди («головой», head) считается первый элемент цепочки, концом («хвостом», tail) — ее
последний элемент. Для возможности быстрого добавления в конец очереди нового элемента
удобно хранить, помимо указателя на начало очереди, также и указатель на ее конец. В случае
пустой очереди указатели на ее начало и конец полагаются равными nullptr. Как и для стека,
значением элемента очереди считается значение его поля Data.
*/

#include <iostream>
#include "Queue.h"

using namespace std;

int main() {
	Queue myQueue;

	cout << "Заполнение очереди элементами от 1 до 10..." << endl;
	for (int i = 1; i <= 10; ++i) {
		Enqueue(myQueue, i);
	}
	cout << "Начальное состояние:" << endl;

	cout << "Адрес начала: " << myQueue.front << ", Адрес конца: " << myQueue.rear << endl;
	if (myQueue.front) cout << "Значение начала: " << myQueue.front->data << endl;
	if (myQueue.rear) cout << "Значение конца: " << myQueue.rear->data << endl;


	// Dequeue five elements as per the task description
	cout << "Извлечение пяти начальных элементов:" << endl;
	cout << "Извлеченные элементы: ";

	int dequeuedValue = 0;
	int successfulDequeues = 0;
	for (int i = 0; i < 5; ++i) {
		if (Dequeue(myQueue, dequeuedValue)) {
			cout << dequeuedValue << " ";
			successfulDequeues++;
		} else {
			cout << "\nОчередь стала пустой во время извлечения.";
			break;
		}
	}
	cout << endl;

	if (successfulDequeues < 5 && myQueue.front == nullptr) {
		cout << "Не удалось извлечь 5 элементов, так как очередь закончилась." << endl;
	}


	
	cout << "Итоговое состояние очереди:" << endl;
	if (myQueue.front != nullptr) {
		cout << "Адрес начала очереди: " << myQueue.front << ", Значение: " << myQueue.front->data << endl;
	} else {
		cout << "Очередь пуста, адрес начала: nullptr" << endl;
	}

	if (myQueue.rear != nullptr) {
		cout << "Адрес конца очереди: " << myQueue.rear << ", Значение: " << myQueue.rear->data << endl;
	} else {
		cout << "Очередь пуста, адрес конца: nullptr" << endl;
	}

	return 0;
}
