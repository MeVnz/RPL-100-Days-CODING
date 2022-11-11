import java.util.Scanner;

public class Day26 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input angka : ");
        int angka = sc.nextInt();
        String a = " ";
        for(int i=0; i <=angka; i++){
            for(int j=0; j < i; j++){
                a += "*";
            }a += "\n";
        }
        System.out.println(a);
    }
}
