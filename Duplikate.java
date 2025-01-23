import java.util.ArrayList;
import java.util.Arrays;

public class Duplikate {
    public static void main(String[] args) {
        // Zwei String-Listen
        String[] a = {"a", "b", "c"};
        String[] b = {"b", "c", "d"};
        // Lösungen
        String[] dupliA = DuplikateA(a, b);
        String[] dupliB = DuplikateB(a, b);
        // Ausgabe
        for (String i: dupliA)
            System.out.print(i + " ");
        System.out.println();
        for (String i: dupliB)
            System.out.print(i + " ");
    }


    // 2a)
    private static String[] DuplikateA(String[] a, String[] b) {
        ArrayList<String> res = new ArrayList<>();
        // Verschachtelte Schleifen
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b.length; j++) {
                if (a[i].equals(b[j])) {
                    res.add(a[i]);
                }
            }
        }
        return res.toArray(new String[0]);
    }
    // Zeitkomplexität ist quadratisch, 
    // da sich die Komplexität verschachtelter Schleifen
    // mit jeweils n-durchläufen multipliziert.
    // Jedes Element von Liste a wird mit jedem Elment der Liste b verglichen.
    // Bei 2 verschachtelten Schleifen quadriert sich es somit.


    // 2b)
    private static String[] DuplikateB(String[] a, String[] b) {
        // Vorsortierung
        Arrays.sort(a);
        Arrays.sort(b);
        // Algorithmus
        int i = 0, j = 0;
        String[] dupli = new String[Math.min(a.length, b.length)]; // max mögliche Duplikate
        int dupliInd = 0;
        // eine einzige Schleife.
        while (i < a.length && j < b.length) {
            int compt = a[i].compareTo(b[j]);
            if (compt == 0) {
                // Duplikat gefunden
                dupli[dupliInd] = a[i];
                dupliInd++;
                i++;
                j++;
            } else if (compt < 0) {
                i++;    // in a das nächste Element anschauen.
            } else {
                j++;    // in b das nächste Element anschauen.
            }
        }
        String[] res = new String[dupliInd];
        System.arraycopy(dupli, 0, res, 0, dupliInd);
        return res;
    }
    // Die Zeitkomplexität ist besser als quadratisch, 
    // weil wir nicht für jedes Element von a jedes Element von b betrachten.
}
