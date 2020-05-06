#include <iostream>

using namespace std;

double power(double x, int k){
    double powered = x;
    for(int i = 0; i < k; i++) {
        powered = powered * powered;
    }
    return powered;
}

double power_recursive(double x, int k){
    if (k==0){
        return x;
    } else {
        double powered = power_recursive(x, k-1);
        return powered * powered;
    }
}
int main(void) {
    double x;
    int k;
    char recursive;
    cout << "x: ";
    cin >> x;
    cout << "k: ";
    cin >> k;
    if(k < 0) {
        cout << "error" << endl;
        return 0;
    } 

    
    while (true){
        cout << "recursive? [y/n]: ";
        cin >> recursive;
        if (recursive == 'y'){
            cout << x << "^" << "(2^" << k << ")=" << power_recursive(x,k) << endl;
            break;
        } else if (recursive == 'n'){
            cout << x << "^" << "(2^" << k << ")=" << power(x,k) << endl;
            break;
        } else {
            cout << "response must be y or n" << endl;
        }
    }


    

}