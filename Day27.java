import java.util.Scanner;

import javax.lang.model.element.Element;

public class Day27 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("PIN ANDA: ");
        int pin = sc.nextInt();
        int Saldo = 2000000;

        if(pin == 1234){
            System.out.println("[1] Transfer");
            System.out.println("[2] Cek Saldo");
            System.out.print("Input pilihan : ");
            int pilih = sc.nextInt();
            if(pilih == 1){
                System.out.println("Pilih bank");
                System.out.println("[1] BCA");
                System.out.println("[2] BRI");
                System.out.println("[4] BNI");
                System.out.println("[3] MANDIRI");
                System.out.print("Bank: ");
                int bank = sc.nextInt();
                if(bank == 1){
                    System.out.print("Nomor Rekening Tujuan: ");
                    int noRek = sc.nextInt();
                    System.out.print("Jumlah Transfer: ");
                    int tf = sc.nextInt();
                    int a = Saldo - tf;
                    System.out.println("Transfer Berhasil");
                    System.out.println("Sisa Saldo: "+a);
                }
                else if(bank == 2){
                    System.out.print("Nomor Rekening Tujuan: ");
                    int noRek = sc.nextInt();
                    System.out.print("Jumlah Transfer: ");
                    int tf = sc.nextInt();
                    int a = Saldo - tf;
                    System.out.println("Transfer Berhasil");
                    System.out.println("Sisa Saldo: "+a);
                }
                else if(bank == 3){
                    System.out.print("Nomor Rekening Tujuan: ");
                    int noRek = sc.nextInt();
                    System.out.print("Jumlah Transfer: ");
                    int tf = sc.nextInt();
                    int a = Saldo - tf;
                    System.out.println("Transfer Berhasil");
                    System.out.println("Sisa Saldo: "+a);
                }
                else if(bank == 4){
                    System.out.print("Nomor Rekening Tujuan: ");
                    int noRek = sc.nextInt();
                    System.out.print("Jumlah Transfer: ");
                    int tf = sc.nextInt();
                    int a = Saldo - tf;
                    System.out.println("Transfer Berhasil");
                    System.out.println("Sisa Saldo: "+a);
                }
            }
            else if(pilih == 2){
                System.out.println("Saldo anda: "+Saldo);
            }
        }else{
            System.out.println("PIN SALAH");
        }
    }
}
