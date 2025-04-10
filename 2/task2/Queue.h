#ifndef QUEUE_H
#define QUEUE_H

// Structure for a queue node
struct QueueNode {
	int data;
	QueueNode* nextNode;
};

// Structure for the queue itself
struct Queue {
	QueueNode* front; // Head
	QueueNode* rear;  // Tail

	// Constructor to initialize an empty queue
	Queue() : front(nullptr), rear(nullptr) {}
};

void Enqueue(Queue& queue, int value);

bool Dequeue(Queue& queue, int& value); 

#endif // QUEUE_H
