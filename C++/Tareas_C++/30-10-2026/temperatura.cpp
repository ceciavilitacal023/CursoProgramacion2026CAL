

#include <iostream>
using namespace std;

int main() {
    double celsius;
    double fahrenheit;

    cout << "Ingrese los grados en °C: ";
    cin >> celsius;

    fahrenheit = celsius * 9.0 / 5.0 + 32.0;

    cout << "La temperatura en Fahrenheit es: " << fahrenheit << " °F" << endl;

    return 0;
}