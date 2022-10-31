import java.util.Scanner;

public class Day15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        while(run){
            String user = "admin";
            String pass = "admin";
    
            System.out.print("Username : ");
            String User = sc.next();
            System.out.print("Password : ");
            String Pass = sc.next();
    
            if(User.equals("admin") && Pass.equals("admin")){
                System.out.println("Login Sukses");
                run = false;
            }
            else{
                System.out.println("Login Gagal");
            }
        }
    }
}
