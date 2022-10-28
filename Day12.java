import java.util.Scanner;

public class Day12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input panjang tanah = ");
        int panjang = sc.nextInt();
        System.out.print("Input lebar tanah = ");
        int lebar = sc.nextInt();
        int hasil = panjang * lebar;

        if(hasil > 200 ){
            System.out.println("Tanah sangat luas");
        }else{
            System.out.println("Tanah cukup luas");
        }
    }
}
