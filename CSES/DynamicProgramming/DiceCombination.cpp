// Solution: f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5) + f(n-6)

#include <vector>
#include <iostream>

using namespace std;


int main() {
    // 
    int n;
    cin >> n;
    int MOD = 1000000007;

    //
    vector<long> dp(n+1, 0);
    dp[0] = 1;

    for (int i=1; i<n+1; ++i) {
	for (int j=1; j <= 6; ++j) {
	    if (j>i) break;
	    dp[i] = (dp[i] + dp[i-j]) % MOD;
	}
    }

    cout << dp[n] << '\n';

    return 0;
}

