import java.util.Scanner;

public class Day22 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input angka : ");
        int angka = sc.nextInt();
        int x = 0;

        for(int i = 0; i <= angka; i++){
            if(i%2 == 1 && i%3==0){
                System.out.println(i);
                x += i;
            }
        }
        System.out.println("Jumlah = "+x);
    }
}
