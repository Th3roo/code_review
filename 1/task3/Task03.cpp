//К - ичные числа.Среди чисел в системе счисления с основанием K(2≤K≤10) определить сколько 
//имеется чисел из N(1 < N < 20, N + K < 26) разрядов таких, что в их записи содержится более 
//трех подряд идущих нулей.Для того, чтобы избежать переполнения, ответ представьте в виде 
//вещественного числа.

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <climits>

using namespace std;

double Count(int N, int K) {
    // dp[i][j] — количество чисел длины i, заканчивающихся на j подряд идущих нулей
    // dp[i][4] — количество чисел, где уже было 4+ подряд идущих нулей
    vector<vector<long long>> dp(N + 1, vector<long long>(5, 0));

    dp[1][0] = K - 1;  // Любая цифра кроме нуля
    dp[1][1] = 1;      // Только ноль

    for (int i = 2; i <= N; i++) {
        for (int j = 0; j < 4; j++) {
            dp[i][0] += dp[i - 1][j] * (K - 1);
        }
        dp[i][1] += dp[i - 1][0];
        dp[i][2] += dp[i - 1][1];
        dp[i][3] += dp[i - 1][2];

        dp[i][4] += dp[i - 1][3];

        dp[i][4] += dp[i - 1][4] * K;
    }

    double count = dp[N][4]; cout <<"Количество чисел, содержащих болше 3 нулей подряд: "<< count << endl;
    return count;
}

void HomeDyn16() {
    int N, K;

    cout<<"Система счисления: ";cin >> K;
    cout<<"Количество разрядов: ";cin >> N;

    double all = pow(K, N);
    cout<<"Общее количество: "<<all<<endl;
    double result = Count(N, K) / all;
    cout  << result << endl;
}


int main()
{
    setlocale(LC_ALL, "ru");
    HomeDyn16();
}