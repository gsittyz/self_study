#include <iostream>

using namespace std;

int gcd(int x, int y) {
    int res = x % y;
    while(res != 0) {
        x = y;
        y = res;
        res = x % y;
    }
    return y;
}

int gcd_recursive(int x, int y) {
    int res = x % y;
    if(res == 0) {
        return res;
    } else {
        return gcd_recursive(y, res);
    }
}

int main(void) {
    int x, y;
    char recursive;
    cout << "x: ";
    cin >> x;
    cout << "y: ";
    cin >> y;
    while(true) {
        cout << "recursive? [y/n]";
        cin >> recursive;
        if(recursive == 'y') {
            cout << gcd(x, y) << endl;
            break;
        } else if(recursive == 'n') {
            cout << gcd(x, y) << endl;
            break;
        } else {
            cout << "resopnse must be in y or n" << endl;
        }
    }

    return 0;
}