class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        // recursive implementation
        // 1. Traverse left
        // 2. Traverse right
        // 3. Visit Node
        List<Integer> values = new ArrayList<>();
        postorder(root, values);
        return values;
    }

    public void postorder(TreeNode node, List<Integer> values){
        if(node != null){
            if(node.left != null) postorder(node.left, values);
            if(node.right != null) postorder(node.right, values);
            values.add(node.val);
        }
    }
}

/* Explanation: https://www.youtube.com/watch?v=4zVdfkpcT6U */
