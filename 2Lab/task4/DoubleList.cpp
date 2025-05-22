/* Продолжение задания №Task 4 */

#include "DoubleList.h"
#include <iostream>
#include <cstddef> // For nullptr

// Node Constructor Definition
DoubleList::Node::Node(int value) {
	data = value;
	next = nullptr;
	prev = nullptr;
}

// DoubleList Constructor
DoubleList::DoubleList() {
	head_node = nullptr;
}

// DoubleList Destructor
DoubleList::~DoubleList() {
	if (!head_node) {
		return;
	}
	Node* current_node = head_node->next;
	while (current_node != head_node) {
		Node* node_to_delete = current_node;
		current_node = current_node->next;
		delete node_to_delete;
	}
	delete head_node;
	head_node = nullptr;
}


void DoubleList::push_back(int value) {
	Node* new_node = new Node(value);
	if (!head_node) {
		head_node = new_node;
		new_node->next = new_node;
		new_node->prev = new_node;
	} else {
		Node* tail_node = head_node->prev;
		tail_node->next = new_node;
		new_node->prev = tail_node;
		new_node->next = head_node;
		head_node->prev = new_node;
	}
}

void DoubleList::printList() {
	if (!head_node) {
		std::cout << "Список пуст." << std::endl;
		return;
	}
	Node* current_node = head_node;
	do {
		std::cout << current_node->data << " ";
		current_node = current_node->next;
	} while (current_node != head_node);
	std::cout << std::endl;
}

DoubleList::Node* DoubleList::deleteNode(Node* node_to_delete) {
	if (!node_to_delete) {
		return nullptr;
	}
	if (node_to_delete->next == node_to_delete && node_to_delete->prev == node_to_delete) {
		delete node_to_delete;
		head_node = nullptr;
		return nullptr;
	}

	Node* previous_node = node_to_delete->prev;
	Node* next_node = node_to_delete->next;

	previous_node->next = next_node;
	next_node->prev = previous_node;

	if (node_to_delete == head_node) {
		head_node = next_node;
	}

	delete node_to_delete;
	return next_node;
}


DoubleList::Node* DoubleList::removeNodesWithMatchingNeighbors() {
	if (!head_node || head_node->next == head_node) {
		return head_node ? head_node->prev : nullptr;
	}

	bool list_changed = true;
	while (list_changed) {
		list_changed = false;
		if (!head_node || head_node->next == head_node) break;

		Node* current_node = head_node;
		Node* iteration_start_node = head_node;
		bool is_first_pass = true;

		do {
			Node* next_node_cache = current_node->next;
			if (current_node->prev->data == current_node->next->data) {
				if (current_node == iteration_start_node) {
					if (current_node->next == current_node) {
						iteration_start_node = nullptr;
					} else {
						iteration_start_node = current_node->next;
					}
				}

				Node* node_after_deletion = deleteNode(current_node);

				if (!head_node) {
					return nullptr;
				}
				current_node = node_after_deletion;
				list_changed = true;
				is_first_pass = false;

				if (current_node == iteration_start_node && iteration_start_node != nullptr) {
					break;
				}

			} else {
				current_node = next_node_cache;
			}
		} while (current_node != iteration_start_node && head_node != nullptr && head_node->next != head_node);

		if (list_changed && head_node != nullptr && head_node->next == head_node) {
			list_changed = false;
		}
	}

	return head_node ? head_node->prev : nullptr;
}
