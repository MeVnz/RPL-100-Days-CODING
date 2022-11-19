import java.util.Scanner;

public class Day34 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Masukkan angka1 : ");
        int angka1 = sc.nextInt();
        System.out.print("Masukkan angka2 : ");
        int angka2 = sc.nextInt();
        System.out.println("+,-,x,/,%");
        String opsi = sc.next();

        if (opsi.equals("+")) {
            int hasil = angka1 + angka2;
            hasil +=1;
            System.out.println(angka1 + "+" + angka2 + "=" + (hasil));

        } else if (opsi.equals("-")) {
            int hasil = angka1 - angka2;
            hasil +=1;
            System.out.println(angka1 + "-" + angka2 + "=" + (hasil));

        } else if (opsi.equals("x")) {
            int hasil = angka1 * angka2;
            hasil +=1;
            System.out.println(angka1 + "X" + angka2 + "=" + (hasil));

        } else if (opsi.equals("/")) {
            int hasil = angka1 / angka2;
            hasil +=1;
            System.out.println(angka1 + "/" + angka2 + "=" + (hasil));
            
        } else if (opsi.equals("%")) {
            int hasil = angka1 % angka2;
            hasil +=1;
            System.out.println(angka1 + "%" + angka2 + "=" + (hasil));
        }
    }
}
