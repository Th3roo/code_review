/* 
 * Задание: Ввести с клавиатуры любое слово. Используя генерацию случайных чисел, переставить
 * буквы этого слова в случайном порядке. Делать это до тех пор, пока полученное слово не совпадёт
 * с начальным словом. Выводить слово после каждой перестановки и посчитать общее количество
 * выведенных слов (не считая исходного).
 */

#include "WordShuffler.h"
#include <iostream>
#include <algorithm>
#include <random>

bool WordShuffler::validateWord(const std::string& word) {
        // Check if the word is empty
        if (word.empty()) {
                return false;
        }
        
        // Check if the word contains only letters
        for (const char& c : word) {
                if (!std::isalpha(c)) {
                        return false;
                }
        }
        
        return true;
}

std::string WordShuffler::shuffleWord(const std::string& word) {
        // Create a copy of the original word
        std::string shuffled = word;
        
        // Use a random device for seed
        std::random_device rd;
        // Mersenne Twister random number generator
        std::mt19937 g(rd());
        
        // Shuffle the word
        std::shuffle(shuffled.begin(), shuffled.end(), g);
        
        return shuffled;
}

int WordShuffler::runShuffling(const std::string& originalWord) {
        int attempts = 0;
        std::string shuffledWord;
        
        do {
                // Shuffle the original word
                shuffledWord = shuffleWord(originalWord);
                std::cout << shuffledWord << std::endl;
                attempts += 1;
        } while (shuffledWord != originalWord);
        
        return attempts;
}