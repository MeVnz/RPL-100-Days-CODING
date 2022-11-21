import java.util.Scanner;

public class Day36 {
    public static void main(String[] args) {
        // membuat array hobi
        String[] hobi = new String[100];
        
        // membuat scanner
        Scanner scan = new Scanner(System.in);
        System.out.print("Masukan Jumlah Hobi :");
        String hitung = scan.nextLine();
        int data = Integer.valueOf(hitung);
        
        // mengisi data ke array
        for (int i = 0; i < data; i++) {
            System.out.print("Masukan Nama Hobi ke-" + (i + 1) + ": ");
            hobi[i] = scan.nextLine();
        }
        
        System.out.println("Hobi anda adalah :");
        // menampilkan semua isi array hobi
        for (int i = 0; i < data; i++) {
            System.out.println((i+1)+"."+hobi[i]);
        }
    }
}
