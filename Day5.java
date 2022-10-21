import java.util.Scanner;

public class Day5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input panjang = ");
        int p = sc.nextInt();
        System.out.print("Input lebar = ");
        int l = sc.nextInt();

        int hasil = p * l;
        System.out.println("Luas = "+hasil);

    }
}
