public class Day33 {
    public static void main(String[] args) {
        String hasil = "";
        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < i; j++) {
                hasil += "*";
            }
            hasil += "\n";
        }
        System.out.println(hasil);
    }
}
