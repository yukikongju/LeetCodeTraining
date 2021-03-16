class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        // recursive solution
        // 1. visit(node)
        // 2. preorder(node.left)
        // 3. preorder(node.right)
        List<Integer> values = new ArrayList<>();
        preorder(root, values);
        return values;
    }

    public void preorder(TreeNode node, List<Integer> values){
        if(node != null){
            values.add(node.val);
            if(node.left != null){
                preorder(node.left, values);
            }
            if(node.right != null){
                preorder(node.right, values);
            }
        }
    }
}
