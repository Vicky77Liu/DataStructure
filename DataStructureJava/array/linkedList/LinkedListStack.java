public class LinkedListStack<E> implements Stack<E>{
    private LinkedList<E> list;
    public LinkedListStack(){
        list = new LinkedList<>();
    }
    @Override
    public int getSize(){
        return list.getSize();
    }

    @Override
    public boolean isEmpty(){
        return list.isEmpty();
    }

    @Override
    // 链表头设置为栈顶
    public void push(E e){
        list.addFirst(e);
    }

    @Override
    public E pop(){
        return list.removeFirst();
    }

    @Override
    public E peek(){
        return list.getFirst();
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append("LkList Stack Top :");
        res.append(list);
        return res.toString();
    }
    public static void  main(String[] args){

        LinkedListStack<Integer> stack = new LinkedListStack<>();
        for (int i = 0;i < 5;i++){
            stack.push(i);
            System.out.println(stack);
        }
        stack.pop();
        System.out.println(stack);

    }
}
