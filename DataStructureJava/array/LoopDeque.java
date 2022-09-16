public class LoopDeque <E> implements Deque<E>{
    private E[] data;
    private int front, tail;
    private int size;

    public LoopDeque(int capacity){
        data = (E[]) new Object[capacity];
        front = 0;
        tail = 0;
        size = 0;
    }
    public LoopDeque(){
        this(10);
    }
    public int getCapacity(){
        return data.length;

    }
    @Override
    public int getSize(){
        return size;
    }

    @Override
    public boolean isEmpty(){
        return size == 0;
    }

    @Override
    public void addFirst(E e){
        if (size == getCapacity())
            resize(getCapacity() * 2);
        // 首先要确定front位置，如果front-1==0 ，则是data.length - 1
        if (front == 0)
            front = data.length - 1;
        else front = front-1;
        data[front] = e;
        size ++;
    }

    @Override
    public void addLast(E e){
        if (size == getCapacity())
            resize(getCapacity() * 2);
        data[tail] = e;
        tail = (tail + 1) % data.length;
        size ++;
    }

    @Override
    public E removeFirst(){
        if (isEmpty())
            throw new IllegalArgumentException("can not remove from an empty deque");
        E ret = data[front];
        data[front] = null;
        front = (front+1) % data.length;
        size --;
        if (size == getCapacity() / 4 && getCapacity() / 2 !=0){
            resize(getCapacity()/2);
        }
        return ret;
    }
    @Override
    public E removeLast(){
        if (isEmpty())
            throw new IllegalArgumentException("can not remove from an empty deque");
        // 计算新的tail的位置
        tail = tail == 0? data.length -1:tail -1;
        E ret = data[tail];
        data[tail] = null;
        size --;
        if (size == getCapacity() / 4 && getCapacity() / 2 !=0){
            resize(getCapacity()/2);
        }
        return ret;
    }

    @Override
    public E getFront(){
        if (isEmpty())
            throw new IllegalArgumentException("deque is empty");
        return data[front];
    }

    @Override
    public E getLast(){
        if (isEmpty())
            throw new IllegalArgumentException("deque is empty");
        return data[tail];
    }

    private void resize(int newcapacity){
        E[] newData = (E[]) new Object[newcapacity];
        for (int i = 0; i < size; i++){
            newData[i]  = data[(i + front) % data.length];
        }
        data = newData;
        front = 0;
        tail = size;
    }
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append(String.format("Deque : size = % d, capacity = %d\n", getSize(),getCapacity()));
        res.append("front[");
        for (int i =0; i < size;i ++) {
            res.append(data[(i+front) % data.length]);
            if (i != size - 1) {
                res.append(",");
            }
        }
        res.append("] tail");
        return res.toString();
    }

    public static void main(String[] args){
        Deque<Integer> dq = new LoopDeque<>();
        for (int i = 0;i < 16;i ++){
            if (i % 2 == 0)
                dq.addLast(i);
            else dq.addFirst(i);
            System.out.println(dq);
        }
    }
}
