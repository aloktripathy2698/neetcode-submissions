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
    int diameter;

    public int dfs(TreeNode node){
        if(node == null)
            return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        diameter = Math.max(diameter, left + right);
        return 1 + Math.max(left, right);
    }
    
    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;
        dfs(root);
        return diameter;
    }
}
