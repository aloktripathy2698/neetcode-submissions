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
    private int maxDiameter;

    public int diameterOfBinaryTree(TreeNode root) {
        maxDiameter = 0;
        dfs(root);
        return maxDiameter;
    }

    public int dfs(TreeNode node) {
        if (node == null)
            return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        maxDiameter = Math.max(maxDiameter, left + right);
        return 1 + Math.max(left, right);
    }
}
