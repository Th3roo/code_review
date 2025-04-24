/* Продолжение задания «Graf8 — поиск городов по количеству пересадок» */

#ifndef GRAPH_ANALYZER_H_
#define GRAPH_ANALYZER_H_

#include <string>
#include <vector>

/**
 * @brief Статический класс-утилита для чтения графа и поиска городов,
 *        до которых минимальный путь содержит не менее L пересадок.
 */
class GraphAnalyzer {
public: // 1 tab
        /**
         * @brief Загружает ориентированный граф из файла в виде матрицы смежности.
         *
         * @param filename  Имя текстового файла.
         * @param[out] m    Заполненная матрица смежности (n × n).
         * @return true, если файл прочитан и корректен; false иначе.
         */
        static bool LoadGraph(const std::string& filename, std::vector<std::vector<int>>& m);

        /**
         * @brief Находит номера городов, удовлетворяющих условию задачи.
         *
         * @param graph Матрица смежности.
         * @param k             Номер стартового города (1-based).
         * @param l             Минимальное требуемое число пересадок.
         * @return Отсортированный по возрастанию список подходящих городов
         *         или пустой вектор, если городов нет.
         */
        static std::vector<int> FindCities(const std::vector<std::vector<int>>& graph,
                                           int k,
                                           int l);

        /**
         * @brief Выводит список городов в формате задачи.
         *
         * @param cities        Вектор номеров городов (1-based).  
         *                 Если вектор пуст, выводится ‑1.
         */
        static void PrintCities(const std::vector<int>& cities);

private:        // 1 tab
        static constexpr int kMaxCities = 15;   // Ограничение из условия
};

#endif  // GRAPH_ANALYZER_H_