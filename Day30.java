import java.util.Scanner;

public class Day30 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Data mhs: ");
        int data = sc.nextInt();

        String mhs[][] = new String[data][3];
        for(int i= 0; i<data; i++)
        {
            System.out.println("");
            System.out.println("Data Mahasiswa ke "+(i+1));

            for(int j=0;j<3;j++)
            {      
                if (j == 0)
                    System.out.print("NIM     : ");
                else if (j == 1)
                    System.out.print("Nama    : ");
                else
                    System.out.print("Semester : ");
                
                System.out.print("");
                mhs[i][j] = sc.next();
            }
        }

        System.out.println("Data Mahasiswa yang dimasukan");
        System.out.println("-----------------------------");
        System.out.println("NIM \t\t\t  NAMA \t\t  JURUSAN \t");
        
        for(int i=0;i<data;i++)
        {
            for(int j=0;j<3;j++)
            {
                System.out.print(mhs[i][j]+"\t\t");
            }
        System.out.println();
        }
    }
}
