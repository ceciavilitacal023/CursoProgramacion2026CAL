

#include <iostream>
using namespace std;

// Funcion cuadrado: devuelve n * n

int cuadrado(int n) {
    return n * n;
}

int main() {

    int i;

    cout << "Ingrese un numero: ";
    cin >> i;

    int resultado = cuadrado(i);

    cout << "El cuadrado es: " << resultado << endl;

    return 0;
}

// Saludar


