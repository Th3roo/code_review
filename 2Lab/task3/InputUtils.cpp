#include "InputUtils.h"
#include <iostream>
#include <limits>
#include <string>

using namespace std; 

int getValidatedIntInput(const string& prompt) {
	int value = 0;
	while (true) {
		cout << prompt;
		cin >> value;

		if (cin.fail()) {
			cout << "Ошибка ввода! Пожалуйста, введите целое число." << endl;
			cin.clear(); 
			cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
		} else {
			cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
			return value; 
		}
	}
}

int getValidatedNonNegativeIntInput(const string& prompt) {
	int value = 0;
	while (true) {
		cout << prompt;
		cin >> value;

		if (cin.fail()) {
			cout << "Ошибка ввода! Пожалуйста, введите целое число." << endl;
			cin.clear(); 
			cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
		} else if (value < 0) { 
            cout << "Ошибка ввода! Количество не может быть отрицательным. Пожалуйста, введите целое неотрицательное число." << endl;
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
        } else {
			cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
			return value; 
		}
	}
} 