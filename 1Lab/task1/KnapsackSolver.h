/*Археолог нашел N артефактов.Известны веса(сi) и налоговое бремя(di) находок.
* Нужно выбрать такое подмножество находок, чтобы их суммарный вес превысил Z кг, а их общее 
* налоговое бремя оказалось минимальным.Известно, что решение единственно.Укажите
* порядковые номера вещей, которые нужно взять.Исходный данные находятся в текстовом файле, 
* в первой строке указаны N и Z, а во второй строке значения весов(в кг), в третьей - величина
* налога по каждой находке.Вывести так же суммарный вес и общую ценность результата.
*/
#ifndef KNAPSACK_SOLVER_H
#define KNAPSACK_SOLVER_H

#include <vector> // Needed for vector type in function signature

// Function declaration
void FindMinTaxForWeightThreshold(int weight_threshold, const std::vector<int>& weights, const std::vector<int>& tax_burdens);

#endif // KNAPSACK_SOLVER_H