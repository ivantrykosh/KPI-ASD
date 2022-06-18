#include <iostream>
#include <stdlib.h>

using namespace std;

void Inp_Out_A(double*, int, int); // Ініціалізуємо та виводимо перший масив
void Solution(double*, int, int, double&, int&, int&, double&); // Оброблюємо масив
void Out_answer(double*, int, int, double&, int&, int&, double&); // Виводимо кінцевий масив

int main()
{
    const int m = 5; // Кількість рядків
    const int n = 5; // Кількість стовпців
    double A[m][n];  // Оголошуємо масив
    double x = 10.1; // Мінімальний елемент
    // Індекси мінімального елемента
    int row;
    int column;
    // Середньоарифметичне значення елементів
    double sum = 0;
    
    Inp_Out_A(&A[0][0], m, n); // Ініціалізуємо та виводимо перший масив
    Solution(&A[0][0], m, n, x, row, column, sum); // Оброблюємо масив
    Out_answer(&A[0][0], m, n, x, row, column, sum); // Виводимо кінцевий масив
}

void Inp_Out_A(double* p, int m, int n)
{
    srand(time(NULL));
    cout << "Array A:";
    for (int i = 0; i < m; i++)
    {
        cout << "\n";
        for (int j = 0; j < n; j++)
        {
            *(p + m * i + j) = (double)(rand()) / RAND_MAX * 10; // Випадкове дійсне число від 0 до 10
            printf("  %.2f", *(p + m * i + j)); //  Виводимо елементи масиву
        }
    }
}

void Solution(double* p, int m, int n, double& x, int& row, int& column, double& sum)
{
    bool flag = false; // Для обходу масиву за стовпцями
    int a = 0; // Кількість елементів над головною діагоналлю
    
    // Знаходимо середньоарифметичне значення елементів і мінімальний елемент
    for (int i = 0; i < m; i++)
    {
        if (flag == false)
        {
            for (int j = 0; j < n; j++) // Проходимо згори вниз
            {
                if (i > j)
                {
                    sum += *(p + n * j + i); // Накопичуємо суму
                    a++; // Збільшуємо кількість елементів
                }
                if (*(p + n * j + i) < x) // Знаходимо мінімальний елемент
                {
                    x = *(p + n * j + i);
                    row = j;
                    column = i;
                }
            }
        }
        else
        {
            for (int j = n - 1; j >= 0; j--) // Проходимо знизу вгору
            {
                if (i > j)
                {
                    sum += *(p + n * j + i); // Накопичуємо суму
                    a++; // Збільшуємо кількість елементів
                }
                if (*(p + n * j + i) < x) // Знаходимо мінімальний елемент
                {
                    x = *(p + n * j + i);
                    row = j;
                    column = i;
                }
            }
        }
        flag = !flag; // Змінюємо на протилежне значення
    }
    
    sum = sum / a; // Середнє арифметичне значення
    flag = false; // Змінюємо на протилежне значення
    
    /* Обходимо масив і змінюємо елемент над головною діагоналлю,
       що більший за середньоарифметичне значення, на мінімальний елемент*/
    for (int i = 0; i < m; i++)
    {
        if (flag == false)
        {
            for (int j = 0; j < n; j++)
            {
                if (j < i)
                {
                    if (*(p + n * j + i) > sum) // Перевіряємо елемент
                    {
                        *(p + n * j + i) = x; // Змінюємо його
                    }
                }
            }
        }
        else
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (j < i)
                {
                    if (*(p + n * j + i) > sum) // Перевіряємо елемент
                    {
                        *(p + n * j + i) = x; // Змінюємо його
                    }
                }
            }
        }
        flag = !flag; // Змінюємо на протилежне значення
    }

}

void Out_answer(double* p, int m, int n, double& x, int& row, int& column, double& sum)
{
    printf("\n\nX = %.2f", x); // Виводимо мінімальний елемент
    cout << "   row = " << row + 1 << "  column = " << column + 1; // Виводимо його індекси
    printf("\nSum = %.2f\n", sum); // Виводимо середньоарифметичне значення
    cout << "\nAnswer: ";
    // Виводимо масив
    for (int i = 0; i < m; i++)
    {
        cout << "\n";
        for (int j = 0; j < n; j++)
        {
            printf("  %.2f", *(p + m * i + j));
        }
    }
}