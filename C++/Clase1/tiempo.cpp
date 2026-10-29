

#include <iostream>

using namespace std;

int main() {
    int totalsegundos;
    cout << "Introduzca l¿todos los segundos que quiere convertir: " << endl;
    cin >> totalsegundos;
    // 3600 segundos = 1 hora
    int horas = totalsegundos / 3600;
    int residuo = totalsegundos % 3600;
    
    int minutos = residuo / 60;
    int segundos = residuo % 60;

    cout << "Tienes horas: " << horas << endl;
    cout << "Tienes horas: " << minutos << endl;
    cout << "Tienes segundos: " << segundos << endl;

    return 0;
    }