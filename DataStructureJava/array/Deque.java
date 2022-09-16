public interface Deque <E>{
    int getSize();
    boolean isEmpty();
    void addFirst(E e);
    void addLast(E e);
    E removeFirst();
    E removeLast();
    E getFront();
    E getLast();
}
