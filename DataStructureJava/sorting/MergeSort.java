import java.util.Arrays;

public class MergeSort {
    private MergeSort(){}
    // 自顶向下的归并排序
    public static <E extends Comparable<E>> void sort(E[] arr){
        sort(arr,0,arr.length-1);
    }
    private  static <E extends Comparable<E>> void sort(E[] arr,int l ,int r){
        if (l >= r) //区间中没有元素或者只有一个元素，不需要排序
            return;
        int mid = l + (r - l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
    }

    //合并两个有序区间[l,mid],[mid+1,r]
    private static <E extends Comparable<E>> void merge(E[] arr,int l,int mid,int r) {
        E[] temp = Arrays.copyOfRange(arr, l, r + 1);
        int i = l;
        int j = mid + 1;
        for (int k = l; k <= r; k++) {
            if (i > mid) {
                arr[k] = temp[j - l];
                j++;
            } else if (j > r) {
                arr[k] = temp[i - l];
                i++;
            } else if (temp[i - l].compareTo(temp[j - l]) <= 0) {
                arr[k] = temp[i - l];
                i++;
            } else {
                arr[k] = temp[j - l];
                j++;
            }
        }
    }

    public static <E extends Comparable<E>> void sort2(E[] arr){
        E[] temp = Arrays.copyOf(arr,arr.length);
        sort2(arr,0,arr.length-1,temp);
    }
    private  static <E extends Comparable<E>> void sort2(E[] arr,int l ,int r,E[] temp){
        if (l >= r) //区间中没有元素或者只有一个元素，不需要排序
            return;
        int mid = l + (r - l)/2;
        sort2(arr,l,mid,temp);
        sort2(arr,mid+1,r,temp);
        if (arr[mid].compareTo(arr[mid+1]) > 0)
            merge2(arr,l,mid,r,temp);
    }
    //自底向上的归并排序
    public static <E extends Comparable<E>> void sortBU(E[] arr){
        E[] temp = Arrays.copyOf(arr,arr.length);
        int n = arr.length;
        // 遍历合并的区间长度
        for(int size = 1;size < n;size += size){
            // 遍历合并的两个区间的起始位置 i
            // 合并[i,i+size-1] 和 【i+size,i+size+size-1 or n-1]
            for(int i = 0; i + size < n; i += size + size){
                merge2(arr,i,i+size-1,Math.min(i+size+size-1,n-1),temp);
            }
        }
    }
    //合并两个有序区间[l,mid],[mid+1,r]
    private static <E extends Comparable<E>> void merge2(E[] arr,int l,int mid,int r,E[] temp){
        System.arraycopy(arr,l,temp,l,r-l+1);
        int i = l;
        int j = mid + 1;
        for (int k = l;k <= r;k++){
            if(i > mid) {
                arr[k] = temp[j];
                j ++;
            }
            else if ( j > r){
                arr[k] = temp[i];
                i ++ ;
            }
            else if (temp[i].compareTo(temp[j]) <= 0){
                arr[k] = temp[i];
                i ++;
            }
            else {
                arr[k] = temp[j];
                j ++ ;
            }
        }
    }
    public static void main(String[] args) {
        int n = 1000000;
        Integer[] arr = {0};
//        Integer[] arr = ArrayGenerator.generateOrderArray(n);
        Integer[] arr2 = Arrays.copyOf(arr,arr.length);
        SortingHelper.sortTest("MergeSort",arr);
        SortingHelper.sortTest("MergeSortBU",arr2);
    }
}

