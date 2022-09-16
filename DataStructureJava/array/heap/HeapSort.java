public class HeapSort {
    private HeapSort(){}

    public static <E extends Comparable<E>> void sort(E[] data){ // data 是一个无序数组
        // 把data heapify 成一个最大堆
        if (data.length <= 1) return;
        for (int i = (data.length-2) / 2; i >= 0; i --)
            siftDown(data,i,data.length);

        for (int i = data.length - 1; i >= 0; i--){
            swap(data,0,i);
            siftDown(data,0,i);
        }
    }
    // 对[0,n)所形成的最大堆中，索引 k 的元素，执行siftdown
    private static <E extends Comparable<E>> void siftDown(E[] data, int k , int n){
        while (2 * k + 1 < n){
            int j = 2 * k + 1;
            // 如果右孩子的值大于左孩子的值，
            if (j + 1 < n && data [j + 1].compareTo(data[j]) > 0)
                j ++; // j = rightChild(k)
            // 此时 j 是左右孩子中的最大值
            if (data[k].compareTo(data[j]) >= 0)
                break;
            swap(data,k,j);
            k = j;
        }
    }
    public static <E> void  swap(E[] data,int i, int j) {

        E t = data[i];
        data[i] = data[j];
        data[j] = t;
    }
}
