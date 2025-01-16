import java.util.HashSet;
import java.util.Random;
import java.util.Set;

// 3b)
public class TestHashTable {
    public static void main(String[] args) {
        // Beispielwerte für Tabellengrößen und Faktoren
        int[] tableSizes = {7, 13, 31}; 
        int[] factors = {1, 3, 5};

        // Anzahl an Schlüsseln, die wir einfügen wollen
        int numberOfKeys = 20;

        for (int size : tableSizes) {
            for (int factor : factors) {
                System.out.println("=== Experiment: Größe = " + size + ", Faktor a = " + factor + " ===");

                // 1. Hashtabelle erzeugen
                HashTable ht = new HashTable(size, factor);

                // 2. Zufällige, paarweise verschiedene Schlüssel erzeugen
                int[] keys = generateDistinctKeys(numberOfKeys, 0, 1000);

                // 3. Einfügen
                for (int key : keys) {
                    ht.insert(key);
                }

                // 4. Auswertung
                int[] chainLengths = ht.getChainLengths();

                // Belegungsfaktor μ (durchschnittliche Einträge pro Index)
                double mu = (double) numberOfKeys / size;

                // Berechnung der "Mean Squared Deviation" (MSD = sqrt(MSE))
                double msd = computeMSD(chainLengths, mu);

                // Anzahl Kollisionen
                int collisions = ht.getCollisionCount();

                // Verhältnis belegte Tabellenplätze / Tabellengröße
                int usedSlots = 0;
                for (int length : chainLengths) {
                    if (length > 0) {
                        usedSlots++;
                    }
                }
                double ratio = (double) usedSlots / size;

                // 5. Ausgabe
                System.out.printf("Eingefügte Schlüssel: %d\n", numberOfKeys);
                System.out.printf("Belegungsfaktor µ = %.3f\n", mu);
                System.out.printf("MSD (Mean Squared Deviation) = %.3f\n", msd);
                System.out.printf("Kollisionen = %d\n", collisions);
                System.out.printf("Anteil belegter Plätze = %.3f\n", ratio);
                System.out.println();
            }
        }
    }

    // Liefert zufällige, paarweise verschiedene Schlüssel
    private static int[] generateDistinctKeys(int count, int minValue, int maxValue) {
        if (maxValue - minValue < count) {
            throw new IllegalArgumentException("Nicht genug Werte im Bereich!");
        }
        Set<Integer> set = new HashSet<>();
        Random rand = new Random();

        while (set.size() < count) {
            int candidate = rand.nextInt(maxValue - minValue + 1) + minValue;
            set.add(candidate);
        }

        // Konvertieren in Array
        int[] result = new int[count];
        int i = 0;
        for (int val : set) {
            result[i++] = val;
        }
        return result;
    }

    // MSD-Berechnung = sqrt( (1/N) * ∑(xi - µ)² )
    private static double computeMSD(int[] chainLengths, double mu) {
        double sumSq = 0.0;
        for (int length : chainLengths) {
            double diff = length - mu;
            sumSq += diff * diff;
        }
        double mse = sumSq / chainLengths.length;   // Mittelwert der quadratischen Abweichung
        return Math.sqrt(mse);                     // MSD ist die Wurzel daraus
    }
}


// 3a)
class HashTable {
    private HashNode[] table;  // Array von verketteten Listen
    private int size;          // Tabellengröße m
    private int factorA;       // Faktor a
    private int collisionCount; // Zum Zählen der Kollisionen

    // Konstruktor
    public HashTable(int size, int factorA) {
        this.size = size;
        this.factorA = factorA;
        this.table = new HashNode[size];
        this.collisionCount = 0;
    }
    
    // Hashfunktion: h(k) = (a * k) mod m
    private int hash(int key) {
        return (factorA * key) % size;
    }
    
    // Schlüssel einfügen
    public void insert(int key) {
        int index = hash(key);
        
        // Prüfen, ob an dieser Stelle bereits ein Eintrag liegt
        if (table[index] != null) {
            // Kollision
            collisionCount++;
        }
        
        // Neuen Knoten vorn an die verkettete Liste hängen
        HashNode newNode = new HashNode(key);
        newNode.next = table[index]; 
        table[index] = newNode; 
    }
    
    // Liefert Anzahl der Kollisionen
    public int getCollisionCount() {
        return collisionCount;
    }

    // Liefert eine Array-Darstellung der Kettenlängen, um MSD & Co. zu berechnen
    public int[] getChainLengths() {
        int[] chainLengths = new int[size];
        for (int i = 0; i < size; i++) {
            int length = 0;
            HashNode current = table[i];
            while (current != null) {
                length++;
                current = current.next;
            }
            chainLengths[i] = length;
        }
        return chainLengths;
    }
}


class HashNode {
    int key;       // Schlüssel
    HashNode next; // Nächstes Element in der Kette
    
    public HashNode(int key) {
        this.key = key;
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
 * Viele Kollisionen bedeutet häufiges Einfügen an bereits belegten Positionen.
 * Viele Kollisionen resultieren oft aus ungeeignetem Faktor a oder einer zu kleinen Tabellengröße m.
 * 
 * Anteil belegter Plätze zeigt an, wie viele Indizes tatsächlich genutzt werden.
 * Wenn Anteil trotz hohem μ sehr niedrig, dann ist Verteilung ungleichmäßig.
 */
