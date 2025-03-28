//Строки, определяющие выражения, не содержат пробелов. 
//При выполнении заданий не следует использовать оператор цикла.
//Вывести значение целочисленного выражения, заданного в виде строки S.Выражение
//определяется следующим образом :
//		<выражение> :: = <цифра> | <выражение> +<цифра> | <выражение> − <цифра>

#include <iostream> 
#include <string> 
using namespace std;
int calc(string str);
int element(string str)
{
	if (str[0] == '(' && str[str.size() - 1] == ')')
		return calc(str.substr(1, str.size() - 2));
	return stoi(str);
}
int term(string str)
{
	int i = str.size() - 1;
	int level = 0;
	int pos = -1;
	while (i >= 0)
	{
		if (str[i] == ')')
			level++;
		if (str[i] == '(')
			level--;
		if (level == 0 && str[i] == '*')
		{
			pos = i;
			break;
		}
		i--; // постфикс низя
	}
	if (pos == -1)
		return element(str);
	return term(str.substr(0, pos)) * element(str.substr(pos + 1));
}
int calc(string str)
{
	int i = str.size() - 1;
	int level = 0;
	int pos = -1;
	while (i >= 0)
	{
		if (str[i] == ')')
			level++;
		if (str[i] == '(')
			level--;
		if (level == 0 && (str[i] == '-' || str[i] == '+'))
		{
			pos = i;
			break;
		}
		i--;
	}
	if (pos == -1)
		return term(str);
	char ch = str[pos];
	if (ch == '+')
		return calc(str.substr(0, pos)) + term(str.substr(pos + 1));
	if (ch == '-')
		return calc(str.substr(0, pos)) - term(str.substr(pos + 1));
	return 0;
}
int main()
{
	setlocale(LC_ALL, "Russian");
	cout << "Программа считает значение выражения которое вы введете" << endl;
	string str;
	cout << "Введите выражение: ";
	getline(cin, str);
	int r = calc(str);
	cout << "Ответ: " << r << endl;
	return 0;
}




