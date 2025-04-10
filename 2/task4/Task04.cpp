/*
��� ����������� ���������� �������� ������ � ��������� ������
������� ����� ������. ���������� ������� � ������ ��� ��������, � ������� ������ �
����� ����� ���������. ���� ����� ��������� ���, �� �������� ������ ��� ���������.
������ � ��������� �������� ������� ��������. � ���������� ������� ������ ��
��������� ������� ����������� ������.
��� ������������ ��������� ������ ������������� ����� ������. �� ������������ STL.  
��� ������ ������������ ��������� ������ ���� ������������ �����������
����� ������� - ����������/��������/������ ���������. �� ���� ������� ����������� ������� 
�������������� ����������. ���� ������ � ����������.
*/

class DoubleList {
    public:
        struct Node {
            int data;
            Node* next;
            Node* prev;
            Node(int val) {
                data = val;
                next = nullptr;
                prev = nullptr;
            }
            
        };
    
        Node* head;
    
        DoubleList() {
            head = nullptr;
        }        
    
        ~DoubleList() {
            if (!head)
                return;
            Node* curr = head;
            while (true) {
                Node* tmp = curr;
                curr = curr->next;
                delete tmp;
                if (curr == head)
                    break;
            }
        }
    
        void push_back(int value) {
            Node* newNode = new Node(value);
            if (!head) {
                head = newNode;
                newNode->next = newNode;
                newNode->prev = newNode;
            }
            else {
                Node* tail = head->prev;
                tail->next = newNode;
                newNode->prev = tail;
                newNode->next = head;
                head->prev = newNode;
            }
        }
    
        void printList() {
            Node* curr = head;
            while (true) {
                cout << curr->data << " ";
                curr = curr->next;
                if (curr == head)
                    break;
            }
            cout << endl;
        }
    
        Node* deleteNode(Node* node) {
            if (!node)
                return nullptr;
            if (node->next == node && node->prev == node) {
                if (node == head)
                    head = nullptr;
                delete node;
                return nullptr;
            }
            Node* nextNode = node->next;
            node->prev->next = node->next;
            node->next->prev = node->prev;
            if (node == head)
                head = nextNode;
            delete node;
            return nextNode;
        }
    
    Node* removeSides() {
        if (!head) return nullptr;
        bool anyDeletion = false;
        bool deletedSomething = false;
        while (true) {
            anyDeletion = false;
            if (!head || head->next == head)
                break;
            Node* start = head;
            Node* curr = head;
            bool completedCycle = false;
            while (!completedCycle) {
                int leftData = curr->prev->data;
                int rightData = curr->next->data;
                if (leftData == rightData) {
                    anyDeletion = true;
                    deletedSomething = true;
                    Node* nextNode = curr->next;
                    if (curr == head)
                        head = nextNode;
                    curr = deleteNode(curr);
                    if (!curr)
                        return nullptr;
                    start = head;
                    continue;
                }
                else {
                    curr = curr->next;
                }
                if (curr == start)
                    completedCycle = true;
            }
            if (!anyDeletion)
                break;
        }
        if (!head)
            return nullptr;
        Node* tail = head->prev;
        return tail;
    }
};    
    

int main(){
    DoubleList list;
    int n, value;
    cout << "������� ���� �����: ";
    cin >> n;
    cout << "����� �����" << endl;
    for (int i = 0; i < n; i++) {
        cin >> value;
        list.push_back(value);
    }
    cout << "���������� ������: ";
    list.printList();
    DoubleList::Node* tail = list.removeSides();
    cout << "������������ ������: ";
    list.printList();
    cout << "��������� �������: " << tail->data << endl;
}