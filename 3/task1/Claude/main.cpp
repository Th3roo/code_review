/* 
 * Задание: Ввести с клавиатуры любое слово. Используя генерацию случайных чисел, переставить
 * буквы этого слова в случайном порядке. Делать это до тех пор, пока полученное слово не совпадёт
 * с начальным словом. Выводить слово после каждой перестановки и посчитать общее количество
 * выведенных слов (не считая исходного).
 */

#include <iostream>
#include <string>
#include "WordShuffler.h"

int main() {
        WordShuffler shuffler;
        std::string word;
        
        // Input with validation
        do {
                std::cout << "Введите слово: ";
                std::cin >> word;
                
                if (!shuffler.validateWord(word)) {
                        std::cerr << "Ошибка: введите корректное слово, содержащее только буквы." << std::endl;
                }
        } while (!shuffler.validateWord(word));
        
        // Run the shuffling simulation
        int attempts = shuffler.runShuffling(word);
        
        std::cout << attempts << " попыток" << std::endl;
        
        return 0;
}