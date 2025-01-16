
// 4d)
public class TestCycle {
    public static void main(String[] args) {
        CycleDetectGraph g = new CycleDetectGraph(5);

        // Kanten (gerichtet) hinzufügen
        g.addDirectedEdge(0, 1);
        g.addDirectedEdge(1, 2);
        g.addDirectedEdge(2, 3);
        // g.addDirectedEdge(3, 1);  // Entkommentieren, um Zyklus zu erzeugen

        boolean hasCycle = g.detectCycle();
        System.out.println("Hat der Graph einen Zyklus? " + hasCycle);

        // Z.B. Kante (3->1) aktivieren → es sollte true ergeben
    }
}


class CycleDetectGraph extends Graph {

    // Konstruktor
    public CycleDetectGraph(int numberOfNodes) {
        super(numberOfNodes);
    }

    // Zyklensuche starten: true = Zyklus gefunden, false = kein Zyklus
    public boolean detectCycle() {
        boolean[] visited = new boolean[getNumberOfNodes()];
        boolean[] recStack = new boolean[getNumberOfNodes()];

        for (int i = 0; i < getNumberOfNodes(); i++) {
            if (!visited[i]) {
                if (dfsCycle(i, visited, recStack)) {
                    return true; // Zyklus entdeckt
                }
            }
        }
        return false; // Kein Zyklus gefunden
    }

    // DFS-Hilfsmethode zur Zyklenerkennung
    private boolean dfsCycle(int node, boolean[] visited, boolean[] recStack) {
        visited[node] = true;
        recStack[node] = true;

        for (int neighbor : getAdjacencyList().get(node)) {
            // Noch unbesucht → tiefere DFS
            if (!visited[neighbor] && dfsCycle(neighbor, visited, recStack)) {
                return true;
            }
            // Bereits im aktiven Pfad → Zyklus
            else if (recStack[neighbor]) {
                return true;
            }
        }

        // Knoten verlässt aktiven Pfad
        recStack[node] = false;
        return false;
    }
}
