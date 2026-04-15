class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> maxD = new ArrayDeque<>();
        Deque<Integer> minD = new ArrayDeque<>();

        int left = 0, ans = 0;

        for (int right = 0; right < nums.length; right++) {
            while (!maxD.isEmpty() && nums[maxD.peekLast()] < nums[right]) {
                maxD.pollLast();
            }
            while (!minD.isEmpty() && nums[minD.peekLast()] > nums[right]) {
                minD.pollLast();
            }

            maxD.offerLast(right);
            minD.offerLast(right);

            while (nums[maxD.peekFirst()] - nums[minD.peekFirst()] > limit) {
                if (maxD.peekFirst() == left) maxD.pollFirst();
                if (minD.peekFirst() == left) minD.pollFirst();
                left++;
            }

            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
