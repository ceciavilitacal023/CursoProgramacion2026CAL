
#include <iostream>
#include <string>
using namespace std;

// Clase padre
class Animal {
protected:
    string nombre;

public:
    Animal(string n) {
        nombre = n;
    }

    virtual string hablar() {
        return "...";
    }

    virtual void mostrar() {
        cout << nombre << " dice " << hablar() << endl;
    }

    virtual ~Animal() {}
};

// Clase hija Perro
class Perro : public Animal {
public:
    Perro(string n) : Animal(n) {}

    string hablar() override {
        return "Guau";
    }
};

// Clase hija Gato
class Gato : public Animal {
public:
    Gato(string n) : Animal(n) {}

    string hablar() override {
        return "Miau";
    }
};

// Clase hija Vaca
class Vaca : public Animal {
public:
    Vaca(string n) : Animal(n) {}

    string hablar() override {
        return "Muu";
    }
};

// Clase hija Pato
class Pato : public Animal {
public:
    Pato(string n) : Animal(n) {}

    string hablar() override {
        return "Cuac";
    }
};

// Programa principal
int main() {

    // Crear los objetos
    Perro p1("Firulais");
    Gato g1("Michi");
    Vaca v1("Lola");
    Pato pa1("Donald");

    // Lista de animales
    Animal* animales[] = {
        &p1,
        &g1,
        &v1,
        &pa1
    };

    // Recorrer la lista
    for (int i = 0; i < 4; i++) {
        animales[i]->mostrar();
    }

    return 0;
}