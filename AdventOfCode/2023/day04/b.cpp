#include <bits/stdc++.h>
#include <cstddef>
#include <iterator>
#include <numeric>
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

  // [ PART 2 - compute number of scratch cards]
  // init cards count
  map<int, int> cardsCounts;
  for (int i = 0; i < cards.size(); i++)
    cardsCounts.insert({i, 1});
  // cardsCounts[0] = 1;

  // for (auto &v : cardsCounts)
  //   cout << v.second << ' ';
  // cout << '\n';

  for (int i = 0; i < cards.size(); i++) {
    // count number of matches
    int numMatches = 0;
    set<int> numbersSet(cards[i].numbers.begin(), cards[i].numbers.end());
    for (auto &wnum : cards[i].winningNumbers) {
      if (numbersSet.find(wnum) != numbersSet.end())
        numMatches += 1;
    }

    // add number of scratches
    for (int k = 1; k <= numMatches; k++) {
      if (i + k < cards.size())
        cardsCounts[i + k] += cardsCounts[i];
    }

    // for (auto &v : cardsCounts)
    //   cout << v.second << ' ';
    // cout << '\n';
  }

  // count total of scratches
  int numScratchCards =
      accumulate(begin(cardsCounts), end(cardsCounts), 0,
                 [](int value, const map<int, int>::value_type &p) {
                   return value + p.second;
                 });

  cout << "[ PART 2 ] Num of Scratch Cards: " << numScratchCards << '\n';

  return 0;
}
