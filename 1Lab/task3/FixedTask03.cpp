//FIX ME задача не по шаблону
/* - ичные числа.Среди чисел в системе счисления с основанием K(2≤K≤10) определить сколько 
* меется чисел из N(1 < N < 20, N + K < 26) разрядов таких, что в их записи содержится более 
* трех подряд идущих нулей.Для того, чтобы избежать переполнения, ответ представьте в виде 
* вещественного числа.
*/

#include <iostream>
// #include <fstream> // Не используется
#include <vector>
#include <cmath>
#include <iomanip>
// #include <climits> // Не используется
#include <limits> // numeric_limits
#include <string> 
#include "Count.h"

using namespace std;

int readValidatedInt(const string& prompt) {
    int value;
    while (true) {
        cout << prompt;
        cin >> value;

        if (cin.good()) {
            return value;
        } else {
            cout << " Ошибка: Введите целое число." << endl;
            cin.clear(); // Сброс флагов ошибок ввода
            // Очистка буфера ввода до следующей новой строки
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
}

//FIX ME названия переменных однобуквенные
double Count(int numDigits, int base) {
    // dp[i][j] — количество чисел длины i, заканчивающихся на j подряд идущих нулей
    // dp[i][4] — количество чисел длины i, где уже было 4+ подряд идущих нулей
    vector<vector<long long>> dp(numDigits + 1, vector<long long>(5, 0));

    dp[1][0] = base - 1;  // Любая цифра кроме нуля
    dp[1][1] = 1;      // Только ноль

    for (int i = 2; i <= numDigits; i++) {
        // Переход для чисел, НЕ заканчивающихся на ноль
        for (int j = 0; j < 4; j++) {
            dp[i][0] += dp[i - 1][j] * (base - 1);
        }
        // Переходы для чисел, заканчивающихся на 1, 2 или 3 нуля
        dp[i][1] += dp[i - 1][0];
        dp[i][2] += dp[i - 1][1];
        dp[i][3] += dp[i - 1][2];

        // Переход для чисел, где только что стало 4 нуля подряд
        dp[i][4] += dp[i - 1][3];

        // Переход для чисел, где уже было 4+ нуля подряд
        dp[i][4] += dp[i - 1][4] * base;
    }

    double countWithFourOrMoreZeros = dp[numDigits][4];
    cout <<"Количество чисел, содержащих болше 3 нулей подряд: "<< countWithFourOrMoreZeros << endl;
    return countWithFourOrMoreZeros;
}

void HomeDyn16() {
    int numDigits, base;

    // FIX ME валидация ввода
    base = readValidatedInt("Система счисления: ");
    numDigits = readValidatedInt("Количество разрядов: ");

    double totalNumbers = pow(base, numDigits);
    cout<<"Общее количество: " << totalNumbers << endl;

    double result = Count(numDigits, base) / totalNumbers; // Отношение чисел с 4+ нулями ко всем числам
    cout << "Отношение: " << result << endl;
}

// FIX ME фигурная скобка
int main(){
    setlocale(LC_ALL, "ru");
    HomeDyn16();
    return 0;
}