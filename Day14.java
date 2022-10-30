import java.util.Scanner;

public class Day14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        while(run){
            System.out.print("Masukkan angka1 : ");
            int angka1 = sc.nextInt();
            System.out.print("Masukkan angka2 : ");
            int angka2 = sc.nextInt();
            System.out.println("+,-,x,/,%");
            String opsi = sc.next();
            
            if(opsi.equals("+")){
                System.out.println(angka1 + "+" + angka2 + "=" + (angka1+angka2));
            }
            else if (opsi.equals("-")){
                System.out.println(angka1 + "-" + angka2 + "=" + (angka1-angka2));
            }
            else if(opsi.equals("x")){
                
                System.out.println(angka1 + "x" + angka2 + "=" + (angka1*angka2));
            }
            else if(opsi.equals("/")){
                
                System.out.println(angka1 + "/" + angka2 + "=" + (angka1/angka2));
            }
            else if(opsi.equals("=")){
                
                System.out.println(angka1 + "%" + angka2 + "=" + (angka1%angka2));
            }
            System.out.println("Yakin ingin keluar? Yes / No ");
            String a = sc.next();
            if(a.equalsIgnoreCase("Yes")){
                run = false;
            }
        }
        System.out.println("Anda Sudah Keluar");
    }
}
