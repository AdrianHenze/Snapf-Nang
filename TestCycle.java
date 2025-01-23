
// 4d)
public class TestCycle {
    public static void main(String[] args) {
        CycleDetectGraph g = new CycleDetectGraph(5);

        // gerichtete Kanten
        g.addDirectedEdge(0, 1);
        g.addDirectedEdge(1, 2);
        g.addDirectedEdge(2, 3);
        g.addDirectedEdge(3, 1);

        boolean hasCycle = g.detectCycle();
        if (hasCycle)
            System.out.println("Der Graph hat einen Kreis.");
        else 
            System.out.println("Der Graph hat keinen Kreis.");
    }
}


class CycleDetectGraph extends Graph {

    public CycleDetectGraph(int numberOfNodes) {
        super(numberOfNodes);
    }

    public boolean detectCycle() {
        boolean[] visited = new boolean[getNumberOfNodes()];
        boolean[] recStack = new boolean[getNumberOfNodes()];
        // Kreissuche starten
        for (int i = 0; i < getNumberOfNodes(); i++) {
            if (!visited[i] && dfsCycle(i, visited, recStack)) {
                return true; // Kreis entdeckt
            }
        }
        return false; // Kein Kreis gefunden
    }

    // DFS-Hilfsmethode zur Kreiserkennung
    private boolean dfsCycle(int node, boolean[] visited, boolean[] recStack) {
        visited[node] = true;
        recStack[node] = true;  // Node zum Aktiven Pfad hinzufügen

        for (int neighbor : getAdjacencyList().get(node)) {
            // Noch unbesucht = tiefere DFS
            if ((!visited[neighbor] && dfsCycle(neighbor, visited, recStack)) || recStack[neighbor]) {
                return true;
            }
        }
        // Knoten verlässt aktiven Pfad
        recStack[node] = false;
        return false;
    }
}
