/*
 * CalcTree3. В текстовом файле с именем filename дано арифметическое выражение в обратной
 * польской записи. Операндами в выражении являются целые числа из промежутка от 0 до 9. Используемые
 * операции: сложение(+), вычитание(-), умножение(*), деление нацело (/) и целочисленный остаток
 * от деления (%). Постройте дерево, соответствующее данному выражению. Знаки операций кодируйте
 * числами: сложение (-1), вычитание (-2), умножение (-3), деление нацело (-4) и целочисленный
 * остаток от деления (-5). Преобразуйте дерево так, чтобы в нем не было операции умножения
 * (замените поддеревья, в которых есть умножение значением данного поддерева). Выведите указатель
 * на корень полученного дерева.
 */

#include <iostream>
#include <string>
#include "CalcTree.h"

int main() {
        CalcTree calcTree;
        std::string filename;
        
        std::cout << "Введите имя файла с выражением в ОПЗ: ";
        std::cin >> filename;
        
        try {
                // Считываем выражение из файла
                std::string rpnExpression = calcTree.readRpnFromFile(filename);
                std::cout << "Прочитано выражение в ОПЗ: " << rpnExpression << std::endl;
                
                // Строим дерево выражения
                TreeNode* root = calcTree.buildTree(rpnExpression);
                
                std::cout << "\nИсходное дерево выражения:" << std::endl;
                calcTree.displayTree(root);
                
                // Преобразуем дерево, устраняя операции умножения
                TreeNode* transformedRoot = calcTree.eliminateMultiplication(root);
                
                std::cout << "\nПреобразованное дерево (без операций умножения):" << std::endl;
                calcTree.displayTree(transformedRoot);
                
                std::cout << "\nУказатель на корень преобразованного дерева: " << transformedRoot << std::endl;
                
                // Очищаем память
                calcTree.cleanupTree(transformedRoot);
                
        } catch (const std::exception& e) {
                std::cerr << "Ошибка: " << e.what() << std::endl;
                return 1;
        }
        
        return 0;
}