//Fix Me задача не по шаблону
/*Археолог нашел N артефактов.Известны веса(сi) и налоговое бремя(di) находок.
* Нужно выбрать такое подмножество находок, чтобы их суммарный вес превысил Z кг, а их общее 
* налоговое бремя оказалось минимальным.Известно, что решение единственно.Укажите
* порядковые номера вещей, которые нужно взять.Исходный данные находятся в текстовом файле, 
* в первой строке указаны N и Z, а во второй строке значения весов(в кг), в третьей - величина
* налога по каждой находке.Вывести так же суммарный вес и общую ценность результата.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <climits>

using namespace std;

// Функция для решения задачи о рюкзаке
// FIX ME названия перменных однобуквенные
void KnapsackSolver(int weight_threshold, const vector<int>& weights, const vector<int>& tax_burdens) {
    int item_count = weights.size();
    int total_possible_weight = 0;
    for (int w : weights) total_possible_weight += w;
    vector<int> min_tax_for_weight(total_possible_weight + 1, INT_MAX);
    min_tax_for_weight[0] = 0;

    vector<vector<bool>> selected_items_for_weight(total_possible_weight + 1, vector<bool>(item_count, false));

    for (int i = 0; i < item_count; i++) {
        for (int current_weight = total_possible_weight; current_weight >= weights[i]; current_weight--)
        { 
            int weight_before_adding_item = current_weight - weights[i];
            if (min_tax_for_weight[weight_before_adding_item] != INT_MAX &&
                min_tax_for_weight[weight_before_adding_item] + tax_burdens[i] < min_tax_for_weight[current_weight])
            {
                min_tax_for_weight[current_weight] = min_tax_for_weight[weight_before_adding_item] + tax_burdens[i];
                selected_items_for_weight[current_weight] = selected_items_for_weight[weight_before_adding_item];
                selected_items_for_weight[current_weight][i] = true;
            }
        }
    }

    int min_total_tax_found = INT_MAX;
    int weight_for_min_tax = 0;
    vector<bool> selection_for_min_tax(item_count, false);

    //FIX ME фигурные скобки
    for (int current_weight = weight_threshold; current_weight <= total_possible_weight; current_weight++) { 
        if (min_tax_for_weight[current_weight] < min_total_tax_found)
        { 
            min_total_tax_found = min_tax_for_weight[current_weight];
            weight_for_min_tax = current_weight;
            selection_for_min_tax = selected_items_for_weight[current_weight];
        }
    }

    // Вывод результата
    if (min_total_tax_found == INT_MAX) // Если решение не найдено
    { 
        cout << "Невозможно достичь минимального веса " << weight_threshold << endl;
    }
    else// Если решение найдено
    { 
        cout << "Порядковые номера выбранных предметов: ";
        for (int i = 0; i < item_count; i++) 
        {
            if (selection_for_min_tax[i]) 
            {
                cout << i + 1 << " ";
            }
        }
        cout << endl;

        cout << "Общий вес: " << weight_for_min_tax << " кг" << endl;
        cout << "Итоговое налогообложение: " << min_total_tax_found << endl;
    }
}

int main() {
    setlocale(LC_ALL, "russian");

    ifstream input("input.txt");

    if (!input.is_open()) {
        cout << "Ошибка открытия файла!" << endl;
        return 1;
    }

    int item_count_n, min_weight_z;
    input >> item_count_n >> min_weight_z;

    vector<int> weights;
    vector<int> taxes;

    // Считываем веса предметов
    for (int i = 0; i < item_count_n; ++i) {
        int temp_value;
        input >> temp_value;
        weights.push_back(temp_value);
    }

    // Считываем налоговое бремя предметов
    for (int i = 0; i < item_count_n; ++i) {
        int temp_value;
        input >> temp_value;
        taxes.push_back(temp_value);
    }

    input.close();

    KnapsackSolver(min_weight_z, weights, taxes);

    return 0;
}