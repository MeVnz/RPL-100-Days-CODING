import java.util.Scanner;

public class Day32 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input jarak tempuh: ");
        int jarak = sc.nextInt();
        int tarif = 10000;

        if(jarak >= 10){
            int JumlahBayar = tarif * jarak;
            int discount = JumlahBayar * 50/100;
            int total = JumlahBayar - discount;
            System.out.println("Jumlah bayar : "+JumlahBayar);
            System.out.println("Discount : "+discount);
            System.out.println("Total bayar : "+total);
        }
        else if(jarak < 10){
            int JumlahBayar = tarif * jarak;
            int total = JumlahBayar;
            System.out.println("Jumlah bayar : "+JumlahBayar);
            System.out.println("Tidak mendapatkan diskon");
            System.out.println("Total bayar : "+total);
        }
    }
}
