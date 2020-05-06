#include <iostream>

using namespace std;

double power(double x, int n) {
    double powered = x;
    int bit[15] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int k = 0;
    while(n > 0) {
        k++;
        bit[15 - k] = n % 2;
        n = n / 2;
    }
    // 一桁目は無視しなくてはならない
    for(int i = 15 - k + 1; i < 15; i++) {
        if(bit[i] == 0) {
            powered = powered * powered;
        } else {
            powered = powered * powered * x;
        }
    }
    return powered;

    // for(int i = 0; i < n; i++) {
    //     powered = powered * powered;
    // }
    // return powered;
}

double power_recursive(double x, int n) {
    if(n == 0) {
        return 1;
    } else if(n == 1) {
        return x;
    } else {
        int res = n % 2;
        double powered = power_recursive(x, n / 2);
        if(res == 1) {
            return powered * powered * x;
        } else {
            return powered * powered;
        }
    }
}
int main(void) {
    double x;
    int n;
    char recursive;
    cout << "x: ";
    cin >> x;
    cout << "n: ";
    cin >> n;
    if(n < 0) {
        cout << "error" << endl;
        return 0;
    }

    while(true) {
        cout << "recursive? [y/n]: ";
        cin >> recursive;
        if(recursive == 'y') {
            cout << x << "^" << n << "=" << power_recursive(x, n) << endl;
            break;
        } else if(recursive == 'n') {
            cout << x << "^" << n << "=" << power(x, n) << endl;
            break;
        } else {
            cout << "response must be y or n" << endl;
        }
    }
}