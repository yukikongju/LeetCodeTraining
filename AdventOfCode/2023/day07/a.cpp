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

unordered_map<char, int> cardValuesDict = {
    {'2', 2}, {'3', 3},  {'4', 4},  {'5', 5},  {'6', 6},  {'7', 7}, {'8', 8},
    {'9', 9}, {'T', 10}, {'J', 11}, {'Q', 12}, {'K', 13}, {'A', 14}};

const vector<char> cardsOrderingDesc = {'A', 'K', 'Q', 'J', 'T', '9', '8',
                                        '7', '6', '5', '4', '3', '2'};

struct Hand {
  string cards;
  int bid;
  unordered_map<int, vector<char>> valueDict;

  void setCardValues() {
    // count each type of cards
    unordered_map<char, int> counts;
    for (char &c : cards) {
      ++counts[c];
    }

    // get ordered dict for each cards
    for (char c : cardsOrderingDesc) {

      if (counts[c] > 0) {
        valueDict[counts[c]].push_back(c);
      }
    }
  }

  void print() {
    cout << "Cards: " << cards << ' ' << "; Bid: " << bid;
    cout << "; Values => ";
    for (const auto &pair : valueDict) {
      cout << pair.first << ": ";
      for (char c : pair.second)
        cout << c;
      cout << "; ";
    }
    cout << "\n";
  }

  string nOfAKind(const Hand &other, int i) const {
    auto it1 = valueDict.find(i);
    auto it2 = other.valueDict.find(i);

    // If the current hand has a higher card count, it is greater
    if (it1 != valueDict.end() && it2 == other.valueDict.end()) {
      return "greater";
    } else if (it1 == valueDict.end() && it2 != other.valueDict.end()) {
      return "lower";
    } else if (it1 != valueDict.end() && it2 != other.valueDict.end()) {
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

  string getFullHouse(const Hand &other) const {
    // verify that both hands have 2 and 3
    auto hand1has2 = valueDict.find(2);
    auto hand2has2 = other.valueDict.find(2);
    auto hand1has3 = valueDict.find(3);
    auto hand2has3 = other.valueDict.find(3);

    if (hand1has2 == valueDict.end() || hand2has2 == other.valueDict.end() ||
        hand1has3 == valueDict.end() || hand2has3 == other.valueDict.end()) {
      return "continue";
    }

    // get greater 3, then 2; Note: if full house, then only one two + one three
    if (cardValuesDict[hand1has3->second[0]] >
        cardValuesDict[hand2has3->second[0]]) {
      return "greater";
    } else if (cardValuesDict[hand1has3->second[0]] <
               cardValuesDict[hand2has3->second[0]]) {
      return "lower";
    }

    if (cardValuesDict[hand1has2->second[0]] >
        cardValuesDict[hand2has2->second[0]]) {
      return "greater";
    } else if (cardValuesDict[hand1has2->second[0]] <
               cardValuesDict[hand2has2->second[0]]) {
      return "lower";
    }

    return "continue";
  }

  string getTwoPairs(const Hand &other) const { // TODO
    // verify that both hands have two pairs
    auto hand1hasPairs = valueDict.find(2);
    auto hand2hasPairs = other.valueDict.find(2);
    if (hand1hasPairs == valueDict.end() or
        hand2hasPairs == other.valueDict.end()) {
      return "continue";
    }

    // checking if it has two pairs
    if (hand1hasPairs->second.size() == 1 or
        hand2hasPairs->second.size() == 1) {
      return "continue";
    }

    // get greater pair 1 => pair 2 => highest card
    for (int i = 0; i < 2; i++) {
      if (cardValuesDict[hand1hasPairs->second[i]] >
          cardValuesDict[hand2hasPairs->second[i]]) {
        return "greater";
      } else if (cardValuesDict[hand1hasPairs->second[i]] <
                 cardValuesDict[hand2hasPairs->second[i]]) {
        return "lower";
      }
    }

    // compare their lowest card
    auto hand1posSingle = valueDict.find(1);
    auto hand2posSingle = other.valueDict.find(1);
    if (cardValuesDict[hand1posSingle->second[0]] >
        cardValuesDict[hand2posSingle->second[0]]) {
      return "greater";
    } else if (cardValuesDict[hand1posSingle->second[0]] <
               cardValuesDict[hand2posSingle->second[0]]) {
      return "lower";
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

    // full house
    string hasFullHouse = getFullHouse(other);
    if (hasFullHouse == "lower") {
      return true;
    } else if (hasFullHouse == "greater") {
      return false;
    }

    string hasThreeOfAKind = nOfAKind(other, 3);
    if (hasThreeOfAKind == "lower") {
      return true;
    } else if (hasThreeOfAKind == "greater") {
      return false;
    }

    // two pairs
    string hasTwoPairs = getTwoPairs(other);
    if (hasTwoPairs == "lower") {
      return true;
    } else if (hasTwoPairs == "greater") {
      return false;
    }

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
  string FILENAME = "inputs/2.txt";
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
  // for (auto &hand : hands) {
  //   hand.print();
  // }
  for (size_t i = 0; i < hands.size(); i++) {
    cout << "Rank: " << i + 1 << "; ";
    hands[i].print();
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
