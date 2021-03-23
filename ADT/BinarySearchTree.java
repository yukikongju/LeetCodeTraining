public class BinarySearchTree<T extends Comparable<T>> {
    private Node root = null;
    private int nodeCount = 0;

    private class Node {
	Node left, right;
	T elem;

	public Node(Node left, Node right, T elem){
	    this.left = left;
	    this.right = right;
	    this.elem = elem;
	}

    }

    public boolean isEmpty(){
	return size() == 0;
    }

    public int size(){
	return nodeCount;
    }

    public Node findMin(Node node){ // find the minimum value in the subtree
	// parcourir le subtree jusqu'au fond gauche
	while(node.left != null) node = node.left;
	return node;
    }

    public Node findMax(Node node){
	// parcourir le subtree jusqu'au fond droit
	while(node.right != null) node = node.right;
	return node;
    }

    private int height(Node node){
	if(node == null) return 0;
	return Math.max(height(node.left), height(node.right)) + 1;
    }

    public boolean contains(Node node, T elem){
	int cmp = elem.compareTo(node.elem); // check if elem < node.elem
	if(cmp < 0) return contains(node.left, elem);
	else if(cmp > 0) return contains(node.right, elem);
	else return true;
    }

    public boolean contains(T elem){
	return contains(root, elem);
    }

    public void insert(T elem){
	root = insert(root, elem);
	nodeCount++;
    }

    private Node insert(Node node, T elem){
	if(node == null){
	    node = new Node(null, null, elem);
	} else {
	    int cmp = elem.compareTo(node.elem);
	    if(cmp < 0) insert(node.left, elem);
	    else if(cmp > 0) insert(node.right, elem);
	    // else node.val == elem -> on n'ajoute rien pcq no duplicate
	}
	return node;
    }



}

