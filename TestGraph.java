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
        System.out.println("== Starte DFS ==");
        g.dfs();

        // Nachbarn auflisten
        System.out.println("\n== Nachbarschaftsliste ==");
        for (int i = 0; i < g.getNumberOfNodes(); i++) {
            System.out.println("Knoten " + i + " → " + g.getAdjacencyList().get(i));
        }
    }
}



// 4a)
class Graph {
    private List<List<Integer>> adjacencyList; // Nachbarschaftsliste
    private int numberOfNodes;

    public Graph(int numberOfNodes) {
        this.numberOfNodes = numberOfNodes;
        adjacencyList = new ArrayList<>(numberOfNodes);
        for (int i = 0; i < numberOfNodes; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }

    // Ungerichtete Kante hinzufügen
    public void addEdge(int source, int destination) {
        adjacencyList.get(source).add(destination);
        adjacencyList.get(destination).add(source);
    }

    // Gerichtete Kante hinzufügen
    public void addDirectedEdge(int source, int destination) {
        adjacencyList.get(source).add(destination);
    }

    // DFS starten
    public void dfs() {
        boolean[] visited = new boolean[numberOfNodes];
        // Falls es mehrere nicht zusammenhängende Komponenten gibt,
        // jedes unbesuchte Node als neuen Startpunkt
        for (int i = 0; i < numberOfNodes; i++) {
            if (!visited[i]) {
                dfsRecursive(i, visited);
            }
        }
    }

    // Rekursive DFS-Hilfsmethode
    private void dfsRecursive(int currentNode, boolean[] visited) {
        visited[currentNode] = true;
        System.out.println("Besuche Knoten: " + currentNode);

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

    public int getNumberOfNodes() {
        return numberOfNodes;
    }
}


/*
 * 4b)
 * DFS besucht jeden Knoten genau einmal.
 * Für jeden Knoten werden sämtliche Kanten zu Nachbarn durchlaufen.
 * Im gerichteten Graphen wird jede Kante genau einmal betrachtet.
 * DFS Tiefensuche Komplexität: O(Knotenmenge + Kantenmenge)
 */