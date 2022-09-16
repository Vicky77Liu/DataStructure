import java.util.Arrays;
import java.util.Random;

public class QuickSort {
    private QuickSort(){}
    public static <E extends Comparable<E>> void sort(E[] arr){
        Random rnd = new Random();
        sort(arr,0, arr.length-1,rnd);

    }
    private static <E extends Comparable<E>> void sort(E[]arr,int l,int r,Random rnd){
        if(l >= r) return;
        int p = partition(arr,l,r,rnd);
        sort(arr,l,p-1,rnd);
        sort(arr,p+1,r,rnd);
    }
    private static <E extends Comparable<E>> int partition(E[]arr,int l,int r,Random rnd) {
        int p = l + rnd.nextInt(r-l+1);
        swap(arr,l,p);
        //循环不变量 arr[l+1...j] < V; arr[j+1...i] >= V
        int j = l;
        for (int i = l + 1; i <= r; i++)
            if (arr[i].compareTo(arr[l]) < 0) {
                j++;
                swap(arr, i, j);
            }
        swap(arr,l,j);
        return j;
    }

    public static <E extends Comparable<E>> void sort2ways(E[] arr){
        Random rnd = new Random();
        sort2ways(arr,0, arr.length-1,rnd);

    }
    private static <E extends Comparable<E>> void sort2ways(E[]arr,int l,int r,Random rnd){
        if(l >= r) return;
        int p = partition2(arr,l,r,rnd);
        sort2ways(arr,l,p-1,rnd);
        sort2ways(arr,p+1,r,rnd);
    }
    private static <E extends Comparable<E>> int partition2(E[]arr,int l,int r,Random rnd) {
        int p = l + rnd.nextInt(r-l+1);
        swap(arr,l,p);
        //循环不变量 arr[l+1...i-1] <= V; arr[j+1...r] >= V
        int i = l + 1,j = r;
        while(true){
            // 从前往后找到第一个大于arr[l]的数
            while(i <= j && arr[i].compareTo(arr[l]) < 0)
                i ++;
            // 从后往前找到第一个小于arr[l]的数
            while(j >= i && arr[j].compareTo(arr[l]) > 0)
                j --;
            if (i >= j )
                break;
            swap(arr,i,j);
            i ++;
            j --;
        }
        swap(arr,l,j);
        return j;
    }

    public static <E extends Comparable<E>> void sort3ways(E[] arr){
        Random rnd = new Random();
        sort3ways(arr,0, arr.length-1,rnd);

    }
    private static <E extends Comparable<E>> void sort3ways(E[]arr,int l,int r,Random rnd){
        if(l >= r) return;
        int p = l + rnd.nextInt(r-l+1);
        swap(arr,l,p);
        //循环不变量 arr[l+1...lt] < V; arr[lt+1...i-1]==V; arr[gt...r] > V
        int lt = l,i = l + 1,gt = r +1;
        while(i < gt) {
            if (arr[i].compareTo(arr[l]) < 0) {
                lt++;
                swap(arr, i, lt);
                i++;
            } else if (arr[i].compareTo(arr[l]) > 0) {
                gt--;
                swap(arr, i, gt);
            } else {
                i++;
            }
        }
        swap(arr,l,lt);//arr[l,lt-1] < V; arr[lt,gt-1]== V,arr[gt,r] > V
        sort3ways(arr, l, lt-1, rnd);
        sort3ways(arr,gt,r,rnd);
    }

    private static <E extends Comparable<E>> void swap(E[]arr,int i, int j ){
        E t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }
    public static void main(String[] args) {
        int n = 1000;
        Integer[] arr = ArrayGenerator.generatorRandomArray(n,n);
        Integer[] arr2 = Arrays.copyOf(arr,arr.length);
        Integer[] arr3 = Arrays.copyOf(arr,arr.length);


        System.out.println("Random:");
        SortingHelper.sortTest("QuickSort",arr);
        SortingHelper.sortTest("QuickSort2ways",arr2);
        SortingHelper.sortTest("QuickSort3ways",arr3);

        arr = ArrayGenerator.generateOrderArray(n);
        arr2 = Arrays.copyOf(arr,arr.length);
        arr3 = Arrays.copyOf(arr,arr.length);
        System.out.println("Ordered:");
        SortingHelper.sortTest("QuickSort",arr);
        SortingHelper.sortTest("QuickSort2ways",arr2);
        SortingHelper.sortTest("QuickSort3ways",arr3);


        arr = ArrayGenerator.generatorRandomArray(n,1);
        arr2 = Arrays.copyOf(arr,arr.length);
        arr3 = Arrays.copyOf(arr,arr.length);
        System.out.println("Same numbers:");
        SortingHelper.sortTest("QuickSort",arr);
        SortingHelper.sortTest("QuickSort2ways",arr2);
        SortingHelper.sortTest("QuickSort3ways",arr3);
    }
}
