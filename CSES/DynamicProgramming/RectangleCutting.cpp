#include <bits/stdc++.h>

// Idea: we can decide to cut horizontally or vertically for each rectangle
// if w=h: we need 0 cuts; else try to cut horizontally/vertically
// dp[i][j] => how many cut we need to get a rectangle of shape (i, j)

using namespace std;

int main() {
  int w, h;
  cin >> w >> h;

  vector<vector<int>> dp(h + 1, vector<int>(w + 1, 1e9));
  for (int i = 0; i <= h; i++) {
    for (int j = 0; j <= w; j++) {
      if (i == j)
        dp[i][j] = 0;
      else {
        // try cutting horizontally
        for (int k = 1; k < j; k++) {
          dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k] + 1);
        }

        // try cutting vertically
        for (int k = 1; k < i; k++) {
          dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1);
        }
      }
    }
  }

  cout << dp[h][w] << '\n';

  return 0;
}
