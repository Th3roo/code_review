/* Продолжение задания «CalcTree3 — построение и преобразование дерева выражения» */

#include <iostream>
#include <string>

#include "ExpressionTree.h"

int main() {
    std::string filename;

    std::cout << "Введите имя файла: ";
    if (!(std::cin >> filename)) {
        std::cerr << "Ошибка ввода имени файла.\n";
        return 1;
    }

    TreeNode* root = nullptr;   // инициализация

    if (!ExpressionTree::BuildFromFile(filename, root)) {
        // Сообщения об ошибках уже выведены внутри функции
        return 1;
    }

    // Преобразуем дерево, устраняя умножение
    root = ExpressionTree::RemoveMultiplication(root);

    // Выводим указатель на корень
    std::cout << "Указатель на корень полученного дерева: " << root << '\n';

    // Освобождаем выделенную память
    ExpressionTree::FreeTree(root);
    return 0;
}