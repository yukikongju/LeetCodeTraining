#include <bits/stdc++.h>

#define ll long long
#define mod 1000000007;

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> coins(n);
    for (int i=0; i<n; i++) cin >> coins[i];

    sort(coins.begin(), coins.end());


    vector<ll> dp(m+1, 0);
    for (int i=1; i<m+1; i++) {
	for (int j=0; j<n; j++) {
	    ll left = (i-coins[j]>=0) ? dp[i-coins[j]] : 0;
	    ll equal = coins[j] == i ? 1 : 0;
	    dp[i] = (dp[i] + left + equal) % mod;
	}
    }

    cout << dp[m] << '\n';


    return 0;
}
