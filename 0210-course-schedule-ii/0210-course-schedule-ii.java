class Solution {
    public int[] findOrder(int n, int[][] pre) {
        List<List<Integer>> g = new ArrayList<>();
        int[] in = new int[n];

        for (int i = 0; i < n; i++) g.add(new ArrayList<>());

        for (int[] p : pre) {
            g.get(p[1]).add(p[0]);
            in[p[0]]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++)
            if (in[i] == 0) q.add(i);

        int[] res = new int[n];
        int idx = 0;

        while (!q.isEmpty()) {
            int c = q.poll();
            res[idx++] = c;

            for (int nei : g.get(c)) {
                if (--in[nei] == 0) q.add(nei);
            }
        }

        return idx == n ? res : new int[0];
    }
}