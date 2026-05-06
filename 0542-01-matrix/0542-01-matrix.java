import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        Queue<int[]> q = new LinkedList<>();

        // Step 1: initialize queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    q.add(new int[]{i, j});
                } else {
                    mat[i][j] = -1; // mark unvisited
                }
            }
        }

        int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};

        // Step 2: BFS
        while (!q.isEmpty()) {
            int[] curr = q.poll();

            for (int[] d : dir) {
                int x = curr[0] + d[0];
                int y = curr[1] + d[1];

                if (x>=0 && y>=0 && x<m && y<n && mat[x][y] == -1) {
                    mat[x][y] = mat[curr[0]][curr[1]] + 1;
                    q.add(new int[]{x, y});
                }
            }
        }

        return mat;
    }
}