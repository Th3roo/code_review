#ifndef SOLVE_LAME_KING_H
#define SOLVE_LAME_KING_H

#include <vector>
#include <string>
#include <utility> // std::pair

using namespace std;

pair<vector<vector<int>>, bool> readBoardFromFile(const string& filename);

pair<int, string> solveLameKing(const vector<vector<int>>& board);

bool writeResultToFile(const string& filename, int maximumSum, const string& path);

#endif // SOLVE_LAME_KING_H
