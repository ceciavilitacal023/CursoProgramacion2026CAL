

#include <iostream>
using namespace std;

int main() {
    int numero;
    int centena, decena, unidad;
    int invertido;

    cout << "Ingrese un numero de 3 cifras: ";
    cin >> numero;

    centena = numero / 100;
    decena = (numero % 100) / 10;
    unidad = numero % 10;

    invertido = unidad * 100 + decena * 10 + centena;

    cout << "El numero invertido es: " << invertido << endl;

    return 0;
}
