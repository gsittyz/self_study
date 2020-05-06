#include <cstdio>
#include <iostream>
#define NUM_MAX 10
using namespace std;
struct hanoi {
    int abc[3][NUM_MAX];
    int abc_top[3];
};

void print_hanoi(struct hanoi *target) {
    int i, j;
    for(i = 0; i < 3; i++) {
        j = 0;
        do {
            printf("%d ", target->abc[i][j]);
            j++;
        } while(target->abc[i][j] > 0);
        printf("\n");
    }
    printf("\n");
}

void hanoi_solve(struct hanoi *target, int num, int from, int to, int tmp) {
    int *from_top;
    from_top = &target->abc_top[from];
    int *to_top;
    to_top = &target->abc_top[to];
    int *tmp_top;
    tmp_top = &target->abc_top[tmp];

    if(num == 1) {
        printf("%d: %d -> %d \n", target->abc[from][*from_top], from, to);
        target->abc[to][++*to_top] = target->abc[from][*from_top];
        target->abc[from][*from_top] = 0;
        *from_top = *from_top - 1;
        print_hanoi(target);
    } else {
        hanoi_solve(target, num - 1, from, tmp, to);
        printf("%d: %d -> %d \n", target->abc[from][*from_top], from, to);
        target->abc[to][++*to_top] = target->abc[from][*from_top];
        target->abc[from][*from_top] = 0;
        *from_top = *from_top - 1;
        // from -> to に移す
        print_hanoi(target);
        hanoi_solve(target, num - 1, tmp, to, from);
    }
}

int main(void) {
    struct hanoi h;
    int num;
    // memset(&h, 0, sizeof(h));
    cout << "number of plates: ";
    cin >> num;

    // h.abc_top = {0};
    h.abc_top[0] = num - 1;
    h.abc_top[1] = -1;
    h.abc_top[2] = -1;

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < NUM_MAX; j++) {
            if(i == 0 && j < num) {
                h.abc[i][j] = num - j;
            } else {
                h.abc[i][j] = 0;
            }
        }
    }
    print_hanoi(&h);
    hanoi_solve(&h, num, 0, 1, 2);
}