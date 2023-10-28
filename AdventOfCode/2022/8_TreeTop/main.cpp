#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int countVisibleTrees(vector<vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();

    cout << m << ' ' << n << '\n';

    //
    vector<vector<bool>> isVisible(m, vector<bool>(n, false));

    // up
    for (int j=0; j<n; ++j) {
	int currentMax = grid[m-1][j];
	isVisible[m-1][j]=true;
	for(int i=m-1; i>=0; --i) {
	    if (grid[i][j] > currentMax) {
		currentMax = grid[i][j];
		isVisible[i][j] = true;
	    }
	}
    }

    // down
    for (int j=0; j<n; ++j) {
	int currentMax = grid[0][j];
	isVisible[0][j];
	for (int i=0; i<m; ++i) {
	    if (grid[i][j] > currentMax) {
		currentMax = grid[i][j];
		isVisible[i][j] = true;
	    }
	}
    }

    // left
    for (int i=0; i<m; ++i) {
	int currentMax = grid[i][0];
	isVisible[i][0];
	for (int j=0; j<n; ++j) {
	    if (grid[i][j] > currentMax) {
		currentMax = grid[i][j];
		isVisible[i][j] = true;
	    }
	}
    }

    // right
    for (int i=0; i<m; ++i) {
	int currentMax = grid[i][n-1];
	isVisible[i][n-1];
	for (int j=n-1; j>=0; --j) {
	    if (grid[i][j] > currentMax) {
		isVisible[i][j] = true;
	    }
	    currentMax = max(grid[i][j], currentMax);
	}
    }

    // set border to true
    for (int j=0; j<n; j++) isVisible[0][j] = true;
    for (int j=0; j<n; j++) isVisible[m-1][j] = true;
    for (int i=0; i<m; i++) isVisible[i][0] = true;
    for (int i=0; i<m; i++) isVisible[i][n-1] = true;

    // 2. count number of visible trees
    int numVisibleTrees = 0;
    for (int i=0; i<m; ++i) {
	for (int j=0; j<n; ++j) {
	    if (isVisible[i][j]) numVisibleTrees++;
	}

    }

    // print
    // for (int i=0; i<m; ++i) {
    //     for (int j=0; j<n; ++j) cout << isVisible[i][j] << ' ';
    //     cout << '\n';
    // }

    return numVisibleTrees;
}



int main() {
    // 1. read inputs
    string FILENAME = "inputs/2.in";
    ifstream file(FILENAME);

    string line;
    vector<string> lines;
    while (getline(file, line)) lines.push_back(line);

    int m = lines.size();
    int n = lines[0].size();

    vector<vector<int>> grid(m, vector<int>(n, 0));
    for (int i=0; i<lines.size(); ++i) {
	for (int j=0; j<lines[0].size(); ++j) {
	    grid[i][j] = lines[i][j];
	}
    }

    // 2. [ PART 1 - Visible Trees ]
    int numVisibleTrees = countVisibleTrees(grid);
    cout << "[ PART 1 ] Number Visible Trees: " << numVisibleTrees << '\n';

    // 3. [ PART 2 ]


    return 0;
}

