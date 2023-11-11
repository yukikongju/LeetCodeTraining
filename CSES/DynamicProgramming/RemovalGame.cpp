// Idea: player has two choices: take first, take last. if only one element
// left, then take it; dp[l][r] = max difference of score for stack[l:r]
// score1 = (S + (score1-score2)) / 2

#include <bits/stdc++.h>
#include <numeric>

#define ll long long

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> numbers(n);
  for (int i = 0; i < n; i++) {
    cin >> numbers[i];
  }

  vector<vector<ll>> dp(n, vector<ll>(n));
  for (int l = n - 1; l >= 0; l--) {
    for (int r = l; r < n; r++) {
      if (l == r)
        dp[l][r] = numbers[l];
      else {
        ll first = numbers[l] - dp[l + 1][r];
        ll last = numbers[r] - dp[l][r - 1];
        dp[l][r] = max(first, last);
      }
    }
  }

  ll sumTotal = accumulate(numbers.begin(), numbers.end(), 0LL);

  // cout << sumTotal << '\n';
  // cout << dp[0][n - 1] << '\n';
  cout << (sumTotal + dp[0][n - 1]) / 2 << '\n';

  return 0;
}
