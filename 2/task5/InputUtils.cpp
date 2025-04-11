#include "InputUtils.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>   // rand() srand()
#include <ctime>     // time()
#include <limits>    // numeric_limits
#include <ios>       // std::ios_base::failure
#include <string>    // to_string

using namespace std;

bool FuncKeyboard(deque<int>& outputDeque)
{
	outputDeque.clear();
	int elementCount;
	cout << "Введите количество целых чисел (нечетное и >= 5): ";

	while (!(cin >> elementCount) || elementCount < 5 || elementCount % 2 == 0)
	{
		cout << "Ошибка ввода. Количество должно быть целым нечетным числом >= 5. Повторите ввод: ";
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
	}

	cout << "Введите " << elementCount << " целых чисел:" << endl;
	for (int i = 0; i < elementCount; ++i)
	{
		int inputNumber;
		while (!(cin >> inputNumber)) {
			cout << "Ошибка ввода. Введите целое число: ";
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
		}
		outputDeque.push_back(inputNumber);
	}

	return true;
}

bool FuncRandom(deque<int>& outputDeque, int elementCount)
{
	outputDeque.clear();
	if (elementCount < 5 || elementCount % 2 == 0) {
        cerr << "Ошибка: Количество для FuncRandom должно быть нечетным и >= 5 (получено " << elementCount << ")." << endl;
		return false;
	}

	for (int i = 0; i < elementCount; ++i)
	{
		outputDeque.push_back(rand() % 100);
	}

	return true;
}

bool FuncFile(deque<int>& outputDeque, const string& sourceFilename)
{
	outputDeque.clear();
	ifstream inputFileStream(sourceFilename);
	int readNumber;

	if (!inputFileStream.is_open())
	{
		cerr << "Ошибка: Не удалось открыть файл '" << sourceFilename << "'." << endl;
		return false;

	while (inputFileStream >> readNumber)
	{
		outputDeque.push_back(readNumber);
	}

	if (inputFileStream.bad()) {
		cerr << "Ошибка чтения из файла '" << sourceFilename << "' (badbit)." << endl;
		inputFileStream.close();
		return false;
	} else if (inputFileStream.fail() && !inputFileStream.eof()) {
        cerr << "Ошибка: Некорректные данные в файле '" << sourceFilename << "'. Ожидались целые числа." << endl;
        inputFileStream.close();
        return false;
    }

	inputFileStream.close();

	if (outputDeque.size() < 5 || outputDeque.size() % 2 == 0)
	{
		cerr << "Ошибка: Количество чисел в файле '" << sourceFilename << "' должно быть нечетным и >= 5 (найдено " << outputDeque.size() << ")." << endl;
		return false;
	}

	return true;
} 