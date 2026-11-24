

#include <iostream>
#include <string>
using namespace std;

// Clase padre
class Personas {
protected:
    string nombre;
    int edad;

public:
    Personas(string nombre, int edad) {
        this->nombre = nombre;
        this->edad = edad;
    }
};

// Clase hija Estudiante
class Estudiante : public Personas {
private:
    string carrera;
    float nota;

public:
    Estudiante(string nombre, int edad, string carrera, float nota)
        : Personas(nombre, edad) {
        this->carrera = carrera;
        this->nota = nota;
    }

    void presentarse() {
        cout << "ESTUDIANTE" << endl;
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
        cout << "Carrera: " << carrera << endl;
        cout << "Nota: " << nota << endl;
    }
};

// Clase hija Docente
class Docente : public Personas {
private:
    string materia;

public:
    Docente(string nombre, int edad, string materia)
        : Personas(nombre, edad) {
        this->materia = materia;
    }

    void presentarse() {
        cout << "DOCENTE" << endl;
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
        cout << "Materia: " << materia << endl;
    }
};

int main() {

    Estudiante e("Pedro", 18, "Sistemas", 85);
    Docente d("Maria", 35, "Programacion");

    e.presentarse();

    cout << "-----------------" << endl;

    d.presentarse();

    return 0;
}