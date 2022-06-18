#include <iostream>
using namespace std;

double dif_y(int, double); // Оголошуємо функцію

int main()
{
    double a, d, an;   // Перший член, різниця і n-ий член
    int n;             // Кількість членів арифметичної прогресії
    cout << "Enter the first term of the arithmetic progression: ";
    cin >> a;
    cout << "Enter the difference of the arithmetic progression: ";
    cin >> d;
    cout << "Enter n > 0: ";
    cin >> n;
    an = a + dif_y(n, d);  // Обчислюємо n-ий член
    cout << n << "-term of the arithmetic progression = " << an;
}

double dif_y(int k, double d)
{
    if (k > 1)
    {
        return d + dif_y(k-1, d); // Повертаємо різницю і викликаємо функцію 
    }
    return 0;
}
