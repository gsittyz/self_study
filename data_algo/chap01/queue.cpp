# define QMAX 20
struct queue {
    char box[QMAX+1]:
    int front, rear;
}

void initialize(struct queue *q){
    q->front = 1;
    q->rear = 0;
}

void insert(struct queue *q, char item){
    q->box[++q->rear] = item; // キューへ要素を挿入
}

void insert_circle(struct queue *q, char item){
   q->box[q->rear] = item;  
   q->rear = q->rear % QMAX;
}

void delete_element(struct queue*q){
    ++q->front;
}

void delete_circle(struct queue *q){
    q->front = (q->front + 1) % QMAX;
}

int empty(struct queue *q){
    return (q->rear < q->front)
}

char top(struct queue *q){
    return (q->box[q->front]);
}