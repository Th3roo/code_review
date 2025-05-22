//FIX ME задача не по шаблону
/*Хромой король.На квадратной доске расставлены монеты, достоинством от 1 до
* 100. Хромой король, находящийся в правом нижнем углу, мечтает попасть в левый верхний.
* При этом он может передвигаться только в клетку слева или сверху и хочет, чтобы сумма всех
* монет, оказавшихся у него на пути, была бы максимальной.Определить эту сумму и путь, каким
* образом должен двигаться король, чтобы ее собрать.Ввод и вывод организовать при помощи
* текстовых файлов.Формат входных данных : в первой строке входного файла записано число N
* - размер доски(1 < N < 80).Далее следует N строк, каждая из которых содержит N целых чисел,
* представляющих доску.В первую строку выходного файл нужно вывести единственное число :
* максимальную сумму, а во второй строке вывести путь в виде строки символов, обозначив символом L 
* движение влево, а символом U - движение вверх.
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm> // std::max
#include <utility>   // std::pair
#include "solveLameKing.h"

using namespace std;

pair<vector<vector<int>>, bool> readBoardFromFile(const string& filename) {
    //FIX ME нет проверки на открытие файлов
    ifstream inputFile(filename);
    if (!inputFile.is_open()) {
        cerr << "Error: Could not open input file " << filename << endl;
        return {{}, false};
    }

    // FIX ME названия переменных
    int boardSize;
    if (!(inputFile >> boardSize)) {
         cerr << "Error: Could not read board size from file." << endl;
         inputFile.close();
         return {{}, false};
    }

    //FIX ME нет проверки на валидность входных данных
    if (boardSize <= 1 || boardSize >= 80) {
         cerr << "Error: Board size N must be between 2 and 79 (inclusive)." << endl;
         inputFile.close();
         return {{}, false};
    }

    // FIX ME названия переменных
    vector<vector<int>> board(boardSize, vector<int>(boardSize));

    // Read the board from the file
    for (int i = 0; i < boardSize; ++i) {
        for (int j = 0; j < boardSize; ++j) {
            if (!(inputFile >> board[i][j])) {
                 cerr << "Error: Invalid format or insufficient data in input file." << endl;
                 inputFile.close();
                 return {{}, false}; // Return empty board and failure flag
            }
        }
    }

    inputFile.close();
    return {board, true}; // Return board and success flag
}

pair<int, string> solveLameKing(const vector<vector<int>>& board) {
    if (board.empty() || board[0].empty()) {
         cerr << "Internal Error: solveLameKing called with empty board." << endl;
         return {0, ""};
    }
    int boardSize = board.size();

    // FIX ME названия переменных
    vector<vector<int>> maxSums(boardSize, vector<int>(boardSize, 0));

    // Starting position (bottom-right corner)
    maxSums[boardSize - 1][boardSize - 1] = board[boardSize - 1][boardSize - 1];

    // Fill the DP table from bottom-right towards top-left
    // Fill the last row and last column first
    for (int i = boardSize - 2; i >= 0; --i) {
        maxSums[i][boardSize - 1] = maxSums[i + 1][boardSize - 1] + board[i][boardSize - 1]; // Move up
        maxSums[boardSize - 1][i] = maxSums[boardSize - 1][i + 1] + board[boardSize - 1][i]; // Move left
    }

    // Fill the rest of the DP table
    for (int i = boardSize - 2; i >= 0; --i) {
        for (int j = boardSize - 2; j >= 0; --j) {
             maxSums[i][j] = board[i][j] + max(maxSums[i + 1][j], maxSums[i][j + 1]);
        }
    }

    // FIX ME названия переменных
    int maximumSum = maxSums[0][0];

    /* КТО ВООБЩЕ ДЕЛАЕТ ВЕКТОР CHAR? */
    //FIX ME переделана логика для работы со строкой

    // Reconstruct the path from top-left (0, 0)
    string path = "";
    int currentRow = 0, currentCol = 0;
    while (currentRow < boardSize - 1 || currentCol < boardSize - 1) {
        if (currentRow == boardSize - 1) {
            path += 'L'; // Moving left
            currentCol++;
        } else if (currentCol == boardSize - 1) {
            path += 'U'; // Moving up
            currentRow++;
        } else if (maxSums[currentRow + 1][currentCol] > maxSums[currentRow][currentCol + 1]) {
            path += 'U';
            currentRow++;
        } else {
            path += 'L';
            currentCol++;
        }
    }

    return {maximumSum, path};
}

bool writeResultToFile(const string& filename, int maximumSum, const string& path) {
    //FIX ME нет проверки на открытие файлов
    ofstream outputFile(filename);
    if (!outputFile.is_open()) {
        cerr << "Error: Could not open output file " << filename << endl;
        return false; // Return false on failure
    }

    outputFile << maximumSum << endl;
    outputFile << path << endl;

    outputFile.close();
    return true; // Return true on success
}


int main() {
    // FIX ME названия переменных
    const string inputFilename = "a.txt";
    const string outputFilename = "b.txt"; 

    pair<vector<vector<int>>, bool> readResult = readBoardFromFile(inputFilename);

    if (!readResult.second) {
        return 1;
    }

    vector<vector<int>> board = readResult.first;
    pair<int, string> result = solveLameKing(board);

    if (!writeResultToFile(outputFilename, result.first, result.second)) {
         return 1;
    }

    return 0;
}
