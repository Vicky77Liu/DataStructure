public class BinarySearch {
    private BinarySearch(){}
    public static <E extends Comparable<E>> int search(E[] data,E target){
        int l = 0, r = data.length;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (data[mid].compareTo(target) == 0) {
                return mid;
            } else if (data[mid].compareTo(target) < 0) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }


    //递归，recursion
    public static <E extends Comparable<E>> int searchR(E[] data,E target){
        return searchR(data,0,data.length-1,target);

    }
    private static <E extends Comparable<E>> int searchR(E[] data, int l ,int r, E target){
        if(l > r)
            return -1;
        int mid = l + (r-l) /2;
        if(data[mid].compareTo(target) == 0){
            return mid;
        }
        else if (data[mid].compareTo(target) < 0){
            return searchR(data,mid+1,r,target);
        }
        else {
            return searchR(data,l,mid-1,target);
        }
    }
    // > target 的最小值索引
    public static <E extends Comparable<E>> int upper(E[] data,E target){
        int l = 0 ,r = data.length;
        while (l < r){
            int mid = l + (r - l) / 2;
            if (data[mid].compareTo(target) <= 0)
                l = mid + 1;
            else if (data[mid].compareTo(target) > 0)
                r = mid;
        }
        return l;
    }
    // > target,返回大于target的最小值的索引
    // == target，返回等于target的最大的那个索引
    public static <E extends Comparable<E>> int upperceil(E[] data,E target){
//        int l = 0, r = data.length;
//        while (l < r){
//            int mid = l + (r - l) / 2;
//            if (data[mid].compareTo(target) <= 0)
//                l = mid + 1;
//            else if (data[mid].compareTo(target) > 0)
//                r = mid;
//        }
        int l = upper(data,target);
        if (l - 1 >= 0 && data[l-1].compareTo(target) == 0)
            return l -1;
        else return l;

    }
    // > target,返回大于target的最小值的索引
    // == target，返回等于target的最小的那个索引
    public static <E extends Comparable<E>> int lowerceil(E[] data,E target) {
        int l = 0, r = data.length;
        while (l < r) {

            int mid = l + (r - l) / 2;
            if (data[mid].compareTo(target) >= 0)
                r = mid;
            else l = mid + 1;
        }
        return l;
    }
    // < target的最大值的索引
    public static <E extends Comparable<E>> int lower(E[] data,E target){
        int l = -1 ,r = data.length-1;
        while (l < r){
            int mid = l + (r - l + 1) / 2;
            if (data[mid].compareTo(target) < 0)
                l = mid;
            else if (data[mid].compareTo(target) >= 0)
                r = mid - 1;
        }
        return l;
    }
    // < target的时候取 <target的 最大值的索引
    // == target ， 取== target的最小的索引
    public static <E extends Comparable<E>> int lowerfloor(E[] data,E target){
        int u = lower(data,target);
        if(u + 1 < data.length && data[u+ 1] == target){
            return u + 1;
        }
        else return u;
    }

    // < target的时候取 <target的 最大值的索引
    // == target ， 取== target的最大的索引
    public static <E extends Comparable<E>> int upperfloor(E[] data,E target){
        int l = -1,r = data.length-1;
        while (l < r){
            int mid = l + (r - l + 1) / 2;
            if (data[mid].compareTo(target) <= 0)
                l = mid;
            else if (data[mid].compareTo(target) > 0)
                r = mid - 1;

        }
        return l;
    }



    public static void main(String[] args){
        Integer[] arr = {1,1,3,3,5,5};
        for(int i = 0;i <= 6; i ++)
            System.out.print(BinarySearch.upperfloor(arr,i) + " ");
        System.out.println();
    }
}
