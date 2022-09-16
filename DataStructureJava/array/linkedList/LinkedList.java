public class LinkedList <E>{
    private class Node{
        public E e;
        public Node next;

        public Node(E e, Node next){
            this.e = e;
            this.next = next;
        }
        public Node(E e){
            this(e,null);
        }
        public Node(){
            this(null,null);
        }
        @Override
        public String toString(){
            return e.toString();
        }
    }
    private Node dummyhead;
    int size;
    public LinkedList(){
        dummyhead = new Node(null,null);
        size = 0;
    }

    public int getSize(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void add(int index,E e){
        if (index < 0 || index > size)
            throw new IllegalArgumentException("add failed,Illegal index");
        Node prev = dummyhead;
        //从dummyhead开始遍历，找到index前面的哪一个节点
        for (int i = 0; i < index ; i++)
            prev = prev.next;
        prev.next = new Node(e,prev.next);
        size ++;
    }

    public void addFirst(E e){
        add(0,e);
    }

    public void addLast(E e){
        add(size,e);
    }

    public E get(int index){
        if (index <0 || index >= size)
            throw new IllegalArgumentException("get failed,Illegal index");
        Node cur = dummyhead.next;
        for (int i = 0; i < index;i ++)
            cur = cur.next;
        return cur.e;
    }

    public E getFirst() {
        return get(0);
    }

    public E getLast() {
        return get(size - 1);
    }

    public void set(int index, E e){
        if (index <0 || index >= size)
            throw new IllegalArgumentException("set failed,Illegal index");
        Node cur = dummyhead.next;
        for(int i = 0;i < index; i ++)
            cur = cur.next;
        cur.e = e;
    }

    public boolean contains(E e){
        Node cur = dummyhead.next;
        while(cur != null){
            if (cur.e.equals(e))
                return true;
            cur = cur.next;
        }
        return false;
    }

    public E remove(int index){
        if (index <0 || index >= size)
            throw new IllegalArgumentException("delete failed,Illegal index");
        Node prev = dummyhead;
        for(int i = 0;i < index; i ++)
            prev = prev.next;
        Node delNode = prev.next;
        prev.next = delNode.next;
        delNode.next = null;
        size --;
        return delNode.e;
    }

    public E removeFirst(){
        return remove(0);
    }

    public E removeLast(){
        return remove(size - 1);
    }

    public void removeElement(E e) {
        Node pre = dummyhead;
        while (pre.next != null) {
            if (pre.next.e.equals(e))
                break;
            pre = pre.next;
        }
        if (pre.next != null) {
            Node delNode = pre.next;
            pre.next = pre.next.next;
            delNode.next = null;
        }
    }


    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        Node cur = dummyhead.next;
        while(cur != null){
            res.append(cur + "->");
            cur = cur.next;
        }
        res.append("null");
        return res.toString();
    }
}
