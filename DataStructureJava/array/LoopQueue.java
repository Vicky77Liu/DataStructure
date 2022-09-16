public class LoopQueue <E> implements Queue<E>{
    private E[] data;
    private int front,tail;
    private int size;

    public LoopQueue(int capacity){
        data = (E[]) new Object[capacity];
        front = 0;
        tail = 0;
        size = 0;
    }
    public LoopQueue(){
        this(10);
    }

    public int getCapacity(){
        return data.length;
    }

    @Override
    public boolean isEmpty(){
        return size == 0;
    }

    @Override
    public int getSize(){
        return size;
    }

    @Override
    public void enqueue(E e){
        if(size == getCapacity())
            resize(getCapacity() * 2);

        data[tail] = e;
        tail = (tail + 1) % data.length;
        size ++;
    }

    @Override
    public E dequeue(){
        if (isEmpty()){
            throw new IllegalArgumentException("Can not dequeue from an empty queue");
        }
        E ret = data[front];
        data[front] = null;
        front = (front + 1) % data.length;
        size --;
        if (size == getCapacity() / 4 && getCapacity() / 2 != 0)
            resize(getCapacity()/2);
        return ret;
    }

    @Override
    public E getFront(){
        if (isEmpty()){
            throw new IllegalArgumentException("Queue is empty");
        }
        return data[front];
    }

    private void resize(int newCapacity){
        E[] newData = (E[]) new Object[newCapacity];
        for (int i = 0;i < size; i ++){
            newData[i] = data[(i + front) % data.length];
        }
        data = newData;
        front = 0;
        tail = size;
    }

    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append("Queue");
        res.append("front[");
        for (int i =0; i < size;i ++) {
            res.append(data[i]);
            if ((i+front+1) % data.length != tail) {
                res.append(",");
            }
        }
        res.append("] tail");
        return res.toString();
    }
}
