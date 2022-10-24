import java.util.Scanner;

public class Day8 {
    public static void main(String[] args) {
        String user = "admin";
        String pass = "admin";

        Scanner sc = new Scanner(System.in);
        System.out.print("Username : ");
        String User = sc.nextLine();
        System.out.print("Password : ");
        String Pass = sc.nextLine();

        if(User.equals("admin") && Pass.equals("admin")){
            System.out.println("Login Sukses");
        }
        else{
            System.out.println("Login Gagal");
        }
    }
}
