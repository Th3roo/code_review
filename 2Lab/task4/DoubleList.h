#ifndef DOUBLELIST_H
#define DOUBLELIST_H

#include <cstddef> // For nullptr

class DoubleList {
public:
	struct Node {
		int data;
		Node* next;
		Node* prev;
		Node(int value);
	};

	Node* head_node;

	DoubleList();
	~DoubleList();

	void push_back(int value);
	void printList();
	Node* deleteNode(Node* node_to_delete);
	Node* removeNodesWithMatchingNeighbors();
};

#endif // DOUBLELIST_H
