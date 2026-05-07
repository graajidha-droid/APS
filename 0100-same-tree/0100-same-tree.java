class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        // If both nodes are null
        if (p == null && q == null) {
            return true;
        }

        // If one is null and other is not
        if (p == null || q == null) {
            return false;
        }

        // If values are different
        if (p.val != q.val) {
            return false;
        }

        // Check left and right subtrees
        return isSameTree(p.left, q.left) &&
               isSameTree(p.right, q.right);
    }
}