/* Продолжение задания «Graf8 — поиск городов по количеству пересадок» */

#include <iostream>
#include <string>
#include <vector>

#include "GraphAnalyzer.h"

int main() {
        std::string filename;
        int k = 0;      // стартовый город
        int l = 0;      // минимальное число пересадок

        std::cout << "Введите имя файла с матрицей: ";
        if (!(std::cin >> filename)) {
                std::cerr << "Ошибка ввода имени файла.\n";
                return 1;
        }

        std::cout << "Введите номер города K и минимальное число пересадок L: ";
        if (!(std::cin >> k >> l)) {
                std::cerr << "Ошибка ввода значений K и L.\n";
                return 1;
        }

        std::vector<std::vector<int>> graph;
        if (!GraphAnalyzer::LoadGraph(filename, graph)) {
                // Подробности ошибки уже выведены
                return 1;
        }

        std::vector<int> cities = GraphAnalyzer::FindCities(graph, k, l);
        GraphAnalyzer::PrintCities(cities);

        return 0;
}