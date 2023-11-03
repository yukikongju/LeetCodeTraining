#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  int mod = 1e9 + 7;

  vector<int> prices(N);
  vector<int> pages(N);
  for (int i = 0; i < N; ++i)
    cin >> prices[i];
  for (int i = 0; i < N; ++i)
    cin >> pages[i];

  //
  vector<vector<int>> dp(N + 1, vector<int>(M + 1, 0));
  for (int i = 1; i < N + 1; ++i) {
    for (int j = 0; j < M + 1; ++j) {
      int top = dp[i - 1][j];
      if (j - prices[i - 1] >= 0) {
        int left = dp[i - 1][j - prices[i - 1]] + pages[i - 1];
        dp[i][j] = max(left, top) % mod;
      } else {
        dp[i][j] = top % mod;
      }
    }
  }

  cout << dp[N][M] << '\n';

  return 0;
}
