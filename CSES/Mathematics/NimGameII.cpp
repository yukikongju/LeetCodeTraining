#include <fstream>
#include <iostream>
#include <vector>
#include <math.h>


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
	vector<int> A(m);
	int L=1, R=3;
	for (int j=0; j<m; ++j) {
	    cin >> A[j];
	    A[j] = A[j] % (L+R);
	    total = total ^ (int) floor(A[j] / L);
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


