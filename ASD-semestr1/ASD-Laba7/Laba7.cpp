#include <iostream>

using namespace std;

void Input_array(char*, char*, char*, int);   // Заповнюємо масиви
int Output_array(char*, char*, char*, int);   // Виводимо масиви
void Solution(char*, int);                    // Перетворюємо третій масив
void Browse(char*, int);                      // Виводимо кінцевий масив

int main()
{
    const int n = 10; // Розмір масиву
    int m;            // Змінна, що дорівнює розміру масиву
    char array1[n];   // Перший масив
    char array2[n];   // Другий масив
    char array3[n];   // Третій масив
    
    Input_array(array1, array2, array3, n);
    m = Output_array(array1, array2, array3, n);
    Solution(array3, m);
    Browse(array3, m);
    
    return 0;
}

void Input_array(char *p, char *g, char *s, int n)
{
	// Ініціалізуємо перший і другий масиви
    for (int i = 0; i < n; i++) 
    {
        *p = 120 - i;
        *g = 110 + i;
        p++;
        g++;
    }
    
    // Ініціалізуємо третій масив
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (*(p - n + i) == *(g - n + j))
            {
                *s = *(g - n + j);
            }
        }
        s++;
    }
}

int Output_array(char *p, char *g, char *s, int m)
{
	// Виводимо масиви
    cout << "Array1: ";
    for (int i = 0; i < m; i++)
    {
        cout << *(p + i) << " ";
    }
    cout << "\nArray2: ";
    for (int i = 0; i < m; i++)
    {
        cout << *(g + i) << " ";
    }
    cout << "\nArray3: ";
    for (int i = 0; i < m; i++)
    {
        if (*(s+i) == 0) // Видаляємо елементи з нульовим значенням
        {
            m = m-1;
            for (int k = 0; k < m; k++)
            {
                *(s + k) = *(s + k + 1);
            }
        }
        cout << *(s + i) << " ";
    }
    return m;
}

void Solution(char* s, int m)
{
    int a, b;     // a - середнє арифметичне масиву, b - індекс максимального елемента
    int sum = 0;  // Сума елементів масиву
    char max = 0; // Максимальний елемент масиву
    
    for (int i = 0; i < m; i++)
    {
        sum += *(s + i);    // Знаходимо суму елементів
        
        // Знаходимо максимальне значення масиву
        if (*(s + i) > max)
        {
            max = *(s + i); 
            b = i;
        }
    }
    
    a = sum/m;     // Середнє арифметичне елементів масиву
    *(s + b) = a; // Замінюємо максимальний елемент середньоарифметичним
}

void Browse(char* s, int m)
{
    // Виводимо кінцевий масив
    cout << "\nAnswer: ";
    for (int i = 0; i < m; i++)
    {
        cout << *(s+i) << " ";
    }
}