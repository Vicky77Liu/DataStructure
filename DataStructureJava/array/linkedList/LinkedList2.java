
public class LinkedList2 <E>{
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
    private Node head;
    private int size;
    public LinkedList2(){
        head = null;
        size = 0;
    }

    public int getSize(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    // 对外方法，在链表的index处添加新的元素e
    public void add(int index,E e){
        if (index < 0 || index > size)
            throw new IllegalArgumentException("add failed,Illegal index");
        head = add(head,index,e);
        size ++;
    }
    // 在以node为头节点的链表index位置插入元素e
    private Node add(Node node,int index,E e){
        if (index == 0)
            return new Node(e,node);
        node.next = add(node.next,index-1,e);
        return node;
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
        return get(head,index);
    }
    private E get(Node node,int index){
        if (index == 0){
            return node.e;
        }
        return get(node.next,index-1);
    }

    public E getFirst() {
        return get(0);
    }

    public E getLast(E e) {
        return get(size - 1);
    }

    public void set(int index, E e){
        if (index <0 || index >= size)
            throw new IllegalArgumentException("set failed,Illegal index");
        set(head,index,e);
    }
    private void set(Node node,int index,E e){
        if (index == 0){
            node.e = e;
            return;
        }
        set(node.next,index-1,e);

    }

    public boolean contains(E e){
        return contains(head,e);
    }
    private boolean contains(Node node,E e){
        if (node == null)
            return false;
        if (node.e.equals(e))
            return true;
        return contains(node.next,e);
    }

//    public E remove(int index){
//        if (index <0 || index >= size)
//            throw new IllegalArgumentException("delete failed,Illegal index");
//        Pair<Node,E> res = remove(node.next,index - 1);
//        size --;
//        head = res.getKey();
//        return res.getValue();
//    }
//    // 从以node为头节点的链表中删除index位置的元素
//    // 返回值包含两个元素。删除后的头节点和删除的值
//    private Pair<Node,E> remove(Node node,int index){
//        if (index == 0)
//            return new Pair<>(node.next,node.e);
//        Pair<Node,E> res = remove(node.next,index - 1);
//        node.next = res.getKey();
//        return new Pair<>(node,res.getValue());
//    }
//
//    public E removeFirst(){
//        return remove(0);
//    }
//
//    public E removeLast(){
//        return remove(size - 1);
//    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        Node cur = head;
        while(cur != null){
            res.append(cur + "->");
            cur = cur.next;
        }
        res.append("null");
        return res.toString();
    }
}
