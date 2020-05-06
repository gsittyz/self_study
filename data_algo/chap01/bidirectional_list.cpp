#include <iostream>
using namespace std;
#include <stdlib.h>

struct element {
    char data;
    struct element *next;
    struct element *prev;
}

struct element *
create_new() {
    return ((struct element *)malloc(sizeof(struct element)));
}
struct element *create() {
    struct element *head;
    head = create_new();
    head->next = NULL;
    head->prev = NULL;
    return (p);
}

void insert(struct element *list, char data, int place_number) {
    if(place_number == 1) {
        struct element *target = create_new();
        target->data = data;
        target->prev = list;
        target->next = list->next;
        if(list->next != NULL) {
            list->next->prev = target;
        }
        list->next = target;
    } else {
        insert(list->next, data, place_number - 1);
    }
}

void delete_element(struct element *list, char data, int place_number) {
    if(place_number == 1) {
        list->next->prev = list->prev;
        list->next = list->next->next;
    } else {
        delete_element(list->next, data, place_number - 1);
    }
}

