#include <bits/stdc++.h>
#include <algorithm>
#include <vector>

#define ll long long
#define inf (1LL<<60)
// #define infty numeric_limits<int>::max()


using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> coins(n);
    for(int i=0; i<n; ++i) cin >> coins[i];

    sort(coins.begin(), coins.end());

    vector<ll> dp(m+1, inf);
    dp[0] = 0;

    for (int i=1; i<=m; i++) {
	for (int j=0; j<n; j++) {
	    if(i >= coins[j])
		dp[i] = min(dp[i], dp[i-coins[j]] + 1);
	}
    }

    if (dp[m] == inf) cout << "-1" << '\n';
    else cout << dp[m] << '\n';

    return 0;
}
