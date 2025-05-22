#include "Stack.h"
#include <iostream>

Node::Node(int data) : data(data), next_node(nullptr) {}

Stack::Stack() : top_node(nullptr) {}

void Stack::Push(int data) {
    Node* new_node = new Node(data);
    new_node->next_node = top_node;
    top_node = new_node;
}

void Stack::Show() const {
    Node* current_node = top_node;
    while (current_node != nullptr) {
        std::cout << current_node->data << " ";
        current_node = current_node->next_node;
    }
    std::cout << std::endl;
}

void Stack::ShowAddress() const {
    std::cout << "Адрес вершины стека: " << top_node << std::endl;
}

int Stack::GetTopValue() const {
    if (top_node != nullptr) {
        return top_node->data;
    }
    return 1;
}

bool Stack::IsEmpty() const {
    return top_node == nullptr;
}