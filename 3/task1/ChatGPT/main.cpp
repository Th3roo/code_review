/* Продолжение задания «Случайные перестановки букв в слове до совпадения» */

#include <iostream>
#include <string>

#include "WordShuffler.h"

int main() {
        std::string input_word; // всегда инициализируем

        std::cout << "Введите слово: ";
        if (!(std::cin >> input_word)) {
                std::cerr << "Ошибка ввода.\n";
                return 1;
        }

        WordShuffler shuffler(input_word);

        if (!shuffler.IsValid()) {
                // Сообщение уже напечатано внутри конструктора
                return 1;
        }

        shuffler.ShuffleUntilOriginal();

        return 0;
}