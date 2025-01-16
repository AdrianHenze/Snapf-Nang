import java.util.ArrayList;
import java.util.Arrays;

public class Duplikate {
    public static void main(String[] args) {
        // Zwei String-Listen
        String[] a = {"a", "b", "c"};
        String[] b = {"b", "c", "d"};

        // Lösungen
        String[] c = Duplikate_a(a, b);
        String[] d = Duplikate_b(a, b);

        // Ausgabe
        for (String i: c)
            System.out.print(i + " ");
        System.out.println();
        for (String i: d)
            System.out.print(i + " ");
    }


    // 2a)
    private static String[] Duplikate_a(String[] a, String[] b) {
        ArrayList<String> res = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b.length; j++) {
                if (a[i].equals(b[j])) {
                    res.add(a[i]);
                }
            }
        }
        return res.toArray(new String[0]);
    }


    // 2b)
    private static String[] Duplikate_b(String[] a, String[] b) {
        // Vorsortierung
        Arrays.sort(a);
        Arrays.sort(b);

        // Algorithmus
        int i = 0, j = 0;
        String[] temp = new String[Math.min(a.length, b.length)]; // max mögliche Duplikate
        int count = 0;

        while (i < a.length && j < b.length) {
            int cmp = a[i].compareTo(b[j]);
            if (cmp == 0) {
                // Duplikat gefunden
                temp[count] = a[i];
                count++;
                i++;
                j++;
            } else if (cmp < 0) {
                // a[i] ist "kleiner" → i inkrementieren
                i++;
            } else {
                // b[j] ist "kleiner" → j inkrementieren
                j++;
            }
        }

        String[] result = new String[count];
        System.arraycopy(temp, 0, result, 0, count);
        return result;
    }
}
