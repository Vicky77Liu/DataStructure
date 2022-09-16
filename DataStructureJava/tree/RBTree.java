import java.util.ArrayList;

public class RBTree <K extends Comparable<K>, V>{
    private static final boolean RED = true;
    private static final boolean BLACK = false;

    private class Node{
        public K key;
        public V value;
        public Node left,right;
        public boolean color;

        public Node(K key, V value){
            this.key = key;
            this.value = value;
            left = null;
            right = null;
            color = RED;
        }
    }
    private Node root;
    private int size;

    public RBTree(){
        root = null;
        size = 0;
    }
    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public boolean isRed(Node node){
        if(node == null)
            return BLACK;
        return node.color;
    }
    //对节点node进行向左旋转操作。返回旋转后的新的根节点x
    //  node                               x
//     /  \                               /  \
//    T1   x                            node  T3
//        /  \        左旋转>>>>        /  \
//       T2  T3                        T1  T2

    private Node leftRotate(Node node){
        Node x = node.right;

        // 左旋转
        node.right = x.left;
        x.left = node;

        x.color = node.color;
        node.color = RED;
        return x;
    }
    //对节点node进行向右旋转操作。返回旋转后的新的根节点x
    //  node                               x
//     /  \                               /  \
//    x   T2                             y   node
//   /  \        右旋转>>>>                   /  \
//  y   T1                                  T1  T2

    private Node rightRotate(Node node){
        Node x = node.left;

        // 右旋转
        node.left = x.right;
        x.right = node;

        x.color = node.color;
        node.color = RED;
        return x;
    }
    //颜色翻转
    private void filpColors(Node node){
        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;
    }

    public void add(K key, V value){
        root = add(root,key,value);
        root.color = BLACK; //最终根节点为黑色
    }

    // 以node为根节点，返回插入元素(key, value)后新的红黑树树的根
    private Node add(Node node,K key,V value){
        if (node == null){
            size ++;
            return new Node(key, value);
        }

        if (key.compareTo(node.key) < 0)
            node.left = add(node.left,key, value);
        else if(key.compareTo(node.key) > 0)
            node.right = add(node.right,key,value);
        else
            node.value = value;

        if(isRed(node.right)  && !isRed(node.left))
            node = leftRotate(node);

        if(isRed(node.left)  && isRed(node.left.left))
            node = rightRotate(node);

        if(isRed(node.left)  && isRed(node.right))
            filpColors(node);

        return node;
    }
    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        generateBSTString(root,0,res);
        return res.toString();
    }
    private void generateBSTString(Node node,int depth,StringBuilder res){
        if(node == null){
            res.append(generatDepthString(depth) + "null\n");
            return;
        }
        res.append(generatDepthString(depth) + node.key +"\n");
        generateBSTString(node.left,depth+1,res);
        generateBSTString(node.right,depth+1,res);

    }
    private String generatDepthString(int depth){
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < depth; i ++)
            res.append("--");
        return res.toString();
    }

}