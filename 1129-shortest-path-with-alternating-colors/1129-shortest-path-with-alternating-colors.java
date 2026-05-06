import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {

        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();

        // color: 0 = red, 1 = blue
        for (int[] e : redEdges) graph[e[0]].add(new int[]{e[1], 0});
        for (int[] e : blueEdges) graph[e[0]].add(new int[]{e[1], 1});

        int[] res = new int[n];
        Arrays.fill(res, -1);

        boolean[][] visited = new boolean[n][2];

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0}); // start with red
        q.add(new int[]{0, 1}); // start with blue

        visited[0][0] = true;
        visited[0][1] = true;

        int dist = 0;

        while (!q.isEmpty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                int node = curr[0];
                int color = curr[1];

                if (res[node] == -1) res[node] = dist;

                for (int[] nei : graph[node]) {
                    int next = nei[0];
                    int nextColor = nei[1];

                    if (nextColor != color && !visited[next][nextColor]) {
                        visited[next][nextColor] = true;
                        q.add(new int[]{next, nextColor});
                    }
                }
            }
            dist++;
        }

        return res;
    }
}