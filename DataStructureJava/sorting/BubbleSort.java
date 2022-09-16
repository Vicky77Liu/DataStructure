public class BubbleSort {
    private BubbleSort(){}
    public static <E extends Comparable<E>> void sort(E[] data){
        for (int i = 0; i < data.length - 1; i++){
            //arr[n-i, n)已经排序
            //通过冒泡在 arr[n-i-1] 的位置放上合适的元素
            for (int j = 0 ; j < data.length -1 -i; j++)
                if(data[j].compareTo(data[j+1]) > 0)
                    swap(data, j , j+ 1);
        }
    }
    // 对有序数组的优化
    public static <E extends Comparable<E>> void sort2(E[] data){
        for (int i = 0; i < data.length - 1; i++){
            //arr[n-i, n)已经排序
            //通过冒泡在 arr[n-i-1] 的位置放上合适的元素
            boolean isSwapped = false;
            for (int j = 0 ; j < data.length -1 -i; j++)
                if(data[j].compareTo(data[j+1]) > 0){
                    swap(data, j , j+ 1);
                    isSwapped = true;}
            if (!isSwapped) break;
        }
    }
    // 跳过已经完成循环的步骤
    public static <E extends Comparable<E>> void sort3(E[] data){
        for (int i = 0; i < data.length - 1;){
            //arr[n-i, n)已经排序
            //通过冒泡在 arr[n-i-1] 的位置放上合适的元素
            int lastSwappedIndex = 0;
            for (int j = 0 ; j < data.length -1 -i; j++)
                if(data[j].compareTo(data[j+1]) > 0){
                    swap(data, j , j+ 1);
                    lastSwappedIndex = j + 1;}

            i = data.length - lastSwappedIndex;
        }
    }
    private static <E> void swap(E[] arr, int i, int j){
        E t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }
}
