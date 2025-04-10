#include "Queue.h"
#include <iostream> // Needed for std::cerr

// Function to add an element to the queue
void Enqueue(Queue& queue, int value) {
	QueueNode* newNode = new QueueNode{value, nullptr};
	if (queue.rear) {
		queue.rear->nextNode = newNode;
	} else {
		queue.front = newNode;
	}
	queue.rear = newNode;
}

// Function to remove an element from the queue
bool Dequeue(Queue& queue, int& value) {
	if (queue.front == nullptr) {
		std::cerr << "Error: Cannot dequeue from an empty queue." << std::endl;
		return false;
	}

	QueueNode* nodeToRemove = queue.front;
	value = nodeToRemove->data;
	queue.front = queue.front->nextNode;

	if (queue.front == nullptr) {
		queue.rear = nullptr;
	}

	delete nodeToRemove;
	return true;
}
