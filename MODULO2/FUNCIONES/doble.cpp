
#include <iostream>
using namespace std;

// Funcion que devuelve el doble de un numero

int doble(int n) {
    return n * 2;
}

void line(){
    cout << "----------------------"<< endl;
}

int main() {

    int n;

    cout << "Ingrese un numero: ";
    cin >> n;

    int resultado = doble(n);

    cout << "El doble es: " << resultado << endl;
    cout << line << endl;
    return 0;
}