public class ShellSort {
    private ShellSort(){}
    //直接依次处理每个元素
    public static <E extends Comparable<E>> void sort(E[] data){
        int h = data.length /2;
        while (h >= 1) {
                // 对data[h....]进行插入排序
            for(int i = h; i < data.length; i ++){
                E t = data[i];
                int j;
                for(j = i; j - h >= 0 && t.compareTo(data[j-h]) < 0; j -= h)
                    data[j] = data[j-h];
                data[j] = t;
                }
            h /= 2;
        }
    }
    public static <E extends Comparable<E>> void sort2(E[] data){
        // 用新的步长序列
        int h = 1;
        while (h < data.length) h = h *3 + 1;
        while (h >= 1) {
            // 对data[h....]进行插入排序
            for(int i = h; i < data.length; i ++){
                E t = data[i];
                int j;
                for(j = i; j - h >= 0 && t.compareTo(data[j-h]) < 0; j -= h)
                    data[j] = data[j-h];
                data[j] = t;
            }
            h /= 3;
        }
    }
}
