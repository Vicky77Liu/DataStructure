import java.util.ArrayList;

public class AVLTree <K extends Comparable<K>, V>{

    private class Node{
        public K key;
        public V value;
        public Node left,right;
        public int height;

        public Node(K key, V value){
            this.key = key;
            this.value = value;
            left = null;
            right = null;
            height = 1;
        }
    }
    private Node root;
    private int size;

    public AVLTree(){
        root = null;
        size = 0;
    }
    public int size(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    //判断该二叉树是否是一颗二分搜索树
    public boolean isBST(){
        ArrayList<K> keys = new ArrayList<>();
        inOrder(root, keys);
        for(int i = 1; i < keys.size(); i++)
            if (keys.get(i-1).compareTo(keys.get(i)) > 0)
                return false;
        return true;
    }

    private void inOrder(Node node, ArrayList<K> keys){
        if(node == null)
            return ;
        inOrder(node.left, keys);
        keys.add(node.key);
        inOrder(node.right, keys);
    }

    //判断该二叉树是否是一颗平衡二叉树
    public boolean isBalanced(){
        return isBalanced(root);
    }
    private boolean isBalanced(Node node){
        if(node == null)
            return true;
        int balanceFactor = getBalanceFactor(node);
        if (Math.abs(balanceFactor) > 1)
            return false;
        return isBalanced(node.left) && isBalanced(node.right);
    }

    //获得节点node的高度
    private int getHeight(Node node){
        if (node == null)
            return 0;
        return node.height;
    }

    //获得节点node的平衡因子
    private int getBalanceFactor(Node node){
        if (node == null)
            return 0;
        return getHeight(node.left) - getHeight(node.right);
    }
//      对节点y进行向右旋转操作。返回旋转后的新的根节点x
//        y                                    x
//       /  \                                /   \
//       x   T4                             z      y
//      /  \        右旋转>>>>             /  \    /  \
//     z  T3                             T1  T2  T3  T4
//     / \
//   T1  T2
    private Node rightRotate(Node y){
        Node x = y.left;
        Node T3 = x.right;
        // 向右旋转的过程
        x.right = y;
        y.left = T3;

        // 更新height，先更新y的高度值
        y.height = Math.max(getHeight(y.left), getHeight(y.right)) + 1;
        x.height = Math.max(getHeight(x.left), getHeight(x.right)) + 1;
        return x;
    }

//   对节点y进行向左旋转操作。返回旋转后的新的根节点x
//      y                                   x
//     /  \                                /  \
//    T1   x                             y      z
//        /  \        左旋转>>>>        /  \    /  \
//       T2  z                        T1  T2   T3  T4
//           / \
//          T3  T4
    private Node leftRotate(Node y){
        Node x = y.right;
        Node T2 = x.left;
        // 向右旋转的过程
        x.left = y;
        y.right = T2;

        // 更新height
        y.height = Math.max(getHeight(y.left), getHeight(y.right)) + 1;
        x.height = Math.max(getHeight(x.left), getHeight(x.right)) + 1;
        return x;
    }


    public void add(K key, V value){
        root = add(root,key,value);
    }
    // 以node为根节点，返回插入元素后新的树的根
    private Node add(Node node,K key,V value){
        if (node == null){
            size ++;
            return new Node(key, value);
        }

        if (key.compareTo(node.key) < 0)
            node.left = add(node.left,key, value);
        else if(key.compareTo(node.key) > 0)
            node.right = add(node.right,key, value);
        else
            node.value = value;

        //更新height
        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));

        // 计算平衡因子
        int balanceFactor = getBalanceFactor(node);
        if (Math.abs(balanceFactor) > 1)
            System.out.println("unbalanced");

        //平衡维护
        // LL，插入的元素在不平衡的节点的左侧的左侧
        if(balanceFactor > 1 && getBalanceFactor(node.left) >= 0)
            return rightRotate(node);

        //RR，插入的元素在不平衡的节点的右侧的右侧
        if(balanceFactor < -1 &&getBalanceFactor(node.right) <=0)
            return leftRotate(node);

        //LR，插入的元素在不平衡的节点的左侧的右侧
        //先转成LL
        if(balanceFactor > 1 && getBalanceFactor(node.left) < 0){
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        //RL，插入的元素在不平衡的节点的右侧的左侧
        //先转成RR
        if(balanceFactor < -1 && getBalanceFactor(node.right) > 0){
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    public V minimum(){
        if (size == 0)
            throw new IllegalArgumentException(("BST is empty"));
        return minimum(root).value;
    }

    private Node minimum(Node node){
        if (node.left == null)
            return node;
        return minimum(node.left);
    }

    // 返回以node为节点的二分搜索树中key为key的节点
    private E getNode(Node node, K key){
        if (node == null)
            return null;
        if (key.compareTo(node.key) == 0)
            return node;
        else if (key.compareTo(node.key) < 0)
            return getNode(node.left,key);
        else
            return getNode(node.right,key);
    }
    // 从二分搜索树中删除key的节点
    public void remove(K key){
        Node node = getNode(root, key);
        if node:
            root = remove(root,key);
            return node.value;
        return null;
    }
    // 删除以node为根节点的二分搜索树中key的节点
    // 返回删除节点后新的二分搜索树的根
    private Node remove(Node node, K key) {
        if (node == null)
            return null;
        Node retNode;
        if (key.compareTo(node.key) < 0) {
            node.left = remove(node.left, key);
            retNode =  node;
        } else if (key.compareTo(node.key) > 0) {
            node.right = remove(node.right, key);
            retNode =  node;
        } else { // ==
            // 待删除的节点左子树为空
            if (node.left == null) {
                Node rightNode = node.right;
                node.right = null;
                size--;
                retNode =  rightNode;
            }
            // 待删除的节点右子树为空
            else if (node.right == null) {
                Node leftNode = node.left;
                node.left = null;
                size--;
                retNode =  leftNode;
            }
            // 待删除的节点左右子树都不为空
            // 找到待删除节点右子树的最小节点，用这个节点顶替待删除节点的位置
            else
                {Node successor = minimum(node.right);
                successor.right = remove(node.right, seccessor.key);
                successor.left = node.left;

                node.left = node.right = null;
                retNode =  successor;}
        }
        if(retNode == null)
            return null;

        //更新height
        retNode.height = 1 + Math.max(getHeight(retNode.left), getHeight(retNode.right));

        // 计算平衡因子
        int balanceFactor = getBalanceFactor(retNode);

        //平衡维护
        // LL
        if(balanceFactor > 1 && getBalanceFactor(retNode.left) >= 0)
            return rightRotate(retNode);

        //RR
        if(balanceFactor < -1 &&getBalanceFactor(retNode.right) <=0)
            return leftRotate(retNode);

        //LR; 先转成LL
        if(balanceFactor > 1 && getBalanceFactor(retNode.left) < 0){
            retNode.left = leftRotate(retNode.left);
            return rightRotate(retNode);
        }

        //RL;先转成RR
        if(balanceFactor < -1 && getBalanceFactor(retNode.right) > 0){
            retNode.right = rightRotate(retNode.right);
            return rightRotate(retNode.right);
        }

        return retNode;
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

