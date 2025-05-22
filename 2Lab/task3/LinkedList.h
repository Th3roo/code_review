#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>

class LinkedList; 

void insertBeforeEverySecond(LinkedList& list, int insertionValue);

class Node {
public:
	int data;
	Node* next;
	Node(int value);
};

class LinkedList {
private:
	Node* head;
	void insertBeforeEverySecond(int insertionValue);

public:
	LinkedList();

	void add(int value);
	void print();
	Node* getLastNode();
	void clearList();

	friend void insertBeforeEverySecond(LinkedList& list, int insertionValue); 
};

#endif // LINKEDLIST_H
