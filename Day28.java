public class Day28 {
    public static void main(String[] args) {
        int x = 0;
        for(int i =100; i >=1; i--){
            System.out.println(i);
            if(i%3!=0){
                x += i;
            }
        }
        System.out.println("-----");
        System.out.println("Hasil = "+x);
    }
}
