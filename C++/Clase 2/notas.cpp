

#include <iostream>

using namespace std;

int main() {

    int nota;

   cout << "Ingrese un nota: "<< endl;
   cin >> nota;
   if (nota >= 90){
        cout  << "Excelente" << endl;
    }    
    else if (nota >= 61){ 
        cout  << "Aprobado" << endl;
    }
        else {
        cout << "Reprobado" << endl;     
    }   
    return 0;

}