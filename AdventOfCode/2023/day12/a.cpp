#include <fstream>
#include <ios>
#include <iostream>
#include <sstream>
#include <string>
#include <string_view>
#include <vector>

using namespace std;

struct Spring {
  string arrangement;
  vector<int> groupings;

  void print() {
    cout << "Arragement: " << arrangement << "; Groupings: ";
    for (const int g : groupings) {
      cout << g << " ";
    }
    cout << "\n";
  }
};

Spring parse_spring(const string &line) {
  Spring spring;
  string groupings_str;

  // if we use string_view instead, but defeats purpose of string_view
  // istringstream ss(string(line), ios_base::in);
  istringstream ss(line);
  ss >> spring.arrangement >> groupings_str;

  // process groupings string
  istringstream gss(groupings_str);
  string token;
  while (getline(gss, token, ',')) {
    spring.groupings.push_back(stoi(token));
  }

  return spring;
}

bool isValidCandidate(string &candidate, vector<int> &grouping) {
  // 1. calculate groupings of '#' in candidate
  vector<int> candidateGrouping;
  int groupingLength = 0;
  for (char c : candidate) {
    if (c == '#') {
      groupingLength++;
    } else if (c == '.' && groupingLength > 0) {
      candidateGrouping.push_back(groupingLength);
      groupingLength = 0;
    }
  }
  if (groupingLength > 0) {
    candidateGrouping.push_back(groupingLength);
  }

  // 2. compare candidate grouping vs arrangements
  if (candidateGrouping.size() != grouping.size()) {
    return false;
  }

  // compare value 1 by 1
  int n = candidateGrouping.size();
  for (int i = 0; i < n; i++) {
    if (candidateGrouping[i] != grouping[i]) {
      return false;
    }
  }

  return true;
}

void genererateCandidateHelper(const string &arrangement, size_t k,
                               string candidate, vector<string> &candidates) {
  // check candidate has been generated
  if (k == arrangement.size()) {
    candidates.push_back(candidate);
    return;
  }

  // generate k+1 steps
  if (arrangement[k] == '?') {
    genererateCandidateHelper(arrangement, k + 1, candidate + '#', candidates);
    genererateCandidateHelper(arrangement, k + 1, candidate + '.', candidates);

  } else {
    genererateCandidateHelper(arrangement, k + 1, candidate + arrangement[k],
                              candidates);
  }
}

vector<string> generateCandidates(string &arrangement) {
  // generating candidates using backtracking strategy
  vector<string> candidates;
  genererateCandidateHelper(arrangement, 0, "", candidates);

  return candidates;
}

int getNumArrangement(Spring &spring) {
  // Brute-Force solution: O(2^n), where n is the number of '?'
  // (1) generate a candidate by replacing '?' by # or .
  // (2) verify if candidate is valid

  int numArrangements = 0;

  vector<string> candidates = generateCandidates(spring.arrangement);
  for (string candidate : candidates) {
    if (isValidCandidate(candidate, spring.groupings)) {
      numArrangements++;
    }
  }

  return numArrangements;
}

int main() {
  // 1. Read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;

  vector<Spring> springs;
  while (getline(file, line)) {
    springs.push_back(parse_spring(line));
  }

  // printing
  // for (auto &s : springs) {
  //   s.print();
  // }

  // 2.
  long long sumArrangements = 0;
  for (auto &spring : springs) {
    sumArrangements += getNumArrangement(spring);
  }

  cout << "Sum Arrangements: " << sumArrangements << "\n";

  return 0;
}
