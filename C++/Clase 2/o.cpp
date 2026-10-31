
#include <iostream>

using namespace std;

int main(){
    int dia;
    cout << "Ingrese un dia"<< endl;
    cin >> dia;

    if(dia ==6 ||dia == 7){
        cout << "es fin de semana"<<endl;
    } else cout <<"Es día de semana"<<endl;
    return 0;
}