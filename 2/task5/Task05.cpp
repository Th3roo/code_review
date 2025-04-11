/* Элементами контейнеров являются целые числа. Для
заполнения контейнера использовать итератор и конструктор соответствующего контейнера,
для вывода элементов использовать итератор (для вывода элементов в обратном порядке
использовать обратные итераторы, возвращаемые функциями-членами rbegin и rend)
Обязательно наличие дружественного интерфейса. Ввод данных организовать 
разными способами (с клавиатуры, рандом, из файла)


 Дан дек D с нечетным количеством элементов N (≥ 5). Добавить в начало дека пять
его средних элементов в исходном порядке. Использовать один вызов функции-члена insert. */
#include <iostream>
#include <deque>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iterator>
using namespace std;

void FuncInsert(deque<int>& D) {
    size_t N = D.size();

    // Вычисляем индекс среднего элемента
    size_t MiddleIndex = N / 2;

    // Получаем пять средних элементов
    deque<int> MiddleElements;
    for (size_t i = MiddleIndex - 2; i <= MiddleIndex + 2; ++i) 
    {
        MiddleElements.push_back(D[i]);
    }

    // Вставляем пять средних элементов в начало дека
    D.insert(D.begin(), MiddleElements.begin(), MiddleElements.end());
}

deque<int> FuncKeyboard() {
    int count;
    cout << "Введите количество целых чисел (нечетное и >= 5): ";
    cin >> count;

    while (count < 5 || count % 2 == 0) 
    {
        cout << "Количество должно быть нечетным и >= 5. Повторите ввод: ";
        cin >> count;
    }

    deque<int> D;
    cout << "Введите " << count << " целых чисел:" << endl;
    for (int i = 0; i < count; ++i) 
    {
        int number;
        cin >> number;
        D.push_back(number);
    }

    return D;
}

deque<int> FuncRandom(int count) {
    deque<int> D;
    srand(static_cast<unsigned>(time(0)));

    for (int i = 0; i < count; ++i) 
    {
        D.push_back(rand() % 100);
    }

    return D;
}

deque<int> FuncFile() {
    deque<int> D;
    ifstream infile("a.txt");
    int number;

    if (!infile.is_open()) 
    {
        throw runtime_error("Не удалось открыть файл.");
    }

    while (infile >> number) 
    {
        D.push_back(number);
    }

    if (D.size() < 5 || D.size() % 2 == 0) 
    {
        throw invalid_argument("Количество чисел в файле должно быть нечетным и >= 5.");
    }

    return D;
}

int main() {
    setlocale(LC_ALL, "ru");
    int choice;
    cout << "Выберите метод ввода данных: 1.Ввод с клавиатуры  2.Случайные числа  3.Чтение из файла" << endl;
    cin >> choice;

    deque<int> D;

    try 
    {
        switch (choice) 
        {
            case 1:
                D = FuncKeyboard();
                break;
            case 2: 
            {
                int count;
                cout << "Введите количество чисел (нечетное и >= 5): ";
                cin >> count;
                while (count < 5 || count % 2 == 0) 
                {
                    cout << "Количество должно быть нечетным и >= 5. Повторите ввод: ";
                    cin >> count;
                }
                D = FuncRandom(count);
                break;
            }
            case 3: 
            {
                D = FuncFile();
                break;
            }
            default:
                cerr << "Некорректный выбор." << endl;
                return 1;
        }

        cout << "Исходный дек: ";
        for (const auto& elem : D) 
        {
            cout << elem << " ";
        }
        cout << endl;

        FuncInsert(D);

        cout << "Дек после вставки: ";
        for (const auto& elem : D) 
        {
            cout << elem << " ";
        }
        cout << endl;

    }
    catch (const exception& e) 
    {
        cerr << "Ошибка: " << e.what() << endl;
    }
    return 0;
}
