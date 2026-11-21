

#include <iostream>
#include <string>
using namespace std;

class Estudiante {
private:
    string nombre;
    int nota;

public:
    // Constructor
    Estudiante(string nom, double calificacion) {
        nombre = nom;
        nota = calificacion;
    }

    // Ver nombre
    string ver_nombre() {
        return nombre;
    }

    // Ver nota
    int ver_nota() {
        return nota;
    }

    // Cambiar nota
    void cambiar_nota(int notaNueva) {
        if (notaNueva < 0 || notaNueva > 100) {
            cout << "Nota invalida" << endl;
        }
        else {
            nota = notaNueva;
        }
    }

    // Verificar si aprobo
    void aprobo() {
        if (nota >= 61) {
            cout << "Aprobo" << endl;
        }
        else {
            cout << "Reprobo" << endl;
        }
    }
};

int main() {

    Estudiante m("ana", 67);

    cout << m.ver_nombre() << " "
         << m.ver_nota() << endl;

    m.cambiar_nota(45);

    cout << m.ver_nombre() << " "
         << m.ver_nota() << endl;

    m.aprobo();

    return 0;
}