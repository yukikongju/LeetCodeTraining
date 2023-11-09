#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

int main() {
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  vector<string> chunks;
  string line;
  while (getline(file, line)) {
    chunks.push_back(line);
  }

  // for (auto &c : chunks)
  //   cout << c << '\n';

  map<char, int> illegalCharactersPoints = {
      {')', 3}, {']', 57}, {'}', 1197}, {'>', 25137}};
  map<char, char> bracketsMap = {
      {')', '('}, {']', '['}, {'}', '{'}, {'>', '<'}};
  set<char> opensChars = {'(', '[', '{', '<'};
  set<char> closedChars = {')', ']', '}', '>'};

  // [ PART 1 - ]
  vector<string> incompletesChunks;

  int syntaxScore = 0;
  for (auto &chunk : chunks) {
    stack<char> s;
    bool isCorrupted = false;
    for (auto &c : chunk) {
      if (opensChars.find(c) != opensChars.end()) {
        s.push(c);
      } else {
        char top = s.top();
        s.pop();
        if (bracketsMap[c] != top) {
          syntaxScore += illegalCharactersPoints[c];
          isCorrupted = true;
          break;
        }
      }
    }

    if (!isCorrupted) {
      incompletesChunks.push_back(chunk);
    }
  }

  cout << "[PART 1] Syntax Error Score: " << syntaxScore << '\n';

  // [PART 2]

  map<char, int> completionMap = {{')', 1}, {']', 2}, {'}', 3}, {'>', 4}};
  map<char, char> bracketsMapInverse = {
      {'(', ')'}, {'[', ']'}, {'{', '}'}, {'<', '>'}};
  vector<long long> missingScores;
  for (auto &chunk : incompletesChunks) {
    stack<char> s;
    for (auto &c : chunk) {
      if (opensChars.find(c) != opensChars.end()) {
        s.push(c);
      } else {
        s.pop();
      }
    }

    // compute score
    long long score = 0;
    while (!s.empty()) {
      score *= 5;
      char top = s.top();
      s.pop();
      score += completionMap[bracketsMapInverse[top]];
      // cout << top;
    }
    missingScores.push_back(score);
    // cout << '\n';
  }

  sort(missingScores.begin(), missingScores.end());

  // for (auto &s : missingScores) {
  //   cout << s << ' ';
  // }
  // cout << '\n';

  int idx_middle = floor(missingScores.size() / 2);

  cout << "[PART 2] Middle score: " << missingScores[idx_middle] << '\n';

  return 0;
}
