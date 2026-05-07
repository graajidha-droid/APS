class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        
        // Create adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Build graph
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        // Visited array
        boolean[] visited = new boolean[n];

        // DFS traversal
        return dfs(graph, visited, source, destination);
    }

    private boolean dfs(List<List<Integer>> graph, boolean[] visited,
                        int node, int destination) {

        // If destination found
        if (node == destination) {
            return true;
        }

        visited[node] = true;

        // Visit neighbors
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(graph, visited, neighbor, destination)) {
                    return true;
                }
            }
        }

        return false;
    }
}