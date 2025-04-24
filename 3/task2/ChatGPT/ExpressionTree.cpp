/* Продолжение задания «CalcTree3 — построение и преобразование дерева выражения» */

#include "ExpressionTree.h"

#include <cctype>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stack>

namespace {     // 1 tab
/**
 * @brief Создаёт новый узел и возвращает указатель на него.
 */
TreeNode* CreateNode(int value, TreeNode* left = nullptr, TreeNode* right = nullptr) {
    // значение создаваемого узла (операнд или операция)
    TreeNode* node = new (std::nothrow) TreeNode{value, left, right};
    if (node == nullptr) {      // проверка результатa new
        std::cerr << "Не удалось выделить память под узел дерева.\n";
    }
    return node;
}
}       // namespace

/* static */ bool ExpressionTree::TryParseNumber(const std::string& token, int& value) {
    // число должно состоять ровно из одной цифры 0..9
    return token.size() == 1 && std::isdigit(token[0]) != 0 && (value = token[0] - '0', true);
}

/* static */ bool ExpressionTree::TryParseOperator(const std::string& token, int& op_code) {
    if (token.size() != 1) {
        return false;
    }
    switch (token[0]) {
        case '+':       op_code = -1;   return true;
        case '-':       op_code = -2;   return true;
        case '*':       op_code = -3;   return true;
        case '/':       op_code = -4;   return true;
        case '%':       op_code = -5;   return true;
        default:                                        return false;
    }
}

/* static */ bool ExpressionTree::BuildFromFile(const std::string& filename, TreeNode*& root_root) {
    root_root = nullptr;        // инициализация выходного значения

    // Открываем файл
    std::ifstream fin(filename);
    if (!fin) {
        std::cerr << "Не удалось открыть файл: " << filename << '\n';
        return false;
    }

    // Читаем всё содержимое файла в строку
    std::ostringstream oss;
    oss << fin.rdbuf();
    fin.close();        // файл всегда закрываем

    std::istringstream iss(oss.str());
    std::stack<TreeNode*> st;   // стек для построения дерева

    std::string token;
    while (iss >> token) {
        int parsed_value = 0;
        if (TryParseNumber(token, parsed_value)) {
            // Операнд: создаём лист и кладём в стек
            TreeNode* leaf = CreateNode(parsed_value);
            if (leaf == nullptr) {
                // память не выделена — очищаем промежуточные узлы
                while (!st.empty()) {
                    FreeTree(st.top());
                    st.pop();
                }
                return false;
            }
            st.push(leaf);
            continue;
        }

        int op_code = 0;
        if (TryParseOperator(token, op_code)) {
            // Для операции нужны два операнда в стеке
            if (st.size() < 2U) {
                std::cerr << "Недостаточно операндов для операции '" << token << "'.\n";
                while (!st.empty()) {
                    FreeTree(st.top());
                    st.pop();
                }
                return false;
            }

            TreeNode* right = st.top(); st.pop();
            TreeNode* left  = st.top(); st.pop();
            TreeNode* op_node = CreateNode(op_code, left, right);
            if (op_node == nullptr) {
                FreeTree(left);
                FreeTree(right);
                while (!st.empty()) {
                    FreeTree(st.top());
                    st.pop();
                }
                return false;
            }
            st.push(op_node);
            continue;
        }

        std::cerr << "Неизвестный токен: " << token << '\n';
        while (!st.empty()) {
            FreeTree(st.top());
            st.pop();
        }
        return false;
    }

    if (st.size() != 1U) {
        std::cerr << "Некорректное выражение: стек после разбора не содержит ровно один элемент.\n";
        while (!st.empty()) {
            FreeTree(st.top());
            st.pop();
        }
        return false;
    }

    root_root = st.top();
    return true;
}

/* static */ int ExpressionTree::Evaluate(const TreeNode* node, bool& ok) {
    if (node == nullptr) {
        ok = false;
        return 0;
    }
    if (node->value >= 0) {
        // Лист — число
        ok = true;
        return node->value;
    }

    // Рекурсивно вычисляем левое и правое поддерево
    bool left_ok  = false;
    bool right_ok = false;
    int left_val  = Evaluate(node->left, left_ok);
    int right_val = Evaluate(node->right, right_ok);
    if (!left_ok || !right_ok) {
        ok = false;
        return 0;
    }

    switch (node->value) {
        case -1:        ok = true;      return left_val + right_val;
        case -2:        ok = true;      return left_val - right_val;
        case -3:        ok = true;      return left_val * right_val;
        case -4:
            if (right_val == 0) {
                std::cerr << "Ошибка: деление на 0.\n";
                ok = false;
                return 0;
            }
            ok = true;
            return left_val / right_val;
        case -5:
            if (right_val == 0) {
                std::cerr << "Ошибка: деление на 0.\n";
                ok = false;
                return 0;
            }
            ok = true;
            return left_val % right_val;
        default:
            ok = false;
            return 0;
    }
}

/* static */ TreeNode* ExpressionTree::RemoveMultiplication(TreeNode* node) {
    if (node == nullptr) {
        return nullptr;
    }

    // Если это узел умножения, то заменяем весь поддерево на лист-значение
    if (node->value == -3) {    // код '*'
        bool eval_ok = false;
        int  eval_val = Evaluate(node, eval_ok);
        if (!eval_ok) {
            // Не удалось вычислить (например, деление на 0 внутри) — оставляем как есть
            return node;
        }

        // Освобождаем детей и создаём новый лист
        FreeTree(node->left);
        FreeTree(node->right);
        node->left  = nullptr;
        node->right = nullptr;
        node->value = eval_val; // теперь это лист-число
        return node;
    }

    // Рекурсивно обрабатываем поддеревья
    node->left  = RemoveMultiplication(node->left);
    node->right = RemoveMultiplication(node->right);
    return node;
}

/* static */ void ExpressionTree::FreeTree(TreeNode* node) {
    if (node == nullptr) {
        return;
    }
    FreeTree(node->left);
    FreeTree(node->right);
    delete node;
}