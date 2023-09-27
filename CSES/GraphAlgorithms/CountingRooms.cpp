// https://cses.fi/problemset/task/1192/

#include <iostream>
#include <vector>
using namespace std;


vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0,1}, {0,-1}};

void printMaze(char maze[1000][1000], int n, int m) {
    for (int i = 0; i < n; i++) {
	for (int j = 0; j < m; ++j) {
	    cout << maze[i][j];
	}
	cout << endl;
    }
}

void dfs(char maze[1000][1000], int i, int j, int n, int m) {
    maze[i][j] = 'X';

    for (const auto& dir: directions) {
	int x = i + dir.first;
	int y = j + dir.second;

	if ((x>=0) && (x<n) && (y>=0) && (y<m) && (maze[x][y] == '.')) {
	    dfs(maze, x, y, n, m);
	}

    }
}


int main() {
    // --- 1. reading inputs
    int n, m;
    cin >> n >> m;

    char maze[1000][1000];
    for (int i = 0; i < n; ++i) {
	for (int j = 0; j < m; ++j) {
	    cin >> maze[i][j];
	}
    }

    // printMaze(maze, n, m);


    // --- 2. run dfs
    int num_rooms = 0;
    for (int i = 0; i < n; ++i) {
	for (int j = 0; j < m; ++j) {
	    if (maze[i][j] == '.') {
		num_rooms += 1;
		dfs(maze, i, j, n, m);
	    }
	}
    }

    // --- 3. print results
    cout << num_rooms << endl;


    return 0;
}

