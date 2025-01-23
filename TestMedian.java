// 1a)
class PriorityHeap {
    private final int[] heap;
    private final boolean isMaxHeap;
    private int numOfElements;

    public PriorityHeap(boolean isMaxHeap, int capacity) {
        this.isMaxHeap = isMaxHeap;
        this.heap = new int[capacity];
        this.numOfElements = 0;
    }


    // Schlusslicht einfügen.
    public void insert(int value) {
        heap[numOfElements] = value;
        heapifyUp(numOfElements);
        numOfElements++;
    }


    // Sorge dafür, dass der Parent dem Heap entsprechend ist.
    private void heapifyUp(int i) {
        int parent = (i - 1) / 2;
        while (i > 0 && compare(heap[i], heap[parent])) {
            swap(i, parent);
            i = parent;
            parent = (i - 1) / 2;
        }
    }


    // Oberstes Element zurückgeben und entfernen.
    public int extractTop() {
        int topValue = heap[0];
        heap[0] = heap[numOfElements - 1];
        numOfElements--;
        heapifyDown(0);
        return topValue;
    }


    private void heapifyDown(int i) {
        while (true) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int target = i;

            // Linkes und Rechtes Kind 
            if (left < numOfElements && compare(heap[left], heap[target])) {
                target = left;
            }
            if (right < numOfElements && compare(heap[right], heap[target])) {
                target = right;
            }
            // Unverändert
            if (target == i) {
                break;
            }
            swap(i, target);
            i = target;
        }
    }


    private boolean compare(int a, int b) {
        // Max-Heap: a > b
        // Min-Heap: a < b
        return isMaxHeap ? (a > b) : (a < b);
    }


    private void swap(int i, int j) {
        int tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    }


    public int peek() {
        return heap[0];
    }


    public int numberOfElements() {
        return numOfElements;
    }
}


// 1b)
class Median {
    private final PriorityHeap maxHeap; // untere Hälfte
    private final PriorityHeap minHeap; // obere Hälfte
    private double median;

    public Median(int capacity) {
        this.maxHeap = new PriorityHeap(true, capacity);
        this.minHeap = new PriorityHeap(false, capacity);
        this.median = 0.0;
    }


    public double addNumberAndCalculateMedian(int newNumber) {
        // Beim ersten Element
        if (maxHeap.numberOfElements() == 0 && minHeap.numberOfElements() == 0) {
            maxHeap.insert(newNumber);
            median = newNumber;
            return median;
        }
        // Max-Heap größer
        if (maxHeap.numberOfElements() > minHeap.numberOfElements()) {
            if (newNumber < median) {
                int resettler = maxHeap.extractTop();
                minHeap.insert(resettler);
                maxHeap.insert(newNumber);
            } else {
                minHeap.insert(newNumber);
            }
            median = (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        // Min-Heap größer
        else if (maxHeap.numberOfElements() < minHeap.numberOfElements()) {
            if (newNumber > median) {
                int resettler = minHeap.extractTop();
                maxHeap.insert(resettler);
                minHeap.insert(newNumber);
            } else {
                maxHeap.insert(newNumber);
            }
            median = (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        // Beide gleich groß
        else {
            if (newNumber < median) {
                maxHeap.insert(newNumber);
                median = maxHeap.peek();
            } else {
                minHeap.insert(newNumber);
                median = minHeap.peek();
            }
        }
        return median;
    }
}


// 1c)
public class TestMedian {
    public static void main(String[] args) {
        // Beispiel 1
        Median medianCalculator = new Median(10);
        int[] nums1 = {2, 8, 12, 19, 22, 34, 49, 63};
        System.out.println("Beispiel 1:");
        for (int num : nums1) {
            double median = medianCalculator.addNumberAndCalculateMedian(num);
            System.out.println("Eingefügt: " + num + "; Median: " + median);
        }
        // Beispiel 2
        medianCalculator = new Median(10);
        int[] nums2 = {1, 4, 13, 21, 42, 69};
        System.out.println("\nBeispiel 2:");
        for (int num : nums2) {
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
