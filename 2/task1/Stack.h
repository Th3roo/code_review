#pragma once

class Node {
public:
    int data;
    Node* next_node;
    Node(int data);
};

class Stack {
private:
    Node* top_node;
public:
    Stack();
    void Push(int data);
    void Show() const;
    void ShowAddress() const;
    int GetTopValue() const;
    bool IsEmpty() const;
};