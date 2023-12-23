#include <bits/stdc++.h>
#include <cstddef>
#include <sstream>

using namespace std;

struct Card {
  vector<int> winningNumbers, numbers;
};

int main() {
  // 1. read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;
  vector<Card> cards;
  while (getline(file, line)) {
    size_t pos = line.find(':');
    stringstream ss(line.substr(pos + 2));
    Card card;

    // read winningNumbers
    string winningNumberPart;
    getline(ss, winningNumberPart, '|');
    istringstream winningNumbersStream(winningNumberPart);
    int winningNumber;
    while (winningNumbersStream >> winningNumber)
      card.winningNumbers.push_back(winningNumber);

    // read numbers
    string numberPart;
    getline(ss, numberPart);
    istringstream numbersStream(numberPart);
    int number;
    while (numbersStream >> number)
      card.numbers.push_back(number);

    // add card
    cards.push_back(card);
  }

  // print
  // for (auto &c : cards) {
  //   for (auto &wnum : c.winningNumbers)
  //     cout << wnum << ' ';
  //   cout << '\n';
  //   for (auto &num : c.numbers)
  //     cout << num << ' ';
  //   cout << '\n';
  // }

  // [ PART 1 - compute ]
  int points = 0;
  for (auto &c : cards) {
    // count number of matches
    int numMatches = 0;
    set<int> numberSet(c.numbers.begin(), c.numbers.end());
    for (auto &wnum : c.winningNumbers) {
      if (numberSet.find(wnum) != numberSet.end())
        numMatches += 1;
    }
    cout << numMatches << '\n';

    // add points to total
    points += (numMatches > 0 ? 1 << (numMatches - 1) : 0);
  }

  cout << "[ PART 1 ] Num Points: " << points << '\n';

  return 0;
}
