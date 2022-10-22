import java.util.Scanner;

public class Day6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan angka1 : ");
        int angka1 = sc.nextInt();
        System.out.print("Masukkan angka2 : ");
        int angka2 = sc.nextInt();

        System.out.println(angka1 + "+" + angka2 + "=" + (angka1+angka2));
        System.out.println(angka1 + "-" + angka2 + "=" + (angka1-angka2));
        System.out.println(angka1 + "x" + angka2 + "=" + (angka1*angka2));
        System.out.println(angka1 + "/" + angka2 + "=" + (angka1/angka2));
        System.out.println(angka1 + "%" + angka2 + "=" + (angka1%angka2));
    }
}
