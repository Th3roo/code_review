/* Продолжение задания «CalcTree3 — построение и преобразование дерева выражения» */

#ifndef EXPRESSION_TREE_H_
#define EXPRESSION_TREE_H_

#include <string>
#include <vector>

/**
 * @brief Узел бинарного дерева арифметического выражения.
 *
 * value ≥ 0  -> операнд (число).
 * value  < 0 -> операция:
 *              -1 = '+', -2 = '-', -3 = '*', -4 = '/', -5 = '%'.
 */
struct TreeNode {
    int         value;      // значение узла
    TreeNode*   left;       // указатель на левое поддерево
    TreeNode*   right;      // указатель на правое поддерево
};

/**
 * @brief Содержит статические методы для работы с деревом выражения.
 */
class ExpressionTree {
public: // 1 tab
    /**
     * @brief Читает постфиксное выражение из файла и строит дерево.
     * @param filename Имя текстового файла-источника.
     * @param[out] root_root Указатель на корень построенного дерева (nullptr при ошибке).
     * @return true в случае успешного построения; false иначе.
     */
    static bool BuildFromFile(const std::string& filename, TreeNode*& root_root);

    /**
     * @brief Преобразует дерево так, чтобы в нём не осталось операции умножения.
     *
     * Каждый найденный узел с операцией «*» заменяется на лист,
     * хранящий вычисленное значение соответствующего поддерева.
     *
     * @param root_root Указатель на корень исходного дерева.
     * @return Указатель на корень преобразованного дерева (может совпадать с входным).
     */
    static TreeNode* RemoveMultiplication(TreeNode* root_root);

    /**
     * @brief Освобождает память, занятую деревом выражения.
     * @param node Корень дерева.
     */
    static void FreeTree(TreeNode* node);

private:        // 1 tab
    /**
     * @brief Пытается преобразовать строковый токен в число 0–9.
     * @param token Токен.
     * @param[out] value Числовое значение если токен — число.
     * @return true, если токен — корректное число; false иначе.
     */
    static bool TryParseNumber(const std::string& token, int& value);

    /**
     * @brief Преобразует токен операции в код (<0).
     * @param token Токен («+», «-», «*», «/», «%»).
     * @param[out] op_code Код операции, если токен валиден.
     * @return true, если токен — допустимая операция; false иначе.
     */
    static bool TryParseOperator(const std::string& token, int& op_code);

    /**
     * @brief Вычисляет значение поддерева.
     * @param node Корень поддерева.
     * @param[out] ok Флаг успешности (false, например, при делении на 0).
     * @return Вычисленное значение (некорректно, если ok == false).
     */
    static int Evaluate(const TreeNode* node, bool& ok);
};

#endif  // EXPRESSION_TREE_H_