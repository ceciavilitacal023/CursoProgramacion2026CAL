

#include <iostream>
using namespace std;

int main() {
    double TotalCuenta;
    double porcentaje;
    double propina;
    double total;

    cout << "Ingrese el monto de la cuenta: ";
    cin >> TotalCuenta;

    cout << "Ingrese el porcentaje de propina en %: ";
    cin >> porcentaje;

    propina = TotalCuenta * porcentaje / 100.0;
    total = TotalCuenta + propina;

    cout << "La propina es: " << propina << endl;
    cout << "El total a pagar es: " << total << endl;
    cout << "Muchas gracias" << endl;

    return 0;
}