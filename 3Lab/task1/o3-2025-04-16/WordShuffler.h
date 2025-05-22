/* Продолжение задания «Случайные перестановки букв в слове до совпадения» */

#ifndef WORD_SHUFFLER_H_
#define WORD_SHUFFLER_H_

#include <random>
#include <string>

/**
 * @brief Класс, инкапсулирующий логику перестановки символов слова.
 */
class WordShuffler {
public: // 1 tab
 
        /**
         * @brief Конструктор.
         * @param source_word Слово, которое требуется перемешивать.
         *
         * Если входное слово некорректно, объект переходит в невалидное состояние,
         * что можно проверить методом IsValid().
         */
        explicit WordShuffler(const std::string& source_word);
 
        /**
         * @brief Проверяет, является ли объект валидным.
         * @return true, если слово корректно и возможно перемешивание; false иначе.
         */
        bool IsValid() const;
 
        /**
         * @brief Перемешивает буквы слова до тех пор, пока не получится исходное слово.
         *
         * После каждой перестановки слово выводится на экран.  
         * По завершении выводится количество выведенных слов
         * (без учёта слова, введённого пользователем).
         */
        void ShuffleUntilOriginal();
 
private:        // 1 tab
 
        /**
         * @brief Выполняет одну случайную перестановку символов в word.
         * @param word Слово, которое требуется перемешать.
         */
        static void ShuffleWord(std::string& word);
 
        /**
         * @brief Проверяет исходное слово на простейшие ошибки ввода:
         *        пустая строка или наличие пробельных символов.
         * @param word Проверяемое слово.
         * @return true, если проверка пройдена; false иначе.
         */
        static bool ValidateInput(const std::string& word);
 
        std::string     original_word;  // Исходное слово
        std::mt19937    rng;                    // Генератор случайных чисел
};

#endif  // WORD_SHUFFLER_H_