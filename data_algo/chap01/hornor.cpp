#include <iostream>
using namespace std;

int main(void){
    int n;
    cout << "多項式の次数: "; cin >> n;
    double a[n];
    for (int i =0; i <= n; i++){
        cout << "a_" << n-i << ": "; cin >> a[n-i];
    }
    cout << "多項式p(x)=";
    for (int i=0; i<= n; i++){
        if(i < n){
            cout << a[n-i] << "x^" << n-i << "+";
        }else{
            cout << a[n-i] << endl;
        }
    }
    double x;
    cout << "x: "; cin >> x;
    double sum = a[n];
    for (int i=0; i<n; i++){
        sum = sum * x + a[n-i-1];
    }
    for (int i=0; i<= n; i++){
        if(i < n){
            cout << a[n-i] << "*" << x << "^" << n-i << "+";
        }else{
            cout << a[n-i] << "=" << sum << endl;
        }
    }

    return 0;
}