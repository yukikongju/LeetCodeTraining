class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // recursive implementation
        // 1. traverse left subtree
        // 2. visit node
        // 3. traverse right subtree
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        return values;
    }

    public void inorder(TreeNode node, List<Integer> values){
        if(node != null) {
            if (node.left != null) inorder(node.left, values);
            values.add(node.val);
            if(node.right != null) inorder(node.right, values);
        }
    }

}
