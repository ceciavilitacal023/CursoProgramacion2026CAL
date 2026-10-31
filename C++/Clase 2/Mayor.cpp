

#include <iostream>

using namespace std;

int main() {

    int num1, num2;

   cout << "Ingrese el numero 1: "<< endl;
   cin >> num1;
   cout << "Ingrese el numero 2: "<< endl;
   cin >> num2;
   if (num1 == num2){
        cout  << "Son iguales" << endl;
    
    } else if (num1 > num2){
        cout  << "El num1 es mayor" << endl;

    } else {
        cout  << "El num2 es mayor" << endl;
    }
    return 0;

}