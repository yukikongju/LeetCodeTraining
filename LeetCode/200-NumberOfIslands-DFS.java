class Solution {
    public int numIslands(char[][] grid) {
	// Depth First Search
	int count = 0;
	for(int i=0; i<grid.length; i++){
	    for(int j=0; j<grid[0].length; j++){
		if(grid[i][j] == '1'){
		    dfs(grid, i, j);
		    count++;
		}
	    }
	}
	return count;
    }

    public void dfs(char[][]grid, int line, int column){
 	if(line>=0 && column >=0 && line<grid.length && column<grid[0].length && grid[line][column] == '1'){
	    grid[line][column] = '0';
	    dfs(grid, line-1, column); // left
	    dfs(grid, line+1, column); // right
	    dfs(grid, line, column+1); // up
	    dfs(grid, line, column-1); // down
	}
    }
}
