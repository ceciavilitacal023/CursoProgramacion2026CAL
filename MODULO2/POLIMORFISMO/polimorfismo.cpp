

#include <iostream>
using namespace std;

// Clase padre
class Figura {
public:
    virtual double area() {
        return 0;
    }
};

// Clase hija Rectangulo
class Rectangulo : public Figura {
private:
    double b, h;

public:
    Rectangulo(double base, double altura) {
        b = base;
        h = altura;
    }

    double area() override {
        return b * h;
    }
};

// Clase hija Circulo
class Circulo : public Figura {
private:
    double r;

public:
    Circulo(double radio) {
        r = radio;
    }

    double area() override {
        return 3.14 * r * r;
    }
};

// Programa principal
int main() {

    Figura* figuras[] = {
        new Rectangulo(3, 4),
        new Circulo(2),
        new Rectangulo(5, 1)
    };

    for (int i = 0; i < 3; i++) {
        cout << figuras[i]->area() << endl;
    }

    // Liberar memoria
    for (int i = 0; i < 3; i++) {
        delete figuras[i];
    }

    return 0;
}