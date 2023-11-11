#include <bits/stdc++.h>
#include <numeric>

using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> coins(N);
  for (int i = 0; i < N; i++)
    cin >> coins[i];

  int maxSum = accumulate(coins.begin(), coins.end(), 0);

  // sort(coins.begin(), coins.end());
  vector<vector<bool>> dp(N + 1, vector<bool>(maxSum + 1, false));
  dp[0][0] = true;

  for (int i = 1; i <= N; i++) {
    for (int j = 0; j <= maxSum; j++) {
      int top = dp[i - 1][j];
      int left = (j - coins[i - 1] >= 0) ? dp[i - 1][j - coins[i - 1]] : 0;
      dp[i][j] = top || left;
    }
  }

  vector<int> possibilities;
  for (int j = 1; j <= maxSum; j++) {
    if (dp[N][j])
      possibilities.push_back(j);
  }

  cout << possibilities.size() << '\n';
  for (auto &p : possibilities)
    cout << p << ' ';
  cout << '\n';

  return 0;
}
