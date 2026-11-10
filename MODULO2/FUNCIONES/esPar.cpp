// Funcion para determinar si un numero es par

#include <iostream>
#include <string>
using namespace std;

// Funcion para saludar
void saludar(string nombre){
    cout << "Hola " << nombre << endl;
}

// Funcion para determinar si un numero es par
bool es_par(int n){
    return (n % 2 == 0);
}

int main(){

    string nombre;

    cout << "Ingrese su nombre: ";
    cin >> nombre;

    saludar(nombre);

    int numero;

    cout << "Ingrese un numero: ";
    cin >> numero;

    bool resultado = es_par(numero);

    if (resultado){
        cout << "El numero es par" << endl;
    }
    else{
        cout << "El numero es impar" << endl;
    }

    return 0;
}