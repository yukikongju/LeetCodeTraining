#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int countVisibleTrees(vector<vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();

    // cout << m << ' ' << n << '\n';

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

int getHighestScenicScore(vector<vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();
    // 1. compute scenic score for each trees
    vector<vector<int>> scores(m, vector<int>(n, 0));
    // int i1, j1, currentMax;
    for (int i=1; i<m-1; ++i) {
	for (int j=1; j<n-1; ++j) {
	    int k1=0, k2=0, k3=0, k4=0;
	    // up
	    int i1=i, j1=j, currentMax=grid[i][j];
	    while ((i1>0) && (grid[i1-1][j] < currentMax)) {
		currentMax=max(grid[i1-1][j],currentMax);
		--i1;
	    }
	    k1 = i-i1+(i1!=0);

	    //down
	    i1=i; currentMax=grid[i][j];
	    while((i1<m-1) && (grid[i1+1][j] < currentMax)) {
		currentMax=max(grid[i1+1][j], currentMax);
		++i1;
	    }
	    k2 = i1-i+(i1!=m-1);

	    // left
	    j1=j; currentMax=grid[i][j];
	    // cout << j1 << '\n';
	    while((j1>0) && (grid[i][j1-1] < currentMax)) {
		currentMax=max(grid[i][j-1], currentMax);
		--j1;
	    }
	    // cout << j1 << '\n';
	    k3 = j-j1+(j1!=0);

	    // right
	    j1=j; currentMax=grid[i][j];
	    while((j1<n-1) && (grid[i][j1+1] < currentMax)) {
		currentMax=max(grid[i][j1+1], currentMax);
		++j1;
	    }
	    k4 = j1-j+(j1!=n-1);

	    // cout << i << ' ' << j << '\n';
	    // cout << k1 << ' ' << k2 << ' ' << k3 << ' ' << k4 << '\n';


	    // compute score
	    scores[i][j] = k1*k2*k3*k4;
	}
    }

    // print
    // for (int i=0; i<m; ++i) {
    //     for (int j=0; j<n; ++j) cout << scores[i][j] << ' ';
    //     cout << '\n';
    // }

    // 2. find the tree with highest score
    int highestScore = 0;
    for (int i=0; i<m; ++i) {
	for (int j=0; j<n; ++j) 
	    highestScore = max(highestScore, scores[i][j]);
    }

    return highestScore;
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
    int score = getHighestScenicScore(grid);
    cout << "[ PART 2 ] Highest Scenic Score: " << score << '\n';

    return 0;
}

