import java.util.Scanner;

public class Day29 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Input range: ");
        int range = sc.nextInt();

        for(int i=1; i < range; i++){
            if(i%2==0){//menampilkan bilangan ganjil
                System.out.println(i);
            }
        }
    }
}
