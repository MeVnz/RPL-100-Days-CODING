import java.util.Scanner;

public class Day16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input range : ");
        int range = sc.nextInt();

        for(int i = 1; i <= range; i++){
            System.out.println("Range "+i);
        }
    }
}
