class PriorityHeap {
    private final int[] heap;
    private final boolean isMaxHeap;
    private int size; // Anzahl gespeicherter Elemente

    public PriorityHeap(boolean isMaxHeap, int capacity) {
        this.isMaxHeap = isMaxHeap;
        this.heap = new int[capacity];
        this.size = 0;
    }

    public int numberOfElements() {
        return size;
    }

    public void insert(int value) {
        if (size == heap.length) {
            throw new IllegalStateException("Heap ist voll!");
        }
        // Einfügen am Ende
        heap[size] = value;
        // Nach oben heapify
        heapifyUp(size);
        size++;
    }

    public int peek() {
        if (size == 0) {
            throw new IllegalStateException("Heap ist leer!");
        }
        return heap[0];
    }

    public int extractTop() {
        if (size == 0) {
            throw new IllegalStateException("Heap ist leer!");
        }
        int topValue = heap[0];
        // Letztes Element nach vorne
        heap[0] = heap[size - 1];
        size--;
        // Nach unten heapify
        heapifyDown(0);
        return topValue;
    }

    private void heapifyUp(int index) {
        int parent = (index - 1) / 2;
        while (index > 0 && compare(heap[index], heap[parent])) {
            swap(index, parent);
            index = parent;
            parent = (index - 1) / 2;
        }
    }

    private void heapifyDown(int index) {
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int target = index;

            // Linkes Kind
            if (left < size && compare(heap[left], heap[target])) {
                target = left;
            }
            // Rechtes Kind
            if (right < size && compare(heap[right], heap[target])) {
                target = right;
            }
            // Keine Änderung ⇒ fertig
            if (target == index) {
                break;
            }
            swap(index, target);
            index = target;
        }
    }

    // Vergleich abhängig davon, ob Max- oder Min-Heap
    private boolean compare(int a, int b) {
        // Max-Heap: a > b ⇒ true
        // Min-Heap: a < b ⇒ true
        return isMaxHeap ? (a > b) : (a < b);
    }

    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
}


class Median {
    private final PriorityHeap maxHeap; // untere Hälfte
    private final PriorityHeap minHeap; // obere Hälfte
    private double currentMedian;

    public Median(int capacity) {
        // Kapazität je nach Bedarf für beide Heaps angeben
        this.maxHeap = new PriorityHeap(true, capacity);
        this.minHeap = new PriorityHeap(false, capacity);
        this.currentMedian = 0.0;
    }

    public double addNumberAndCalculateMedian(int newNumber) {
        // Sonderfall: erstes Element
        if (maxHeap.numberOfElements() == 0 && minHeap.numberOfElements() == 0) {
            maxHeap.insert(newNumber);
            currentMedian = newNumber;
            return currentMedian;
        }

        // Falls Max-Heap größer
        if (maxHeap.numberOfElements() > minHeap.numberOfElements()) {
            if (newNumber < currentMedian) {
                int verschoben = maxHeap.extractTop();
                minHeap.insert(verschoben);
                maxHeap.insert(newNumber);
            } else {
                minHeap.insert(newNumber);
            }
            currentMedian = (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        // Falls Min-Heap größer
        else if (maxHeap.numberOfElements() < minHeap.numberOfElements()) {
            if (newNumber > currentMedian) {
                int verschoben = minHeap.extractTop();
                maxHeap.insert(verschoben);
                minHeap.insert(newNumber);
            } else {
                maxHeap.insert(newNumber);
            }
            currentMedian = (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        // Beide gleich groß
        else {
            if (newNumber < currentMedian) {
                maxHeap.insert(newNumber);
                currentMedian = maxHeap.peek();
            } else {
                minHeap.insert(newNumber);
                currentMedian = minHeap.peek();
            }
        }

        return currentMedian;
    }
}


public class TestMedian {
    public static void main(String[] args) {
        Median medianCalculator = new Median(10);

        // Beispiel 1
        int[] input1 = {5, 10, 15};
        System.out.println("Beispiel 1:");
        for (int num : input1) {
            double median = medianCalculator.addNumberAndCalculateMedian(num);
            System.out.println("Eingefügt: " + num + "; Median: " + median);
        }

        // Neuer Median-Rechner für Beispiel 2
        medianCalculator = new Median(10);

        // Beispiel 2
        int[] input2 = {1, 2, 3, 4};
        System.out.println("\nBeispiel 2:");
        for (int num : input2) {
            double median = medianCalculator.addNumberAndCalculateMedian(num);
            System.out.println("Eingefügt: " + num + "; Median: " + median);
        }
    }
}


/*
 * 1d)
 * Zeitkomplexität: O(n log n)
 * Speicherkomplexität: O(n)
 */
