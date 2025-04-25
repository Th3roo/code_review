/* 
 * Задание: Ввести с клавиатуры любое слово. Используя генерацию случайных чисел, переставить
 * буквы этого слова в случайном порядке. Делать это до тех пор, пока полученное слово не совпадёт
 * с начальным словом. Выводить слово после каждой перестановки и посчитать общее количество
 * выведенных слов (не считая исходного).
 */

#ifndef WORD_SHUFFLER_H
#define WORD_SHUFFLER_H

#include <string>

/**
 * Class for shuffling words randomly until the original word is found again.
 */
class WordShuffler {
public:
        /**
         * Validates that the input is a valid word.
         * 
         * @param word The word to validate
         * @return True if the word is valid, false otherwise
         */
        bool validateWord(const std::string& word);
        
        /**
         * Shuffles a word randomly.
         * 
         * @param word The word to shuffle
         * @return The shuffled word
         */
        std::string shuffleWord(const std::string& word);
        
        /**
         * Runs the shuffling simulation until the original word is found.
         * Prints each shuffled word and counts the number of attempts.
         * 
         * @param originalWord The original word to start with
         * @return The number of attempts made until finding the original word
         */
        int runShuffling(const std::string& originalWord);
};

#endif // WORD_SHUFFLER_H