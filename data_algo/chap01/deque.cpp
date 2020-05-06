# define QMAX 20
struct queue {
    char box[QMAX+1]:
    int front, rear;
}

void initialize(struct queue *q){
    q->front = 1;
    q->rear = 0;
}

void insert_rear(struct queue *q, char item){
    q->box[++q->rear] = item; // キューへ要素を挿入
}
void insert_front(struct queue *q, char item){
    q->box[q->front--] = item; // キューへ要素を挿入
}

void insert_rear_circle(struct queue *q, char item){
   q->box[q->rear] = item;  
   q->rear = q->rear % QMAX;
}
void insert_front_circle(struct queue *q, char item){
   q->box[q->front - 1] = item;  
   q->front =( q->front - 1 )% QMAX;
}

void delete_element_front(struct queue*q){
    ++q->front;
}

void delete_element_rear(struct queue *q){
    --q->rear;
}

void delete_circle_rear(struct queue *q){
    q->rear = (q->rear - 1 )% QMAX;
}

void delete_circle_front(struct queue *q){
    q->front = (q->front + 1 )% QMAX;
}

int empty(struct queue *q){
    return (q->rear < q->front)
}

char top(struct queue *q){
    return (q->box[q->front]);
}

char bottom(struct queue *q){
    return (q->box[q->reat]);
}