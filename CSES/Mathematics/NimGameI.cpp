#include <fstream>
#include <iostream>
#include <vector>

using namespace std;


int main() {
    // 1. read inputs
    int N;
    cin >> N;

    // 2. compute nim sum
    for (int i=0; i<N; ++i) {
    int total=0;
	int m;
	cin >> m;
	int A[m];
	for (int j=0; j<m; ++j) {
	    cin >> A[j];
	    total ^= A[j];
	}

	// 3. print results
	if (total == 0) {
	    cout << "second" << '\n';
	} else {
	    cout << "first" << '\n';
	}

    }



    return 0;
}


