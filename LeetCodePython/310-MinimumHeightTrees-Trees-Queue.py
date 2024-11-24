#  https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Solution: Tree - BFS Topological Sort - O(n)
        # V = n ; E = n - 1
        # Tree Properties
        # 1. A tree is an undirected graph in which any two vertices are connected by exactly one path.
        # 2. Any connected graph who has n nodes with n-1 edges is a tree.
        # 3. The degree of a vertex of a graph is the number of edges incident to the vertex.
        # 4. A leaf is a vertex of degree 1. An internal vertex is a vertex ofdegree at least 2.
        # 5. A path graph is a tree with two or more vertices that is not branched at all.
        # 6. A tree is called a rooted tree if one vertex has been designated the root.
        # 7. The height of a rooted tree is the number of edges on the longest downward path between root and a leaf.

        ### Intuition: remove the leaves iteratively 

        if n == 1: return [0]

        ## Build the graph 
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        

        ## Remove the leaves iteratively until root remains
        leaves = [node for node in range(n) if len(adj[node]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                node = adj[i].pop()
                adj[node].remove(i)
                if len(adj[node]) == 1: new_leaves.append(node)
            leaves = new_leaves
            
        return leaves
        
