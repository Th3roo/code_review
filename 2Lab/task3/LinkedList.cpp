#include "LinkedList.h"
#include <iostream>

using namespace std;

Node::Node(int value) : data(value), next(nullptr) {}

LinkedList::LinkedList() : head(nullptr) {}

void LinkedList::add(int value) {
	Node* newNode = new Node(value);
	if (head == nullptr) {
		head = newNode;
	} else {
		Node* current = head;
		while (current->next != nullptr) {
			current = current->next;
		}
		current->next = newNode;
	}
}

void LinkedList::insertBeforeEverySecond(int insertionValue) {
	Node* current = head;
	int count = 1;

	while (current != nullptr && current->next != nullptr) {
		if (count % 2 == 1) {
			Node* newNode = new Node(insertionValue);
			newNode->next = current->next;
			current->next = newNode;
			current = newNode->next;
		} else {
			current = current->next;
		}
		++count;
	}
}

void LinkedList::print() {
	Node* current = head;
	while (current != nullptr) {
		cout << current->data << " ";
		current = current->next;
	}
	cout << endl;
}

Node* LinkedList::getLastNode() {
	Node* current = head;
	while (current != nullptr && current->next != nullptr) { 
		current = current->next;
	}
	return current;
}

void LinkedList::clearList() {
	while (head != nullptr) {       // While the list is not empty
		Node* nodeToDelete = head;          // Store the current head
		head = head->next;          // Move head to the next node
		delete nodeToDelete;                // Delete the old head node
	}
}
void insertBeforeEverySecond(LinkedList& list, int insertionValue) {
	list.insertBeforeEverySecond(insertionValue); 
}
