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
    private int count = 0;

    public void dfs(TreeNode node, int max_value){
        if(node == null)
            return;
        if(node.val >= max_value){
            count++;
            max_value = node.val;
        }
        dfs(node.left, max_value);
        dfs(node.right, max_value);
    }
    public int goodNodes(TreeNode root) {
        dfs(root, root.val);
        return count;
    }
}
