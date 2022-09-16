import java.util.Random;

public class MinHeap<E extends Comparable<E>> {
    private Array<E> data;

    public MinHeap(int capacity) {
        data = new Array<>(capacity);
    }

    public MinHeap() {
        data = new Array<>();
    }

    public MinHeap(E[] arr) {
        data = new Array<>(arr);
        if (arr.length != 1) {
            for (int i = parent(arr.length - 1); i >= 0; i--)
                siftDown(i);
        }
    }

    public int getSize() {
        return data.getSize();
    }

    public boolean isEmpty() {
        return data.isEmpty();
    }

    // 返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    private int parent(int index) {
        if (index == 0) {
            throw new IllegalArgumentException("index - 0 doesn't have parent");
        }
        return (index - 1) / 2;
    }

    // 返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
    private int leftChild(int index) {
        return index * 2 + 1;
    }

    // 返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
    private int rightChild(int index) {
        return index * 2 + 2;
    }

    public void add(E e) {
        data.addLast(e);
        siftUp(data.getSize() - 1);
    }

    private void siftUp(int k) {
        while (k > 0 && data.get(parent(k)).compareTo(data.get(k)) > 0) {
            data.swap(k, parent(k));
            k = parent(k);
        }
    }

    public E findMin() {
        if (data.getSize() == 0) {
            throw new IllegalArgumentException("Can't find min when heap is empty");
        }
        return data.get(0);
    }

    // 取出堆中最小元素
    public E extractMin() {
        E ret = findMin();
        data.swap(0, data.getSize() - 1);
        data.removeLast();
        siftDown(0);
        return ret;
    }

    private void siftDown(int k) {
        while (leftChild(k) < data.getSize()) {
            int j = leftChild(k);
            // 如果右孩子的值小于左孩子的值，
            if (j + 1 < data.getSize() && data.get(j + 1).compareTo(data.get(j)) < 0)
                j++; // j = rightChild(k)
            // 此时 j 是左右孩子中的最小值
            if (data.get(k).compareTo(data.get(j)) <= 0)
                break;
            data.swap(k, j);
            k = j;
        }
    }

    //  取出堆中最小的元素，并且替换成元素e
    public E replace(E e) {
        E ret = findMin();
        data.set(0, e);
        siftDown(0);
        return ret;
    }

    public static void main(String[] args) {
        int n = 10000;
        MinHeap<Integer> minHeap = new MinHeap<>();
        Random rnd = new Random();
        for(int i = 0; i < n; i ++)
            minHeap.add(rnd.nextInt(Integer.MAX_VALUE));

        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = minHeap.extractMin();
        for (int i = 1; i < n; i++)
            if (arr[i - 1] > arr[i])
                throw new IllegalArgumentException("Error");

        System.out.println("finish");
    }
}
