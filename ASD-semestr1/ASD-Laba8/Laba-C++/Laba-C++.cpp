#include <iostream>
#include <stdlib.h>
#include <iomanip>

using namespace std;

void In_Out_A(double*, int, int);   // Ініціалізація та виведення початкового масиву
void In_Out_B(double*, double*, double, int, int); // Ініціалізація та виведення другого масиву
void Solution(double*, double, int);  // Сортування другого масиву
void Browse(double*, int);   // Виведення відсортованого масиву

int main()
{
    const int rows = 8;       // Кількість рядків
    const int columns = 4;    // Кількість стовпців
    double A[rows][columns];  // Оголошення першого масиву
    double B[rows];           // Оголошення другого масиву
    double b = 1.0;  // Змінна для обчислення добутку елементів рядка та для заміни елементів

    In_Out_A(&A[0][0], rows, columns); // Ініціалізація та виведення першого масиву
    In_Out_B(&A[0][0], B, b, rows, columns); // Ініціалізація та виведення другого масиву
    Solution(B, b, rows);   // Обробка третього масиву
    Browse(B, rows);        // Виведення обробленого масиву
    return 0;
}

void In_Out_A(double* g, int rows, int columns)
{
    srand(time(NULL));
    cout << "Array A: ";
    for (int i = 0; i < rows; i++)
    {
        cout << "\n";
        for (int j = 0; j < columns; j++)
        {
            *(g + i * columns + j) = (double)(rand()) / RAND_MAX * 10;  // Випадкове дійсне число
            printf("  %.1f", *(g + i * columns + j));  // Виводимо поточний елемент масиву
        }
    }
}

void In_Out_B(double *g, double* p, double b, int rows, int columns)
{
    cout << "\n\nArray B:\n";
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            b *= *(g + i*columns + j); // Накопичуємо добуток елементів рядка
        }
        p[i] = b; // Ініціалізуємо елементи другого масиву
        printf(" %.4f  ", p[i]); // Виводимо поточний елемент масиву
        b = 1.0;
    }
}

void Solution(double* p, double b, int rows)
{
    for (int i = rows / 2; i >= 1; i /= 2) // Крок обміну
    {
        // Перебираємо елементи з кроком і
        for (int j = i; j < rows; j++)
        {
            for (int k = j; k >= i; k -= i)
            {
                // Мінямо елементи місцями, якщо елемент зліва більший за елемент справа
                if (p[k - i] > p[k])
                {
                    b = p[k];
                    p[k] = p[k - i];
                    p[k - i] = b;
                }
            }
        }
    }
}
void Browse(double* p, int rows)
{
    cout << "\n\nAnswer:\n";
    for (int i = 0; i < rows; i++)
    {
        printf(" %.4f  ", p[i]); // Виводимо елементи відсортованого масиву
    }
}