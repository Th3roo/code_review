/* Продолжение задания «Случайные перестановки букв в слове до совпадения» */

#include "WordShuffler.h"

#include <algorithm>    // std::shuffle
#include <chrono>
#include <iostream>

/* static */ bool WordShuffler::ValidateInput(const std::string& word) {
        // Слово не должно быть пустым и не должно содержать пробелы
        return !word.empty() && word.find_first_of(" \t\n\r") == std::string::npos;
}

WordShuffler::WordShuffler(const std::string& source_word)
        : original_word(source_word)    // инициализация исходным словом
        , rng(static_cast<std::mt19937::result_type>(
                std::chrono::steady_clock::now().time_since_epoch().count())) {
        // Проверяем входные данные
        if (!ValidateInput(source_word)) {
                std::cerr << "Ошибка: введено пустое слово или содержатся пробельные символы.\n";
                original_word.clear();  // делаем объект невалидным
        }
}

/* static */ void WordShuffler::ShuffleWord(std::string& word) {
        // Используем std::shuffle и передаём итераторы контейнера
        // auto - ожидаемый тип: std::string::iterator
        auto first = word.begin();                      // NOLINT
        auto last  = word.end();                        // NOLINT
        std::shuffle(first, last, std::mt19937{
                static_cast<std::mt19937::result_type>(
                        std::chrono::steady_clock::now().time_since_epoch().count())});
}

bool WordShuffler::IsValid() const {
        return !original_word.empty();
}

void WordShuffler::ShuffleUntilOriginal() {
        if (!IsValid()) {
                std::cerr << "Невозможно выполнить перестановку: объект в невалидном состоянии.\n";
                return;
        }

        std::string current_word = original_word;       // копия для работы
        std::size_t attempts     = 0;                           // счётчик выведенных слов

        do {
                ShuffleWord(current_word);                              // случайная перестановка
                ++attempts;                                                             // i += 1 запрещён, ++attempts ок
                std::cout << current_word << '\n';
        } while (current_word != original_word);

        std::cout << attempts << " попыток\n";
}