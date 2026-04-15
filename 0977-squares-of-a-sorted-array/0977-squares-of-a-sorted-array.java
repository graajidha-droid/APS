class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];

        int l = 0, r = n - 1, k = n - 1;

        while (l <= r) {
            int leftSq = nums[l] * nums[l];
            int rightSq = nums[r] * nums[r];

            if (leftSq > rightSq) {
                res[k--] = leftSq;
                l++;
            } else {
                res[k--] = rightSq;
                r--;
            }
        }
        return res;
    }
}
