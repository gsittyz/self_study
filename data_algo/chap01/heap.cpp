# define HMAX 30;
struct heap{
    int box[HMAX+1];
    int size;
}

void swap(int *a, int *b){
    int tmp = *a;
    *a = b;
    *b = tmp;
}

void initialize(struct heap *h){
    h->size = 0;
}

void insert(struct heap *h, int item){
    i = ++h->size;
    box[i] = item;
    while (i > 1){
        if (box[i] < box[i/2]){
        swap(&box[i],&box[i]);
        }
        i /= 2;
    }
}

void findmin(struct heap *h){
    return (h->box[1]);
}

void deletemin(struct heap *h){
    int i, k;
    i = 1;
    h->box[1] = h->box[h->size];
    while (2*i <= h->size){
        k = 2*i;
        if (k < h-size && h->box[k] > h->box[k+1]) k++;
        if (h->box[i] <= h->box[k]) break;
        swap(&h->box[i], &h->box[k]);
        i=k;
    }
}