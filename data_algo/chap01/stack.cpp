#define SMAX 10
#include <iostream>
#include <stdlib.h>
using namespace std;

struct stack {
    char box[SMAX + 1];
    int top;
};

void initialize(struct stack *s) { s->top = 0; }

void push(struct stack *s, char item) { s->box[++s->top] = item; }

void pop(struct stack *s) { --s->top; }

int empty(struct stack *s) { return (s->top == 0); }

char top(struct stack *s) { return (s->box[s->top]); }

#define CHAR_LEN 30
// カッコの整合
bool check_parenthesis(char str[CHAR_LEN]) {
    struct stack parenthesis;
    initialize(&parenthesis);
    for(int i = 0; i < CHAR_LEN; i++) {
        if(str[i] == '(') {
            push(&parenthesis , '(');
        } else if(str[i] == ')'){
            if (empty(&parenthesis)){
                return false;
            } else {
                pop(&parenthesis);
            }
        }
    }
    if (empty(&parenthesis)) return true;
    return false;
}


int main(void) {
    struct stack test_stack;
    initialize(&test_stack);
    cout << (int)top(&test_stack) << endl;
    push(&test_stack, (char)114);
    cout << (int)top(&test_stack) << endl;
    push(&test_stack, (char)37);
    cout << (int)top(&test_stack) << endl;
    push(&test_stack, (char)33);
    cout << (int)top(&test_stack) << endl;
    pop(&test_stack);
    cout << (int)top(&test_stack) << endl;
    pop(&test_stack);
    cout << (int)top(&test_stack) << endl;
    char str[CHAR_LEN];
    cin >> str;
    cout << check_parenthesis(str);
}

