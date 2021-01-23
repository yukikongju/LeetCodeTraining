#!/usr/bin/java

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
    public boolean isSymmetric(TreeNode root) {
        // Recursive Solution
        return checkSymmetry(root, root);
    }
    
    private boolean checkSymmetry(TreeNode leftChild, TreeNode rightChild){
        if(leftChild == null && rightChild == null) return true;
        if(leftChild == null || rightChild == null) return false;
        
        return checkSymmetry(leftChild.right, rightChild.left) &&
            checkSymmetry(leftChild.left, rightChild.right) &&
            (leftChild.val == rightChild.val);
    }
}
