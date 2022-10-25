import java.util.Scanner;

public class Day9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input nilai = ");
        int nilai = sc.nextInt();

        if(nilai >= 90 && nilai <=100){
            System.out.println("Nilai A");
        }
        else if (nilai >= 80 && nilai <= 90){
            System.out.println("Nilai B");
        }
        else if (nilai <= 80 && nilai >= 65){
            System.out.println("Nilai C");
        }
        else if (nilai <=65){
            System.out.println("Nilai E");
        }
        else{
            System.out.println("Input nilai");
        }
    }
}
