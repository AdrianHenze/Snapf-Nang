import java.util.ArrayList;
import java.util.List;

// 4c)
public class TestGraph {
    public static void main(String[] args) {
        // Beispielgraph mit 5 Knoten
        Graph g = new Graph(5);

        // Kanten hinzufügen (ungerichtet)
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);

        // DFS ausführen
        g.dfs();

        // Nachbarn auflisten
        System.out.println("\nNachbarschaftsliste");
        for (int i = 0; i < g.getNumberOfNodes(); i++) {
            System.out.println("Knoten " + i + ": " + g.getAdjacencyList().get(i));
        }
    }
}



// 4a)
class Graph {
    private List<List<Integer>> adjacencyList;  // Liste aller Nachbarschaften
    private int numberOfNodes;

    public Graph(int numberOfNodes) {
        this.numberOfNodes = numberOfNodes;
        adjacencyList = new ArrayList<>(numberOfNodes);
        for (int i = 0; i < numberOfNodes; i++) {
            adjacencyList.add(new ArrayList<>());   // jeweilige Nachbarschaftsliste
        }
    }

    // Ungerichtete Kante
    public void addEdge(int a, int b) {
        adjacencyList.get(a).add(b);
        adjacencyList.get(b).add(a);
    }

    // Gerichtete Kante (für aufgabe 4d)
    public void addDirectedEdge(int src, int dest) {
        adjacencyList.get(src).add(dest);
    }

    public void dfs() {
        boolean[] visited = new boolean[numberOfNodes]; 
        // Startet suche für unbesuchte Knoten
        for (int i = 0; i < numberOfNodes; i++) {
            if (!visited[i]) {
                dfsRecursive(i, visited);
            }
        }
    }

    // Rekursive DFS-Hilfsmethode
    private void dfsRecursive(int currentNode, boolean[] visited) {
        visited[currentNode] = true;    // Knoten als besucht markiert
        System.out.println("Besuche Knoten: " + currentNode);   // Zum Prüfen
        // Geh alle Nachbarn durch und führe gegebenfalls DFS durch
        for (int neighbor : adjacencyList.get(currentNode)) {
            if (!visited[neighbor]) {
                dfsRecursive(neighbor, visited);
            }
        }
    }

    // Getter für die Nachbarschaftsliste
    public List<List<Integer>> getAdjacencyList() {
        return adjacencyList;
    }

    // Getter für die Knotenanzahl
    public int getNumberOfNodes() {
        return numberOfNodes;
    }
}


/*
 * 4b)
 * DFS besucht jeden Knoten genau einmal.
 * Für jeden Knoten werden sämtliche Kanten zu Nachbarn durchlaufen.
 * Im gerichteten Graphen wird jede Kante genau einmal betrachtet.
 * DFS Zeitkomplexität: O(Knotenmenge + Kantenmenge)
 */