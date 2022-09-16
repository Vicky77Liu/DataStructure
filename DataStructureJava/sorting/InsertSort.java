import java.util.Arrays;

public class InsertSort {
    private InsertSort(){}
    public static <E extends Comparable<E>> void sort(E[] arr) {
        for (int i = 0; i < arr.length; i++) {
            E temp = arr[i];
            int j;
            for (j = i; j - 1 >= 0 && temp.compareTo(arr[j - 1]) < 0; j--) {
                arr[j] = arr[j - 1]; //move every element 
            }
            arr[j] = temp; //insert into the right index
        }
    }


    public static void main(String[] args){

        int[] dataSize = {10000,100000};
        for (int n:dataSize){
            System.out.println(" Random array: ");

            Integer[] arr = ArrayGenerator.generatorRandomArray(n,n);
            Integer[] arr2 = Arrays.copyOf(arr,arr.length);
            SortingHelper.sortTest("InsertSort",arr);
            SortingHelper.sortTest("SelectSort",arr2);

            System.out.println();

            System.out.println(" Ordered Array: ");
            arr = ArrayGenerator.generateOrderArray(n);
            arr2 = Arrays.copyOf(arr,arr.length);
            SortingHelper.sortTest("InsertSort",arr);
            SortingHelper.sortTest("SelectSort",arr);
        }
    }
}
