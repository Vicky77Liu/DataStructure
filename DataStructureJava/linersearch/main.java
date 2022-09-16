public class main {
    public static void main(String[] args){
        int n = 1000000;
        Integer [] data = ArrayGenerator.generateOrderArray(n);

        long startTime = System.nanoTime();
        for(int k = 0; k < 100; k++){
            LinearSearch.search(data,n);
        }
        long endTime = System.nanoTime();
        double time = (endTime - startTime) / 1000000000.0;
        System.out.println(time + "s");


//        Student[] students = {new Student("Alice"),
//                              new Student("Bob"),
//                              new Student("charles")};
//        Student bobo = new Student("alice");
//        int res1 = LinearSearch.search(students,bobo);
//        System.out.println(res1);
    }
}
