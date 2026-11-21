

#include <iostream>
#include <string>
using namespace std;

class Producto {
private:
    string nombre;
    double precio;
    int stock;

public:
    // Constructor
    Producto(string nom, double pre, int cantidad) {
        nombre = nom;
        precio = pre;
        stock = cantidad;
    }

    // Metodo para mostrar los datos
    void mostrar() {
        cout << nombre << " - Bs " << precio
             << " - Stock: " << stock << endl;
    }

    // Metodo para vender productos
    void vender(int cantidad) {
        if (cantidad > 0 && cantidad <= stock) {
            stock = stock - cantidad;
            cout << "Venta realizada" << endl;
        }
        else {
            cout << "No hay suficiente stock o cantidad invalida" << endl;
        }
    }

    // Metodo para calcular el valor total
    double valor_total() {
        return precio * stock;
    }
};

int main() {

    // Crear dos productos
    Producto producto1("Arroz", 8.5, 20);
    Producto producto2("Azucar", 7, 15);

    // Mostrar productos
    cout << "--- PRODUCTOS INICIALES ---" << endl;
    producto1.mostrar();
    producto2.mostrar();

    // Realizar ventas
    cout << "\n--- REALIZAR VENTAS ---" << endl;
    producto1.vender(5);
    producto2.vender(20);

    // Mostrar stock actualizado
    cout << "\n--- STOCK ACTUALIZADO ---" << endl;
    producto1.mostrar();
    producto2.mostrar();

    // Calcular valor total del stock
    cout << "\n--- VALOR TOTAL DEL STOCK ---" << endl;

    cout << "Valor total del arroz: Bs "
         << producto1.valor_total() << endl;

    cout << "Valor total del azucar: Bs "
         << producto2.valor_total() << endl;

    return 0;
}