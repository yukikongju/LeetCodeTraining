#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

const vector<char> cardsOrderingDesc = {'A', 'K', 'Q', 'J', 'T', '9', '8',
                                        '7', '6', '5', '4', '3', '2'};

struct Hand {
  string cards;
  int bid;
  unordered_map<int, vector<char>> cardsValuesDict;

  void setCardValues() {
    // count each type of cards
    unordered_map<char, int> counts;
    for (char &c : cards) {
      ++counts[c];
    }

    // get ordered dict for each cards
    for (char c : cardsOrderingDesc) {

      if (counts[c] > 0) {
        cardsValuesDict[counts[c]].push_back(c);
      }
    }
  }

  void print() {
    cout << "Cards: " << cards << ' ' << "; Bid: " << bid;
    cout << "; Values => ";
    for (const auto &pair : cardsValuesDict) {
      cout << pair.first << ": ";
      for (char c : pair.second)
        cout << c;
      cout << "; ";
    }
    cout << "\n";
  }

  string nOfAKind(const Hand &other, int i) const {
    auto it1 = cardsValuesDict.find(i);
    auto it2 = other.cardsValuesDict.find(i);

    // If the current hand has a higher card count, it is greater
    if (it1 != cardsValuesDict.end() && it2 == other.cardsValuesDict.end()) {
      return "greater";
    } else if (it1 == cardsValuesDict.end() &&
               it2 != other.cardsValuesDict.end()) {
      return "lower";
    } else if (it1 != cardsValuesDict.end() &&
               it2 != other.cardsValuesDict.end()) {
      // Compare the card values in descending order
      for (char c : cardsOrderingDesc) {
        auto f1 = find(it1->second.begin(), it1->second.end(), c);
        auto f2 = find(it2->second.begin(), it2->second.end(), c);
        if (f1 != it1->second.end() && f2 == it2->second.end()) {
          return "greater";
        } else if (f1 == it1->second.end() && f2 != it2->second.end()) {
          return "lower";
        }
      }
    }

    return "continue";
  }

  bool operator<(const Hand &other) const {
    string hasFiveOfAKind = nOfAKind(other, 5);
    if (hasFiveOfAKind == "lower") {
      return true;
    } else if (hasFiveOfAKind == "greater") {
      return false;
    }
    string hasFourOfAKind = nOfAKind(other, 4);
    if (hasFourOfAKind == "lower") {
      return true;
    } else if (hasFourOfAKind == "greater") {
      return false;
    }

    // TODO: full house

    string hasThreeOfAKind = nOfAKind(other, 3);
    if (hasThreeOfAKind == "lower") {
      return true;
    } else if (hasThreeOfAKind == "greater") {
      return false;
    }

    // TODO: two pairs
    string hasOnePair = nOfAKind(other, 2);
    if (hasOnePair == "lower") {
      return true;
    } else if (hasOnePair == "greater") {
      return false;
    }

    string hasHighCard = nOfAKind(other, 1);
    if (hasHighCard == "lower") {
      return true;
    } else if (hasHighCard == "greater") {
      return false;
    }

    // If all the above comparisons are equal, the hands are considered equal
    return false;
  }
};

int main() {
  // 1. read inputs
  string FILENAME = "inputs/1.txt";
  ifstream file(FILENAME);
  string line;

  vector<Hand> hands;
  while (getline(file, line)) {

    // get (1) cards (2) bid
    istringstream iss(line);
    Hand hand;
    iss >> hand.cards >> hand.bid;
    hand.setCardValues();

    hands.push_back(hand);
  }

  // print hand
  for (auto &hand : hands) {
    hand.print();
  }

  // 2. Implement sorting algorithm to rank hands
  sort(hands.begin(), hands.end());
  cout << "\nAfter sorting \n";
  for (auto &hand : hands) {
    hand.print();
  }

  // 3. Compute total winnings
  int rank = 1;
  int totalWinnings = 0;
  for (auto hand : hands) {
    totalWinnings += hand.bid * rank;
    rank++;
  }
  cout << "Total Winnings: " << totalWinnings << "\n";

  return 0;
}
