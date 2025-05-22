//Археолог нашел N артефактов.Известны веса(сi) и налоговое бремя(di) находок.
//Нужно выбрать такое подмножество находок, чтобы их суммарный вес превысил Z кг, а их общее 
//налоговое бремя оказалось минимальным.Известно, что решение единственно.Укажите
//порядковые номера вещей, которые нужно взять.Исходный данные находятся в текстовом файле, 
//в первой строке указаны N и Z, а во второй строке значения весов(в кг), в третьей - величина
//налога по каждой находке.Вывести так же суммарный вес и общую ценность результата.

#include <iostream>
#include <fstream>
#include <vector>
#include <climits>
using namespace std;

// Функция для решения задачи о рюкзаке
void knapSack(int W, vector<int>& wt, vector<int>& val) {
    int n = wt.size(); // Количество предметов
    int maxWeight = 0; // Максимально возможный вес всех предметов
    for (int w : wt) maxWeight += w; // Считаем общий вес всех предметов

    // Вектор dp, где dp[w] хранит минимальное налоговое бремя для веса w
    vector<int> dp(maxWeight + 1, INT_MAX);
    dp[0] = 0; // Нулевой вес имеет нулевое налоговое бремя

    // Матрица selected, где selected[w][i] = true, если предмет i включен в набор для веса w
    vector<vector<bool>> selected(maxWeight + 1, vector<bool>(n, false));

    // Заполняем dp и selected
    for (int i = 0; i < n; i++) { // Перебираем все предметы
        for (int w = maxWeight; w >= wt[i]; w--) // Перебираем все возможные веса
        { 
            // Если можно достичь веса (w - wt[i]) и добавление текущего предмета улучшает результат
            if (dp[w - wt[i]] != INT_MAX && dp[w - wt[i]] + val[i] < dp[w]) 
            {
                dp[w] = dp[w - wt[i]] + val[i]; // Обновляем минимальное налоговое бремя
                selected[w] = selected[w - wt[i]]; // Копируем набор предметов для веса (w - wt[i])
                selected[w][i] = true; // Добавляем текущий предмет в набор
            }
        }
    }

    // Находим минимальное налоговое бремя для весов >= W
    int minVal = INT_MAX;
    int bestWeight = 0; // Вес, соответствующий минимальному налоговому бремени
    vector<bool> bestSelection(n, false); // Набор предметов, дающий минимальное налоговое бремя

    for (int w = W; w <= maxWeight; w++) // Перебираем все веса >= W
    { 
        if (dp[w] < minVal) // Если найдено лучшее решение
        { 
            minVal = dp[w]; // Обновляем минимальное налоговое бремя
            bestWeight = w; // Запоминаем вес
            bestSelection = selected[w]; // Запоминаем набор предметов
        }
    }

    // Вывод результата
    if (minVal == INT_MAX) // Если решение не найдено
    { 
        cout << "Невозможно достичь минимального веса " << W << endl;
    }
    else// Если решение найдено
    { 
        cout << "Порядковые номера выбранных предметов: ";
        for (int i = 0; i < n; i++) 
        {
            if (bestSelection[i]) 
            {
                cout << i + 1 << " ";
            }
        }
        cout << endl;

        // Выводим общий вес и итоговое налоговое бремя
        cout << "Общий вес: " << bestWeight << " кг" << endl;
        cout << "Итоговое налогообложение: " << minVal << endl;
    }
}

int main() {
    setlocale(LC_ALL, "russian");

    ifstream input("t.txt");

    if (!input.is_open()) {
        cout << "Ошибка открытия файла!" << endl;
    }

    int N, Z;
    input >> N >> Z; // Считываем количество предметов и минимальный вес Z

    vector<int> weights; // Вектор для хранения весов предметов
    vector<int> taxes; // Вектор для хранения налогового бремени предметов

    // Считываем веса предметов
    for (int i = 0; i < N; ++i) 
    {
        int value;
        input >> value;
        weights.push_back(value);
    }

    // Считываем налоговое бремя предметов
    for (int i = 0; i < N; ++i) 
    {
        int value;
        input >> value;
        taxes.push_back(value);
    }

    input.close();

    knapSack(Z, weights, taxes);
}