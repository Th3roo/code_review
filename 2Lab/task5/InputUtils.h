#ifndef INPUT_UTILS_H
#define INPUT_UTILS_H

#include <deque>
#include <string>

bool FuncKeyboard(std::deque<int>& outputDeque);

bool FuncRandom(std::deque<int>& outputDeque, int elementCount);

bool FuncFile(std::deque<int>& outputDeque, const std::string& sourceFilename = "a.txt");

#endif // INPUT_UTILS_H 