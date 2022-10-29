import java.util.Scanner;

public class Day13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        while(run){
            System.out.println("Yakin ingin keluar? Yes / No ");
            String a = sc.nextLine();
            if(a.equalsIgnoreCase("Yes")){
                run = false;
            }
        }
        System.out.println("Anda Sudah Keluar");
    }
}
