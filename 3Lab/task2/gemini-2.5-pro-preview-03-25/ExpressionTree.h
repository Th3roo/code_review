#ifndef EXPRESSIONTREE_H
#define EXPRESSIONTREE_H

#include <string>
#include <vector> // For internal stack use in implementation if needed

// Forward declaration if Node uses functions defined later, not needed here.

/**
 * @struct Node
 * @brief Represents a node in the arithmetic expression tree.
 *        Can store an operand (0-9) or an encoded operator (-1 to -5).
 */
struct Node {
	int value;      // Operand (0-9) or encoded operator (-1 to -5)
	Node* left;     // Pointer to the left child
	Node* right;    // Pointer to the right child

	/**
	 * @brief Constructor for a Node.
	 * @param val The value for the node.
	 * @param l Pointer to the left child (defaults to nullptr).
	 * @param r Pointer to the right child (defaults to nullptr).
	 */
	Node(int val, Node* l = nullptr, Node* r = nullptr);

	/**
	 * @brief Destructor for a Node.
	 *        Recursively deletes child nodes to prevent memory leaks.
	 */
	~Node();

	// Disable copy constructor and assignment operator to prevent shallow copies
	// leading to double deletion issues with raw pointers.
	Node(const Node&) = delete;
	Node& operator=(const Node&) = delete;
};

/**
 * @brief Builds an expression tree from a Reverse Polish Notation (RPN) expression
 *        stored in a file.
 * @param filename The name of the file containing the RPN expression.
 * @return Node* Pointer to the root of the constructed tree, or nullptr if an error occurred
 *         (e.g., file not found, invalid RPN, invalid token). Errors are printed to std::cerr.
 * @throws Does not throw exceptions directly, but uses std::cerr for errors.
 */
Node* buildTreeFromFile(const std::string& filename);

/**
 * @brief Evaluates the integer value represented by the expression tree.
 * @param node Pointer to the root of the tree/subtree to evaluate.
 * @return int The calculated integer value.
 * @throws std::runtime_error If division or modulo by zero occurs during evaluation.
 */
int evaluateTree(Node* node);

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
Node* transformTree(Node* node);

#endif // EXPRESSIONTREE_H