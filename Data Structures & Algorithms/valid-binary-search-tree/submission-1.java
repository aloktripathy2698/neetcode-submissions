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
    public boolean dfs(TreeNode node, int left_min, int right_max){
        if(node == null)
            return true;
        if(node.val <= left_min || node.val >= right_max)
            return false;
        return dfs(node.left, left_min, node.val) && dfs(node.right, node.val, right_max);
    }
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
}
