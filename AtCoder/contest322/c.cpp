#include <bits/stdc++.h>
#include <vector>
using namespace std;


int main() {
    // 1. read inputs
    int n, m;
    cin >> n >> m; 
    vector<int> v(m);
    for (int i = 0; i < m; ++i) cin >> v[i];

    // 2. dp
    vector<int> res(n+1);
    vector<bool> fireworks(n+1);
    for (int i = 0; i < m; ++i) fireworks[v[i]] = true;

    int last = n;
    for (int i = n ; i >= 0; --i) {
	if (fireworks[i]) last = i;
	res[i] = last - i;
    }

    // 3. print results
    for (int i = 1; i <= n; ++i) cout << res[i] << endl;

    return 0;
}
