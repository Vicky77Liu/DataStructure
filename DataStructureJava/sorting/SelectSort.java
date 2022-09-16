public class SelectSort {
    private SelectSort(){}

    public static <E extends Comparable<E>> void sort(E[] arr){
        for(int i = 0;i < arr.length;i++){
            //chose the index of the smallest number of the arr[i...n)
            int minIndex = i;
            for (int j = i;j < arr.length;j++){
                if (arr[j].compareTo(arr[minIndex]) < 0){
                    minIndex = j;
                }
            }
            swap(arr,i,minIndex);
        }
    }

    public static <E extends Comparable<E>> void sort2(E[] arr){
        for(int i = arr.length - 1;i >= 0; i--){
            //chose the index of the biggest number of the arr[0...i]
            int maxIndex = i;
            for (int j = i;j >= 0;j--){
                if (arr[j].compareTo(arr[maxIndex]) < 0){
                    maxIndex = j;
                }
            }
            swap(arr,i,maxIndex);
        }
    }
    private static <E>void swap(E[]arr,int i ,int j){
        E t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args){

        int n = 10000;
        Integer [] arr = ArrayGenerator.generatorRandomArray(n,n);
        SortingHelper.sortTest("SelectSort",arr);
//
//
//        Student[] students = {new Student("Alice",98),
//                              new Student("Bob",100),
//                              new Student("charles",66)};
//        SelectSort.sort(students);
//        for(Student student: students){
//            System.out.print(student + "");
//        }
//        System.out.println();
    }
}
