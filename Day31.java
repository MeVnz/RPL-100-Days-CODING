import java.util.Scanner;

public class Day31 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input gaji: ");
        int gaji = sc.nextInt();

        if(gaji >= 5000000){
            int bonus = gaji * 10/100;
            System.out.println("Bonus = "+bonus);
            System.out.println("Total gaji = "+(gaji+bonus));
        }
        if(gaji < 5000000){
            int bonus = gaji * 5/100;
            System.out.println("Bonus = "+bonus);
            System.out.println("Total gaji = "+(gaji+bonus));
        }
    }
}
