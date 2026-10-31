

#include <iostream>

using namespace std;

int main(){
    int nota;
    cout << "Ingrese una nota valida"<< endl;
    cin >> nota;

    if(nota >=0 && nota <= 100){
        cout << "nota valida"<<endl;
    }
    return 0;
}