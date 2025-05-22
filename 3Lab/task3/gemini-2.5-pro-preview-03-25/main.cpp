/* Задание Graf8: Найти города, достижимые из K ровно за L пересадок,
   причем более короткого пути до них не существует. */
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <limits>   // For numeric_limits
#include <cstdlib>  // For EXIT_SUCCESS, EXIT_FAILURE
#include <algorithm> // For std::all_of (optional matrix validation)

#include "GraphSolver.h" // Include our header

// Allow using namespace std in .cpp files
using namespace std;

/**
 * @brief Reads graph data (n, matrix) and query parameters (K, L) from a file.
 * @param filename The name of the input file.
 * @param[out] graphData The structure to populate with read data.
 * @param[out] k The starting city K (1-based).
 * @param[out] l The required transfers L.
 * @return true if reading and basic validation succeed, false otherwise.
 *         Errors are printed to std::cerr.
 */
bool readInput(const string& filename, GraphData& graphData, int& k, int& l) {
	ifstream inputFile(filename);
	if (!inputFile.is_open()) {
		cerr << "Ошибка: Не удалось открыть файл '" << filename << "'" << endl;
		return false;
	}

	// --- Read N ---
	if (!(inputFile >> graphData.n) || graphData.n <= 0 || graphData.n > 15) {
		cerr << "Ошибка: Неверное или недопустимое значение N (количество городов)." << endl;
		inputFile.close();
		return false;
	}

	// --- Read Adjacency Matrix ---
	graphData.adjMatrix.assign(graphData.n, vector<int>(graphData.n, 0)); // Resize and initialize
	int value = 0;
	for (int i = 0; i < graphData.n; ++i) {
		for (int j = 0; j < graphData.n; ++j) {
			if (!(inputFile >> value) || (value != 0 && value != 1)) {
				cerr << "Ошибка: Неверное значение в матрице смежности в строке "
					 << (i + 1) << ", столбце " << (j + 1) << "." << endl;
				inputFile.close();
				return false;
			}
			graphData.adjMatrix[i][j] = value;
		}
	}

    // --- Read K and L (assuming they are at the end of the file or on the next line) ---
    // Let's assume they are read from standard input as per typical competitive programming style,
    // unless explicitly stated to be in the file AFTER the matrix.
    // If K and L are in the file, add:
    // if (!(inputFile >> k) || !(inputFile >> l)) { ... error ... }

    // Assume K and L are read from console:
    cout << "Введите начальный город K (1-" << graphData.n << "): ";
    if (!(cin >> k) || k < 1 || k > graphData.n) {
        cerr << "Ошибка: Неверное значение для K." << endl;
        cin.clear(); // Clear error flags
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard bad input
        inputFile.close(); // Close the file stream
        return false;
    }

    cout << "Введите необходимое количество пересадок L (>=0): ";
    if (!(cin >> l) || l < 0) {
        cerr << "Ошибка: Неверное значение для L." << endl;
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        inputFile.close(); // Close the file stream
        return false;
    }

	// Assign K and L to graphData structure as well
	graphData.startCityK = k;
	graphData.requiredTransfersL = l;

	inputFile.close(); // Ensure file is closed
	return true;
}

/**
 * @brief Главная функция программы Graf8.
 *        Читает данные из файла, вызывает решатель и выводит результат.
 * @param argc Количество аргументов командной строки (не используется).
 * @param argv Вектор аргументов командной строки (не используется).
 * @return EXIT_SUCCESS при успехе, EXIT_FAILURE при ошибке.
 */
int main(int argc, char* argv[]) {
	// Имя файла с данными графа (согласно заданию "FileName")
	const string inputFilename = "input.txt"; // Используем фиксированное имя файла

	GraphData graphData;
    int k_in = 0; // Variable to read K into
    int l_in = 0; // Variable to read L into

	// --- Чтение и валидация входных данных ---
	if (!readInput(inputFilename, graphData, k_in, l_in)) {
		// Сообщение об ошибке уже выведено функцией readInput
		return EXIT_FAILURE;
	}

	// --- Вызов решателя ---
	vector<int> result = findCitiesWithExactTransfers(graphData);

	// --- Вывод результата ---
	if (result.empty()) {
		cout << -1 << endl; // Выводим -1, если таких городов нет
	} else {
		// Выводим номера городов через пробел
		for (size_t i = 0; i < result.size(); ++i) {
			cout << result[i] << (i == result.size() - 1 ? "" : " ");
		}
		cout << endl;
	}

	return EXIT_SUCCESS;
}