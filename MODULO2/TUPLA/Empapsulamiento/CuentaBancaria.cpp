

#include <iostream>
#include <string>
using namespace std;

class CuentaBancaria {
private:
    string titular;
    double saldo;

public:
    // Constructor
    CuentaBancaria(string nombre, double cantidad) {
        titular = nombre;
        saldo = cantidad;
    }

    // Ver titular
    string ver_titular() {
        return titular;
    }

    // Ver saldo
    double ver_saldo() {
        return saldo;
    }

    // Depositar dinero
    void depositar(double monto) {
        if (monto > 0) {
            saldo += monto;
            cout << "Deposito realizado correctamente" << endl;
        }
        else {
            cout << "El monto debe ser mayor a cero" << endl;
        }
    }

    // Retirar dinero
    void retirar(double monto) {
        if (monto > 0 && monto <= saldo) {
            saldo -= monto;
            cout << "Retiro realizado correctamente" << endl;
        }
        else {
            cout << "No se puede retirar" << endl;
        }
    }
};

int main() {

    CuentaBancaria c("Ana", 100);

    cout << c.ver_titular() << " "
         << c.ver_saldo() << endl;

    c.depositar(50);

    cout << c.ver_titular() << " "
         << c.ver_saldo() << endl;

    c.retirar(500);

    cout << c.ver_titular() << " "
         << c.ver_saldo() << endl;

    c.retirar(30);

    cout << c.ver_titular() << " "
         << c.ver_saldo() << endl;

    return 0;
}