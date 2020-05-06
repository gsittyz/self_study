#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
struct element {
    char data;
    struct element *next;
};

struct element *create_new() {
    return ((struct element *)malloc(sizeof(struct element)));
}
struct element *create() {
    struct element *p;
    p = create_new();
    p->next = NULL;
    return (p);
}

void insert(struct element *l, int k, char item) {
    struct element *p;
    if(k > 1)
        insert(l->next, k - 1, item);
    else {
        p = create_new();
        p->data = item;
        p->next = l->next;
        l->next = p;
    }
}

void insert_non_recursive(struct element *l, int k, char item) {
    struct element *new_element = create();
    new_element->data = item;
    struct element *target_next = l->next;
    struct element *target_prev = l;
    for(int i = 0; i < k - 1; i++) {
        target_next = target_next->next;
        target_prev = target_prev->next;
    }
    new_element->next = target_next;
    target_prev->next = new_element;
}

void delete_element(struct element *l, int k) {
    if(k > 1)
        delete_element(l->next, k - 1);
    else
        l->next = l->next->next;
}

void delete_element_non_recursive(struct element *l, int k) {
    struct element *target_prev = l;
    for(int i = 0; i < k - 1; i++) {
        target_prev = target_prev->next;
    }
    target_prev->next = target_prev->next->next;
}

void delete_all(struct element *l, char a) {
    if(l->next == NULL) {
        return;
    } else if(l->next->data == a) {
        l->next = l->next->next;
        delete_all(l, a);
    } else {
        delete_all(l->next, a);
    }
}

void delete_all_recursive(struct element *l, char a) {
    struct element *target = l->next;
    struct element *target_prev = l;
    while(target != NULL) {
        if(target->data == a) {
            target_prev->next = target->next->next;
            target_prev = target;
            target = target->next->next;
        } else {
            target_prev = target;
            target = target->next;
        }
    }
}

char access(struct element *l, int k) {
    if(k > 1)
        return (access(l->next, k - 1));
    else
        return (l->next->data);
}

char access_non_recursive(struct element *l, int k) {
    struct element *target = l;
    for(int i = 0; i < k; i++) {
        target = target->next;
    }
    return target->data;
}

void reverse(struct element *l) {
    struct element *prev = NULL;
    struct element *current = l->next;
    struct element *next;
    while(current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    l->next = prev;
}
bool member(struct element *l, char a) {
    if(l->next == NULL) {
        return false;
    } else if(l->next->data == a) {
        return true;
    } else {
        return member(l->next, a);
    }
}

bool member_recursive(struct element *l, char a) {
    struct element *target = l;
    while(l->next != NULL) {
        if(target->next->data == a) {
            return true;
        }
    }
    return false;
}

int main(void) {
    struct element *test_element = create();
    cout << &(test_element->data) << endl;
    // test_element->data = 100;
    // insert(test_element,0,101);
    insert_non_recursive(test_element, 1, 102);
    insert_non_recursive(test_element, 2, 103);
    insert_non_recursive(test_element, 2, 105);

    // cout << "a" << test_element.data << endl;
    // cout << 0 << (int)access(test_element,0) << endl;
    cout << 1 << (int)access(test_element, 1) << endl;
    cout << 2 << (int)access(test_element, 2) << endl;
    cout << 3 << (int)access(test_element, 3) << endl;

    reverse(test_element);

    // cout << 0 << (int)access(test_element,0) << endl;
    cout << 1 << (int)access(test_element, 1) << endl;
    cout << 2 << (int)access(test_element, 2) << endl;
    cout << 3 << (int)access(test_element, 3) << endl;

    return 0;
}