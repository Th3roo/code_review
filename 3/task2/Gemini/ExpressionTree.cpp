/* Implementation of expression tree building, evaluation, and transformation */
#include "ExpressionTree.h"
#include <iostream>
#include <fstream>
#include <stack>
#include <string>
#include <vector>
#include <stdexcept> // For std::runtime_error in evaluateTree
#include <sstream>   // For parsing tokens

// Allow using namespace std in .cpp files
using namespace std;

// --- Node Implementation ---

/**
 * @brief Constructor for a Node.
 * @param val The value for the node.
 * @param l Pointer to the left child (defaults to nullptr).
 * @param r Pointer to the right child (defaults to nullptr).
 */
Node::Node(int val, Node* l /*= nullptr*/, Node* r /*= nullptr*/) :
	value(val), left(l), right(r) {}

/**
 * @brief Destructor for a Node.
 *        Recursively deletes child nodes to prevent memory leaks.
 */
Node::~Node() {
	// Recursively delete children. Deleting nullptr is safe.
	delete left;
	left = nullptr; // Optional: Good practice to null pointers after delete
	delete right;
	right = nullptr;// Optional: Good practice to null pointers after delete
}

// --- Helper Function ---

/**
 * @brief Maps an operator character to its integer code.
 * @param op The operator character (+, -, *, /, %).
 * @return int The corresponding integer code (-1 to -5), or 0 if invalid.
 */
int encodeOperator(char op) {
	switch (op) {
		case '+': return -1;
		case '-': return -2;
		case '*': return -3;
		case '/': return -4;
		case '%': return -5;
		default:  return 0; // Indicate invalid operator
	}
}

// --- Core Logic Implementation ---

/**
 * @brief Builds an expression tree from a Reverse Polish Notation (RPN) expression
 *        stored in a file.
 * @param filename The name of the file containing the RPN expression.
 * @return Node* Pointer to the root of the constructed tree, or nullptr if an error occurred
 *         (e.g., file not found, invalid RPN, invalid token). Errors are printed to std::cerr.
 * @throws Does not throw exceptions directly, but uses std::cerr for errors.
 */
Node* buildTreeFromFile(const string& filename) {
	ifstream inputFile(filename);
	if (!inputFile.is_open()) {
		cerr << "Ошибка: Не удалось открыть файл '" << filename << "'" << endl;
		return nullptr;
	}

	stack<Node*> nodeStack;
	string token = "";

	// Read tokens separated by whitespace
	while (inputFile >> token) {
		// Try to interpret as an integer operand (single digit 0-9)
		if (isdigit(token[0]) && token.length() == 1) {
			int operandValue = token[0] - '0'; // Convert char '0'-'9' to int 0-9
			// Although problem statement says 0-9, good practice to double check range
			 if (operandValue >= 0 && operandValue <= 9) {
				Node* operandNode = nullptr;
				try {
					operandNode = new Node(operandValue);
					nodeStack.push(operandNode);
				} catch (const bad_alloc& e) {
					cerr << "Ошибка: Не удалось выделить память для узла операнда." << endl;
					// Clean up stack before returning
					while(!nodeStack.empty()){
						delete nodeStack.top();
						nodeStack.pop();
					}
					inputFile.close(); // Ensure file is closed
					return nullptr;
				}
			} else {
				// This case shouldn't happen if isdigit() and length == 1 checks pass for 0-9
				cerr << "Ошибка: Неверный операнд '" << token << "'. Ожидалась цифра от 0 до 9." << endl;
				while(!nodeStack.empty()){ delete nodeStack.top(); nodeStack.pop(); }
				inputFile.close();
				return nullptr;
			}
		} else if (token.length() == 1) { // Potential operator
			int operatorCode = encodeOperator(token[0]);
			if (operatorCode != 0) { // It's a valid operator
				// Check if there are enough operands on the stack
				if (nodeStack.size() < 2) {
					cerr << "Ошибка: Недостаточно операндов для операции '" << token << "' в RPN." << endl;
					while(!nodeStack.empty()){ delete nodeStack.top(); nodeStack.pop(); }
					inputFile.close();
					return nullptr;
				}
				// Pop the operands (right first, then left)
				Node* rightOperand = nodeStack.top();
				nodeStack.pop();
				Node* leftOperand = nodeStack.top();
				nodeStack.pop();

				// Create the operator node
				Node* operatorNode = nullptr;
				try {
					operatorNode = new Node(operatorCode, leftOperand, rightOperand);
					nodeStack.push(operatorNode);
				} catch (const bad_alloc& e) {
					cerr << "Ошибка: Не удалось выделить память для узла оператора." << endl;
					// Must delete popped operands if operator node creation fails
					delete leftOperand;
					delete rightOperand;
					while(!nodeStack.empty()){ delete nodeStack.top(); nodeStack.pop(); }
					inputFile.close();
					return nullptr;
				}
			} else {
				cerr << "Ошибка: Неверный токен '" << token << "' в файле." << endl;
				while(!nodeStack.empty()){ delete nodeStack.top(); nodeStack.pop(); }
				inputFile.close();
				return nullptr;
			}
		} else { // Invalid token (not single digit, not single operator char)
			cerr << "Ошибка: Неверный токен '" << token << "' в файле." << endl;
			while(!nodeStack.empty()){ delete nodeStack.top(); nodeStack.pop(); }
			inputFile.close();
			return nullptr;
		}
	} // end while reading tokens

	inputFile.close(); // Close the file

	// After processing all tokens, the stack should contain exactly one node (the root)
	if (nodeStack.size() == 1) {
		return nodeStack.top();
	} else if (nodeStack.empty() && token.empty()) {
         // Handle case of empty input file correctly
         cerr << "Ошибка: Входной файл пуст или не содержит допустимого выражения." << endl;
         return nullptr;
    }
    else {
		cerr << "Ошибка: Неверный формат RPN. Лишние операнды или незавершенное выражение." << endl;
		// Clean up remaining nodes on the stack
		while(!nodeStack.empty()){
			delete nodeStack.top();
			nodeStack.pop();
		}
		return nullptr;
	}
}

/**
 * @brief Evaluates the integer value represented by the expression tree.
 * @param node Pointer to the root of the tree/subtree to evaluate.
 * @return int The calculated integer value.
 * @throws std::runtime_error If division or modulo by zero occurs during evaluation.
 */
int evaluateTree(Node* node) {
	// Base case: If null pointer, indicates an error or empty subtree
	if (node == nullptr) {
		// This situation might indicate an invalid tree structure.
		// Throwing here helps signal the problem upwards.
		throw runtime_error("Попытка вычислить значение пустого узла (nullptr).");
	}

	// Base case: If it's a leaf node (operand)
	if (node->left == nullptr && node->right == nullptr) {
		// Check if it's a valid operand value range (0-9)
		if(node->value >= 0 && node->value <= 9) {
			return node->value;
		} else {
			// Or if it's a transformed node holding a result
			// For simplicity, assume any leaf node holds a valid value at this stage.
			// A more robust check could verify it's not an operator code.
			// If it IS an operator code in a leaf, the tree is malformed.
			 if (node->value < 0) {
                 throw runtime_error("Неверный узел: оператор без дочерних узлов.");
             }
			return node->value; // Assume it's a valid pre-calculated value
		}
	}

	// Recursive step: Evaluate children first
	// Check if children exist before evaluating (robustness)
	if (node->left == nullptr || node->right == nullptr) {
		throw runtime_error("Неверный узел: оператор с отсутствующими дочерними узлами.");
	}
	int leftVal = evaluateTree(node->left);
	int rightVal = evaluateTree(node->right);

	// Perform the operation based on the node's value
	switch (node->value) {
		case -1: // +
			return leftVal + rightVal;
		case -2: // -
			return leftVal - rightVal;
		case -3: // *
			return leftVal * rightVal;
		case -4: // / (integer division)
			if (rightVal == 0) {
				throw runtime_error("Ошибка вычисления: Деление на ноль.");
			}
			return leftVal / rightVal;
		case -5: // % (integer remainder)
			if (rightVal == 0) {
				throw runtime_error("Ошибка вычисления: Взятие остатка от деления на ноль.");
			}
			return leftVal % rightVal;
		default:
			// Should not happen in a correctly built tree
			throw runtime_error("Неизвестный код операции в узле дерева: " + to_string(node->value));
	}
}

/**
 * @brief Transforms the expression tree by replacing all multiplication subtrees
 *        with leaf nodes containing the evaluated result of that subtree.
 *        The original multiplication subtree is deleted.
 * @param node Pointer to the root of the tree/subtree to transform.
 * @return Node* Pointer to the root of the transformed tree/subtree. Returns nullptr
 *         if an error occurred during evaluation needed for transformation (e.g., div by zero).
 * @throws Does not throw exceptions directly, handles evaluation exceptions internally
 *         using std::cerr and returning nullptr.
 */
Node* transformTree(Node* node) {
	// Base case: empty subtree
	if (node == nullptr) {
		return nullptr;
	}

	// Recursively transform children first (post-order)
	// This ensures that nested multiplications are handled correctly from bottom up.
	// We store the results in temporary pointers because the recursive call might return
	// a pointer to a *new* node if a child was transformed.
	Node* transformedLeft = transformTree(node->left);
	Node* transformedRight = transformTree(node->right);

	// Update the node's children with the potentially transformed ones.
	// This is safe even if they weren't transformed (pointers remain the same).
	node->left = transformedLeft;
	node->right = transformedRight;


	// Now process the current node
	if (node->value == -3) { // Is it multiplication?
		int result = 0;
		try {
			// Evaluate the subtree rooted at this multiplication node
			// Note: It uses the potentially already transformed children.
			result = evaluateTree(node);
		} catch (const runtime_error& e) {
			cerr << "Ошибка при вычислении поддерева для трансформации: " << e.what() << endl;
			// If evaluation fails (e.g., div by zero deeper down), we cannot transform.
			// We should clean up the current node and signal failure by returning nullptr.
			// Deleting 'node' will trigger recursive deletion of its children via destructor.
			delete node; // This deletes the structure rooted at 'node'
			return nullptr; // Signal error
		}

		// Create the replacement leaf node containing the calculated result
		Node* replacementNode = nullptr;
		try {
			replacementNode = new Node(result); // New node is a leaf
		} catch (const bad_alloc& e) {
			cerr << "Ошибка: Не удалось выделить память для узла-замены при трансформации." << endl;
			// We still need to delete the original node structure
			delete node;
			return nullptr; // Signal error
		}


		// *** Crucial Memory Management ***
		// We need to delete the original multiplication node ('node') BUT *not* its children,
		// because the children pointers (node->left, node->right) might now point to
		// nodes that are part of the larger tree structure (if they weren't multiplication nodes themselves)
		// or replacement nodes created by deeper recursive calls.
		// The 'delete node;' call would recursively delete these children if we don't detach them first.
		node->left = nullptr;  // Detach the left child
		node->right = nullptr; // Detach the right child
		delete node;           // Now delete ONLY the original multiplication node itself

		// Return the pointer to the new replacement leaf node
		return replacementNode;

	} else {
		// Not a multiplication node, just return the pointer to the (potentially child-modified) current node.
		return node;
	}
}