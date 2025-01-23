import java.util.HashSet;
import java.util.Random;
import java.util.Set;

// 3)
public class TestHashTable {
    public static void main(String[] args) {
        int[] tableSizes = {7, 13, 31}; // Tabellengrößen.
        int[] factors = {1, 3, 5};  // Faktoren.
        // Anzahl an Schlüsseln, die wir einfügen.
        int keyCount = 20;
        for (int size : tableSizes) {
            for (int factor : factors) {
                HashTable ht = new HashTable(size, factor);
                // Zufällige, paarweise verschiedene Schlüssel generieren.
                int[] keys = generateDistinctKeys(keyCount, 0, 1000);
                // Einfügen der Schlüssel in den Hashtable.
                for (int key : keys) {
                    ht.insert(key);
                }
                // Belegungsfaktor μ (durchschnittliche Einträge pro Index).
                double mu = (double) keyCount / size;
                // Anzahl der Elemente in der verketteten Liste.
                int[] chainLengths = ht.getChainLengths();
                // Berechnung der mittleren quadratischen Abweichung.
                double msd = computeMSD(chainLengths, mu);
                // Anzahl Kollisionen
                int collisions = ht.getCollisionCount();
                // Verhältnis belegte Tabellenplätze / Tabellengröße
                int usedCells = 0;
                for (int len : chainLengths) {
                    if (len > 0) {
                        usedCells++;
                    }
                }
                double ratio = (double) usedCells / size;

                System.out.println("Experiment: Größe = " + size + ", Faktor a = " + factor);
                System.out.printf("Eingefügte Schlüssel: %d\n", keyCount);
                System.out.printf("Belegungsfaktor µ = %.3f\n", mu);
                System.out.printf("MSD (Mean Squared Deviation) = %.3f\n", msd);
                System.out.printf("Kollisionen = %d\n", collisions);
                System.out.printf("Anteil belegter Plätze = %.3f\n", ratio);
                System.out.println();
            }
        }
    }


    // Liefert zufällige, paarweise verschiedene Schlüssel
    private static int[] generateDistinctKeys(int keyCount, int minValue, int maxValue) {
        Set<Integer> set = new HashSet<>();
        Random rand = new Random();
        // Generieren und Einfügen der Schlüssel.
        while (set.size() < keyCount) {
            int key = rand.nextInt(maxValue - minValue + 1) + minValue;
            set.add(key);
        }
        // Konvertieren in Array
        int[] res = new int[keyCount];
        int i = 0;
        for (int value : set) {
            res[i++] = value;
        }
        return res;
    }


    private static double computeMSD(int[] chainLengths, double mu) {
        int N = chainLengths.length;
        double sumSq = 0.0;
        for (int len : chainLengths) {
            double diff = len - mu;  // xi - µ
            sumSq += diff * diff;   // (xi - µ)²
        }
        double mse = sumSq / N;
        return Math.sqrt(mse);  // MSD = sqrt(mse)
    }
}


class HashTable {
    private HashNode[] table;   // Array von verketteten Listen
    private int m;  // Tabellengröße m
    private int a;  // Faktor a
    private int collisionCount; // Zum Zählen der Kollisionen

    // Konstruktor
    public HashTable(int tableSize, int fac) {
        this.m = tableSize;
        this.a = fac;
        this.table = new HashNode[tableSize];
        this.collisionCount = 0;
    }
    

    // Hashfunktion.
    private int hash(int k) {
        return (a * k) % m;
    }
    

    // Schlüssel einfügen.
    public void insert(int k) {
        int ind = hash(k);
        // Kollisionsprüfung.
        if (table[ind] != null)
            collisionCount++;
        // Neuen Knoten vorn an die verkettete Liste hängen.
        HashNode newNode = new HashNode(k);
        newNode.next = table[ind];
        table[ind] = newNode;
    }
    

    public int getCollisionCount() {
        return collisionCount;
    }


    // Liefert eine Array-Darstellung der Kettenlängen, um MSD & Co. zu berechnen.
    public int[] getChainLengths() {
        int[] chainLengths = new int[m];
        for (int i = 0; i < m; i++) {
            int len = 0;
            HashNode current = table[i];
            // solange bis der Knoten nicht gefüllt ist.
            while (current != null) {
                len++;
                current = current.next;
            }
            chainLengths[i] = len;
        }
        return chainLengths;
    }
}


class HashNode {
    int k;  // Schlüssel.
    HashNode next;  // Nächstes Element in der Kette.
    
    public HashNode(int key) {
        this.k = key;
        this.next = null;
    }
}


/*
 * 3c)
 * Wenn μ mind. 1 ist, ist die Tabelle im Schnitt "voll".
 * Wenn μ unter 1, ist Verteilung gleichmäßiger mit weniger Kollisionen.
 * 
 * Wenn MSD niedrig, dann ist Verteilung gleichmäßig.
 * Wenn MSD hoch, dann sind Verteilung ungleichmäßig.
 * 
 * Viele Kollisionen resultieren oft aus ungeeignetem Faktor a oder einer zu kleinen Tabellengröße m.
 * Wenn Anteil belegter Plätze trotz hohem μ sehr niedrig, dann ist Verteilung ungleichmäßig.
 */
