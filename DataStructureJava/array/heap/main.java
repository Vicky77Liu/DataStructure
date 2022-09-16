import java.util.Random;

public class main {
    public static double testHeap(Integer[] testdata, boolean isheapify){
        long startTime = System.nanoTime();
        MaxHeap<Integer> maxHeap;
        if (isheapify)
            maxHeap = new MaxHeap<>(testdata);
        else
            maxHeap = new MaxHeap<>();
            for(int num : testdata)
                maxHeap.add(num);

        int [] arr = new int[testdata.length];
        for (int i = 0;i < testdata.length; i ++)
            arr[i] = maxHeap.extractMax();
        for (int i = 1;i < testdata.length; i ++)
            if (arr[i-1] < arr[i])
                throw new IllegalArgumentException("Error");

        System.out.println("finish");
        long endTime = System.nanoTime();
        return (endTime - startTime) / 1000000000.0;
    }
    public static void main(String[] args){
        int n = 100;
        MaxHeap<Integer> maxHeap = new MaxHeap<>();
        Random rnd = new Random();
        Integer[] testdata = new Integer[n];
        for(int i = 0; i < n; i ++)
            testdata[i] = rnd.nextInt(Integer.MAX_VALUE);
        double time1 = testHeap(testdata, false);
        System.out.println("without heapify   " + time1);

        double time2 = testHeap(testdata,true);

        System.out.println("heapify   " + time2);
    }
}
