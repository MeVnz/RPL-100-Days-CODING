import java.util.Scanner;

public class Day11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input nama : ");
        String nama = sc.next();

        for (int i = 0; i < 5; i++) {
            System.out.println(nama);
        }
    }
}
