package graphalgorithms;

import java.util.HashMap;
import java.util.Map;

public class Graph {
    private final Map<String, Vertex> graph;

    public Graph(Edge[] edges){
        graph = new HashMap<>();
        
        // find all vertices
        for(Edge e: edges){
            if(!graph.containsKey(e.v1)) graph.put(e.v1, new Vertex(e.v1));
            if(!graph.containsKey(e.v2)) graph.put(e.v2, new Vertex(e.v1));
        }
        
        // set neighboring vertices
        for(Edge e: edges){
            graph.get(e.v1).neighbours.put(graph.get(e.v2), e.dist);
        }
    }
    
    public static class Edge {
        public final String v1, v2; // starting node -> end node
        public final int dist;

        public Edge(String v1, String v2, int dist) {
            this.v1 = v1;
            this.v2 = v2;
            this.dist = dist;
        }
    }
    
    public static class Vertex implements Comparable<Vertex> {

        public final String name;
        public int dist = Integer.MAX_VALUE; // the distance from node to end is initialized to infinity
        public Vertex previous = null;
        public final Map<Vertex, Integer> neighbours = new HashMap<>();

        public Vertex(String name) {
            this.name = name;
        }

        @Override
        public int compareTo(Vertex t) {
            if (dist == t.dist) {
                return name.compareTo(t.name);
            }
            return Integer.compare(dist, t.dist);
        }

        private void printPath() { // TODO
        }

        @Override
        public String toString() {
            return "(" + name + ", " + dist + ")";
        }

        @Override
        public boolean equals(Object object) {
            if (this == object) return true;
            if (object == null || getClass() != object.getClass()) return false;
            if (!super.equals(object)) return false;

            Vertex vertex = (Vertex) object;

            if (dist != vertex.dist) return false;
            if (name != null ? !name.equals(vertex.name) : vertex.name != null) return false;
            if (previous != null ? !previous.equals(vertex.previous) : vertex.previous != null) return false;
            if (neighbours != null ? !neighbours.equals(vertex.neighbours) : vertex.neighbours != null) return false;

            return true;
        }

        @Override
        public int hashCode() {
            int result = super.hashCode();
            result = 31 * result + (name != null ? name.hashCode() : 0);
            result = 31 * result + dist;
            result = 31 * result + (previous != null ? previous.hashCode() : 0);
            result = 31 * result + (neighbours != null ? neighbours.hashCode() : 0);
            return result;
        }

    }

}
