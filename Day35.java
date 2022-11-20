import java.util.HashMap;

public class Day35 {
    public static void main(String[] args) {
        HashMap<Integer, String> days = new HashMap<Integer,String>();

        // mengisi nilai
        days.put(1, "Minggu");
        days.put(2, "Senin");
        days.put(3, "Selasa");
        days.put(4, "Rabu");
        days.put(5, "Kamis");
        days.put(6, "Jum'at");
        days.put(7, "Sabtu");
        
        // mencetak semua isi dari objek days
        System.out.println("Isi objek days: " + days);

    }
}
