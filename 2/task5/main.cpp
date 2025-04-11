/* 
Элементами контейнеров являются целые числа. Для
заполнения контейнера использовать итератор и конструктор соответствующего контейнера,
для вывода элементов использовать итератор (для вывода элементов в обратном порядке
использовать обратные итераторы, возвращаемые функциями-членами rbegin и rend)
Обязательно наличие дружественного интерфейса. Ввод данных организовать
разными способами (с клавиатуры, рандом, из файла)


 Дан дек D с нечетным количеством элементов N (≥ 5). Добавить в начало дека пять
его средних элементов в исходном порядке. Использовать один вызов функции-члена insert. 
*/

#include <iostream>
#include <deque>
#include <iterator> 
#include <limits>    
#include <clocale>   
#include <cstdlib>   
#include <ctime>     

#include "Deque.h"       
#include "InputUtils.h"  

using namespace std; 

int main()
{
	setlocale(LC_ALL, "ru");
	srand(static_cast<unsigned>(time(0))); 

	int inputMethodChoice;
	cout << "Выберите метод ввода данных:" << endl;
	cout << "1. Ввод с клавиатуры" << endl;
	cout << "2. Случайные числа" << endl;
	cout << "3. Чтение из файла 'a.txt'" << endl;
	cout << "Ваш выбор: ";

	while (!(cin >> inputMethodChoice) || inputMethodChoice < 1 || inputMethodChoice > 3) {
		cout << "Ошибка ввода. Введите число от 1 до 3: ";
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
	}

	deque<int> dataDeque;
	bool inputSuccess = false;

	switch (inputMethodChoice)
	{
		case 1:
			inputSuccess = FuncKeyboard(dataDeque);
			break;
		case 2:
		{
			int randomElementCount;
			cout << "Введите количество чисел (нечетное и >= 5): ";
			// Keep the loop for getting a valid count *before* calling FuncRandom
			while (!(cin >> randomElementCount) || randomElementCount < 5 || randomElementCount % 2 == 0)
			{
				cout << "Ошибка ввода. Количество должно быть целым нечетным числом >= 5. Повторите ввод: ";
				cin.clear();
				cin.ignore(numeric_limits<streamsize>::max(), '\n');
			}
			inputSuccess = FuncRandom(dataDeque, randomElementCount);
			break;
		}
		case 3:
		{
			inputSuccess = FuncFile(dataDeque); // a.txt
			break;
		}
	}

	if (!inputSuccess) {
		cerr << "Не удалось получить данные для дека. Завершение программы." << endl;
		return 1;
	}

	cout << "Исходный дек: ";
	for (const auto& element : dataDeque)
	{
		cout << element << " ";
	}
	cout << endl;
	
	cout << "Исходный дек (обратный порядок): ";
	for (auto reverseIter = dataDeque.rbegin(); reverseIter != dataDeque.rend(); ++reverseIter) {
		cout << *reverseIter << " ";
	}
	cout << endl;

	FuncInsert(dataDeque);
	cout << "Дек после вставки: ";
	for (const auto& element : dataDeque)
	{
		cout << element << " ";
	}
	cout << endl;
	
	cout << "Дек после вставки (обратный порядок): ";
	for (auto reverseIter = dataDeque.rbegin(); reverseIter != dataDeque.rend(); ++reverseIter) {
		cout << *reverseIter << " ";
	}
	cout << endl;
	
	return 0;
