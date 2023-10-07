// https://atcoder.jp/contests/abc322/tasks/abc322_a

#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;


int main() {
    // 1. read inputs
    int n; 
    cin >> n;
    string s;
    cin >> s;

    // 2. find index
    for (int i = 0; i < n-2; i++) {
	if (s.substr(i, 3) == "ABC") {
	    cout << i+1 << endl;
	    return 0;
	}
    }

    cout << -1 << endl;
    return 0;

}

