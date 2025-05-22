/*
 * Graf8. Юный путешественник решил изучить схему авиационного сообщения. Схема авиационного
 * сообщения задана в текстовом файле с именем FileName в виде матрицы смежности. Первая
 * строка файла содержит количество городов (n) n<=15, связанных авиационным сообщением, а
 * следующие n строк хранят матрицу (m), m[i][j]=0, если не имеется возможности перелета из города
 * i в город j, иначе m[i][j]=1. Определить номера городов, в которые из города K можно долететь
 * не менее чем с L пересадками и более коротких путей к таким городам не существует. Перечислите
 * номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
 * таких городов нет, выведите число (-1).
 */

#include "Graf.h"
#include <fstream>
#include <queue>
#include <algorithm>
#include <iostream>

Graph::Graph() : numCities(0) {
}

bool Graph::readFromFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
                std::cerr << "Ошибка: не удалось открыть файл " << filename << std::endl;
                return false;
        }
        
        file >> numCities;
        if (numCities <= 0 || numCities > 15) {
                std::cerr << "Ошибка: некорректное количество городов" << std::endl;
                file.close();
                return false;
        }
        
        // Инициализация матрицы смежности
        adjacencyMatrix.resize(numCities, std::vector<int>(numCities, 0));
        
        // Чтение матрицы смежности
        for (int i = 0; i < numCities; ++i) {
                for (int j = 0; j < numCities; ++j) {
                        if (!(file >> adjacencyMatrix[i][j])) {
                                std::cerr << "Ошибка: некорректный формат данных в файле" << std::endl;
                                file.close();
                                return false;
                        }
                        
                        // Проверка значений матрицы (должны быть 0 или 1)
                        if (adjacencyMatrix[i][j] != 0 && adjacencyMatrix[i][j] != 1) {
                                std::cerr << "Ошибка: матрица должна содержать только 0 и 1" << std::endl;
                                file.close();
                                return false;
                        }
                }
        }
        
        file.close();
        return true;
}

std::vector<int> Graph::findCitiesWithExactTransfers(int k, int l) {
        // Преобразуем номер города из 1-based в 0-based
        int cityIndex = k - 1;
        
        // Проверка корректности входных данных
        if (cityIndex < 0 || cityIndex >= numCities || l < 0) {
                return std::vector<int>();
        }
        
        std::vector<int> result;
        std::vector<int> distances(numCities, -1); // -1 означает, что город недостижим
        
        // Используем BFS для нахождения кратчайших путей
        std::queue<int> q;
        q.push(cityIndex);
        distances[cityIndex] = 0; // Расстояние до исходного города равно 0
        
        while (!q.empty()) {
                int current = q.front();
                q.pop();
                
                for (int next = 0; next < numCities; ++next) {
                        if (adjacencyMatrix[current][next] == 1 && distances[next] == -1) {
                                distances[next] = distances[current] + 1;
                                q.push(next);
                        }
                }
        }
        
        // Находим города, удовлетворяющие условию:
        // - Количество пересадок равно L (длина пути равна L+1)
        for (int i = 0; i < numCities; ++i) {
                // Если город достижим, не совпадает с исходным и количество пересадок равно L
                if (i != cityIndex && distances[i] != -1 && distances[i] - 1 == l) {
                        result.push_back(i + 1); // Возвращаем номера в 1-based формате
                }
        }
        
        // Сортируем результат по возрастанию
        std::sort(result.begin(), result.end());
        
        return result;
}

int Graph::getNumCities() const {
        return numCities;
}