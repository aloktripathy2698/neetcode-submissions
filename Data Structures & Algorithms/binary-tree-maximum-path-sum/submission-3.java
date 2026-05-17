/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int maxPathSum;
    public int maxPathSum(TreeNode root) {
        if(root == null)
            return 0;
        maxPathSum = Integer.MIN_VALUE;
        dfs(root);
        return maxPathSum;
    }

    public int dfs(TreeNode node){
        if(node == null)
            return 0;
        int left = dfs(node.left);
        left = left < 0 ? 0 : left;
        int right = dfs(node.right);
        right = right < 0 ? 0 : right;
        maxPathSum = Math.max(maxPathSum, node.val + left + right);
        return node.val + Math.max(left, right);
    }
}
