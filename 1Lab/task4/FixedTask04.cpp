//FIX ME не по шаблону
/*
* Строки, определяющие выражения, не содержат пробелов. 
* При выполнении заданий не следует использовать оператор цикла.
* Вывести значение целочисленного выражения, заданного в виде строки S.Выражение
* определяется следующим образом :
* 		<выражение> :: = <цифра> | <выражение> +<цифра> | <выражение> − <цифра>
*/

#include <iostream> 
#include <string>
#include "evaluate.h"

using namespace std;

// FIX ME названия
int evaluate_expression(string expression); 
int evaluate_term(string expression); 
int evaluate_factor(string expression);

bool is_valid_expression(const string& expression) {
    int parenthesis_balance = 0;
    for (char c : expression) {
        if (!isdigit(c) && c != '+' && c != '-' && c != '*' && c != '(' && c != ')') {
            cout << "Ошибка: Недопустимый символ '" << c << "' в выражении." << endl;
            return false; 
        }
        if (c == '(') {
            parenthesis_balance++;
        } else if (c == ')') {
            parenthesis_balance--;
        }
        if (parenthesis_balance < 0) {
            cout << "Ошибка: Несбалансированные скобки (лишняя закрывающая)." << endl;
            return false;
        }
    }
    if (parenthesis_balance != 0) {
         cout << "Ошибка: Несбалансированные скобки (не хватает закрывающей)." << endl;
        return false;
    }
    return true;
}

int evaluate_factor(string expression) {
	if (expression[0] == '(' && expression[expression.size() - 1] == ')')
		return evaluate_expression(expression.substr(1, expression.size() - 2));
	return stoi(expression);
}

int evaluate_term(string expression) {
	int index = expression.size() - 1;
	int parenthesis_level = 0;
	int multiplication_pos = -1;
	while (index >= 0) {
		if (expression[index] == ')')
			parenthesis_level++;
		if (expression[index] == '(')
			parenthesis_level--;
		if (parenthesis_level == 0 && expression[index] == '*') {
			multiplication_pos = index;
			break;
		}
		index--;
	}
	if (multiplication_pos == -1)
		return evaluate_factor(expression);
	return evaluate_term(expression.substr(0, multiplication_pos)) * evaluate_factor(expression.substr(multiplication_pos + 1));
}

int evaluate_expression(string expression) {
	int index = expression.size() - 1;
	int parenthesis_level = 0;
	int add_sub_pos = -1;
	while (index >= 0) {
		if (expression[index] == ')')
			parenthesis_level++;
		if (expression[index] == '(')
			parenthesis_level--;
		if (parenthesis_level == 0 && (expression[index] == '-' || expression[index] == '+')) {
			add_sub_pos = index;
			break;
		}
		index--;
	}
	if (add_sub_pos == -1)
		return evaluate_term(expression);
	char operator_char = expression[add_sub_pos];
	if (operator_char == '+')
		return evaluate_expression(expression.substr(0, add_sub_pos)) + evaluate_term(expression.substr(add_sub_pos + 1));
	if (operator_char == '-')
		return evaluate_expression(expression.substr(0, add_sub_pos)) - evaluate_term(expression.substr(add_sub_pos + 1));
	return 0;
}

int main() {
	setlocale(LC_ALL, "Russian");
	cout << "Программа считает значение выражения которое вы введете" << endl;
	string input_expression;
	
	do {
	    cout << "Введите выражение: ";
	    getline(cin, input_expression);
        
	    size_t first = input_expression.find_first_not_of(' ');
        if (string::npos == first) { // String is all spaces
             input_expression = "";
        } else {
             size_t last = input_expression.find_last_not_of(' ');
             input_expression = input_expression.substr(first, (last - first + 1));
        }
        
        if (input_expression.empty()) {
             cout << "Ошибка: Введена пустая строка." << endl;
             continue; 
        }

	} while (!is_valid_expression(input_expression));

	int result = evaluate_expression(input_expression);
	cout << "Ответ: " << result << endl;
	return 0;
}