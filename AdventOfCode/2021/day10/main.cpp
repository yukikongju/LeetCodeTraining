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
  int syntaxScore = 0;
  for (auto &chunk : chunks) {
    stack<char> s;
    for (auto &c : chunk) {
      if (opensChars.find(c) != opensChars.end()) {
        s.push(c);
      } else {
        char top = s.top();
        s.pop();
        if (bracketsMap[c] != top) {
          syntaxScore += illegalCharactersPoints[c];
          break;
        }
      }
    }
  }

  cout << "[PART 1] Syntax Error Score: " << syntaxScore << '\n';

  return 0;
}
