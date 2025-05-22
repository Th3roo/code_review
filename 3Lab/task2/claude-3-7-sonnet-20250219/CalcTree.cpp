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

#include "CalcTree.h"
#include <iostream>
#include <fstream>
#include <stack>
#include <stdexcept>

std::string CalcTree::readRpnFromFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
                std::cerr << "Ошибка открытия файла: " << filename << std::endl;
                throw std::runtime_error("Невозможно открыть файл");
        }
        
        std::string rpnExpression;
        std::string line;
        
        while (std::getline(file, line)) {
                rpnExpression += line + " ";
        }
        
        file.close();
        
        return rpnExpression;
}

TreeNode* CalcTree::buildTree(const std::string& rpnExpression) {
        std::stack<TreeNode*> nodeStack;
        
        for (char c : rpnExpression) {
                if (c == ' ' || c == '\n' || c == '\t') {
                        continue; // Пропускаем пробельные символы
                }
                
                if (c >= '0' && c <= '9') {
                        // Операнд (0-9)
                        TreeNode* node = new TreeNode(c - '0');
                        nodeStack.push(node);
                } else {
                        // Оператор (+, -, *, /, %)
                        if (nodeStack.size() < 2) {
                                std::cerr << "Ошибка: некорректное выражение в ОПЗ - недостаточно операндов для оператора" << std::endl;
                                throw std::invalid_argument("Некорректное выражение в ОПЗ");
                        }
                        
                        TreeNode* rightChild = nodeStack.top();
                        nodeStack.pop();
                        TreeNode* leftChild = nodeStack.top();
                        nodeStack.pop();
                        
                        TreeNode* operatorNode = nullptr;
                        
                        switch (c) {
                                case '+':
                                        operatorNode = new TreeNode(-1);
                                        break;
                                case '-':
                                        operatorNode = new TreeNode(-2);
                                        break;
                                case '*':
                                        operatorNode = new TreeNode(-3);
                                        break;
                                case '/':
                                        operatorNode = new TreeNode(-4);
                                        break;
                                case '%':
                                        operatorNode = new TreeNode(-5);
                                        break;
                                default:
                                        std::cerr << "Ошибка: неизвестный оператор '" << c << "'" << std::endl;
                                        throw std::invalid_argument("Неизвестный оператор");
                        }
                        
                        operatorNode->left = leftChild;
                        operatorNode->right = rightChild;
                        nodeStack.push(operatorNode);
                }
        }
        
        if (nodeStack.size() != 1) {
                std::cerr << "Ошибка: некорректное выражение в ОПЗ - слишком много операндов" << std::endl;
                throw std::invalid_argument("Некорректное выражение в ОПЗ");
        }
        
        return nodeStack.top();
}

int CalcTree::evaluateSubtree(TreeNode* node) {
        if (!node) {
                std::cerr << "Ошибка: попытка вычислить значение пустого поддерева" << std::endl;
                throw std::invalid_argument("Попытка вычислить значение пустого поддерева");
        }
        
        // Если это листовой узел (операнд), возвращаем его значение
        if (!node->left && !node->right) {
                return node->value;
        }
        
        // Вычисляем значения левого и правого поддеревьев
        int leftValue = evaluateSubtree(node->left);
        int rightValue = evaluateSubtree(node->right);
        
        // Выполняем операцию в соответствии со значением узла
        switch (node->value) {
                case -1: // Сложение
                        return leftValue + rightValue;
                case -2: // Вычитание
                        return leftValue - rightValue;
                case -3: // Умножение
                        return leftValue * rightValue;
                case -4: // Деление нацело
                        if (rightValue == 0) {
                                std::cerr << "Ошибка: деление на ноль" << std::endl;
                                throw std::invalid_argument("Деление на ноль");
                        }
                        return leftValue / rightValue;
                case -5: // Остаток от деления
                        if (rightValue == 0) {
                                std::cerr << "Ошибка: деление на ноль (остаток)" << std::endl;
                                throw std::invalid_argument("Деление на ноль (остаток)");
                        }
                        return leftValue % rightValue;
                default:
                        std::cerr << "Ошибка: неизвестная операция с кодом " << node->value << std::endl;
                        throw std::invalid_argument("Неизвестная операция");
        }
}

TreeNode* CalcTree::eliminateMultiplication(TreeNode* root) {
        if (!root) {
                return nullptr;
        }
        
        // Рекурсивно преобразуем левое и правое поддеревья (обход в глубину)
        root->left = eliminateMultiplication(root->left);
        root->right = eliminateMultiplication(root->right);
        
        // Если текущий узел - операция умножения
        if (root->value == -3) {
                // Вычисляем значение всего поддерева с корнем в текущем узле
                int result = evaluateSubtree(root);
                
                // Очищаем левое и правое поддеревья
                cleanupTree(root->left);
                cleanupTree(root->right);
                
                // Заменяем текущий узел листовым узлом с вычисленным значением
                root->value = result;
                root->left = nullptr;
                root->right = nullptr;
        }
        
        return root;
}

void CalcTree::displayTree(TreeNode* node, int level) {
        if (!node) {
                return;
        }
        
        displayTree(node->right, level + 1);
        
        for (int i = 0; i < level; ++i) {
                std::cout << "    ";
        }
        
        if (node->value >= 0) {
                std::cout << node->value << std::endl;
        } else {
                char op;
                switch (node->value) {
                        case -1: op = '+'; break;
                        case -2: op = '-'; break;
                        case -3: op = '*'; break;
                        case -4: op = '/'; break;
                        case -5: op = '%'; break;
                        default: op = '?'; break;
                }
                std::cout << op << std::endl;
        }
        
        displayTree(node->left, level + 1);
}

void CalcTree::cleanupTree(TreeNode* node) {
        if (!node) {
                return;
        }
        
        cleanupTree(node->left);
        cleanupTree(node->right);
        
        delete node;
}