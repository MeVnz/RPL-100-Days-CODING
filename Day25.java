import java.util.ArrayList;

public class Day25 {
    public static void main(String[] args) {
        ArrayList<Integer> angka = new ArrayList<>();
        
        //menambahkan nilai
        angka.add(5);
        angka.add(5);
        angka.add(3);
        System.out.println(angka);
        //mengakses indeks tertentu
        System.out.println(angka.get(0));
        //menghapus nilai
        angka.remove(2);
        System.out.println(angka);
        //mengecek nilai
        System.out.println(angka.contains(10));
        //mengupdate nilai
        angka.set(1, 10);
        System.out.println(angka);
    }
}