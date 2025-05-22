/* Продолжение задания «Graf8 — поиск городов по количеству пересадок» */

#include "GraphAnalyzer.h"

#include <fstream>
#include <iostream>
#include <queue>

namespace {     // 1 tab
/**
 * @brief Проверяет значение матрицы (должно быть 0 или 1).
 */
bool IsValidCell(int v) {
        return v == 0 || v == 1;
}
}       // namespace

/* static */ bool GraphAnalyzer::LoadGraph(const std::string& filename,
                                                                                   std::vector<std::vector<int>>& m) {
        m.clear();      // гарантируем начальное состояние

        std::ifstream fin(filename);
        if (!fin) {
                std::cerr << "Не удалось открыть файл: " << filename << '\n';
                return false;
        }

        int n = 0;
        if (!(fin >> n)) {
                std::cerr << "Ошибка чтения количества городов.\n";
                fin.close();
                return false;
        }
        if (n <= 0 || n > kMaxCities) {
                std::cerr << "Некорректное количество городов (1.." << kMaxCities << ").\n";
                fin.close();
                return false;
        }

        m.assign(n, std::vector<int>(n, 0));    // инициализируем матрицу

        for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                        int cell = 0;
                        if (!(fin >> cell)) {
                                std::cerr << "Не удалось прочитать элемент матрицы [" << i << "][" << j << "].\n";
                                fin.close();
                                return false;
                        }
                        if (!IsValidCell(cell)) {
                                std::cerr << "Элемент матрицы должен быть 0 или 1.\n";
                                fin.close();
                                return false;
                        }
                        m[i][j] = cell;
                }
        }

        fin.close();    // явно закрываем файл
        return true;
}

/* static */ std::vector<int> GraphAnalyzer::FindCities(
        const std::vector<std::vector<int>>& graph,
        int k,
        int l) {

        std::vector<int> result;
        const int n = static_cast<int>(graph.size());

        // Проверка входных параметров
        if (n == 0 || k <= 0 || k > n || l < 0) {
                std::cerr << "Некорректные параметры поиска городов.\n";
                return result;
        }

        // BFS для поиска кратчайших путей (по числу перелётов = рёбер)
        const int kInf = 1'000'000;
        std::vector<int> dist(n, kInf);
        std::queue<int> q;

        // Приводим город к indexing 0-based
        const int start = k - 1;
        dist[start] = 0;
        q.push(start);

        while (!q.empty()) {
                int v = q.front();
                q.pop();

                for (int to = 0; to < n; ++to) {
                        if (graph[v][to] == 1 && dist[to] == kInf) {    // ребро существует и вершина не посещена
                                dist[to] = dist[v] + 1;
                                q.push(to);
                        }
                }
        }

        // Собираем города, удовлетворяющие условию
        for (int i = 0; i < n; ++i) {
                // Кол-во пересадок = кол-во рёбер – 1
                if (dist[i] != kInf && dist[i] - 1 >= l) {
                        result.push_back(i + 1);        // обратно к 1-based
                }
        }

        return result;  // уже отсортирован по возрастанию благодаря порядку обхода i
}

/* static */ void GraphAnalyzer::PrintCities(const std::vector<int>& cities) {
        if (cities.empty()) {
                std::cout << -1 << '\n';
                return;
        }

        for (std::size_t i = 0; i < cities.size(); ++i) {
                std::cout << cities[i];
                if (i + 1U < cities.size()) {
                        std::cout << ' ';
                }
        }
        std::cout << '\n';
}