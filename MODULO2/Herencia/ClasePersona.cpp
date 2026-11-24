

#include <iostream>
#include <string>

using namespace std;

// Clase padre
class Personas {
protected:
    string nombre;
    int edad;

    // Usar publico para que la hija pueda heredar el codigo
public:
    // Constructor
    Personas(string nombre, int edad) {
        this->nombre = nombre;
        this->edad = edad;
    }

    // Metodo para presentarse
    virtual void presentarse() {
        cout << "Soy " << nombre << " y tengo "
             << edad << " años" << endl;
    }
};

// Clase hija Estudiante
class Estudiante : public Personas {
private:
    string carrera;
    float nota;

public:
    // Constructor
    Estudiante(string nombre, int edad, string carrera, float nota)
        : Personas(nombre, edad) {

        this->carrera = carrera;
        this->nota = nota;
    }

    // Metodo para presentarse
    void presentarse() override {
        Personas::presentarse();
        cout << "Estudio la carrera de " << carrera << endl;
        cout << "Mi nota es " << nota << endl;
    }
};

// Clase hija Docente
class Docente : public Personas {
private:
    string materia;

public:
    // Constructor
    Docente(string nombre, int edad, string materia)
        : Personas(nombre, edad) {

        this->materia = materia;
    }

    // Metodo para presentarse
    void presentarse() override {
        Personas::presentarse();
        cout << "Enseño " << materia << endl;
    }
};

// Funcion principal
int main() {

    // Crear objeto Estudiante
    Estudiante e("Pedro", 18, "Sistemas", 85);

    cout << "----- ESTUDIANTE -----" << endl;
    e.presentarse();

    cout << "----------------------" << endl;

    // Crear objeto Docente
    Docente d("Maria", 35, "Programacion");

    cout << "----- DOCENTE -----" << endl;
    d.presentarse();

    cout << "-------------------" << endl;

    // Crear objeto Personas
    Personas p("Juan", 21);

    cout << "----- PERSONA -----" << endl;
    p.presentarse();

    return 0;
}