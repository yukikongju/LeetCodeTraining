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

// unordered_map<char, int> cardValuesDict = {
//     {'2', 2}, {'3', 3},  {'4', 4},  {'5', 5},  {'6', 6},  {'7', 7}, {'8', 8},
//     {'9', 9}, {'T', 10}, {'J', 11}, {'Q', 12}, {'K', 13}, {'A', 14}};
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

  bool operator<(const Hand &other) const {
    for (int i = 5; i >= 1; i--) {
      auto it1 = cardsValuesDict.find(i);
      auto it2 = other.cardsValuesDict.find(i);

      // If the current hand has a higher card count, it is greater
      if (it1 != cardsValuesDict.end() && it2 == other.cardsValuesDict.end()) {
        return false;
      } else if (it1 == cardsValuesDict.end() &&
                 it2 != other.cardsValuesDict.end()) {
        return true;
      } else if (it1 != cardsValuesDict.end() &&
                 it2 != other.cardsValuesDict.end()) {
        // Compare the card values in descending order
        for (char c : cardsOrderingDesc) {
          auto f1 = find(it1->second.begin(), it1->second.end(), c);
          auto f2 = find(it2->second.begin(), it2->second.end(), c);
          if (f1 != it1->second.end() && f2 == it2->second.end()) {
            return false;
          } else if (f1 == it1->second.end() && f2 != it2->second.end()) {
            return true;
          }
        }
      }
    }

    // If all the above comparisons are equal, the hands are considered equal
    return false;
  }
};

// bool compareHandByCards(Hand &hand1, Hand &hand2) { // TODO
//   for (int i = 5; i >= 1; i--) {
//     auto it1 = hand1.cardsvaluesdict.find(i);
//     auto it2 = hand2.cardsvaluesdict.find(i);
//     if ((it1 != hand1.cardsvaluesdict.end()) &&
//         (it2 == hand2.cardsvaluesdict.end())) {
//       return true;
//     } else if ((it1 != hand1.cardsvaluesdict.end()) &&
//                (it2 == hand2.cardsvaluesdict.end())) {
//       return false;
//     } else {
//       for (char c : cardsorderingdesc) {
//         auto f1 = find(hand1.cardsvaluesdict[i].begin(),
//                        hand1.cardsvaluesdict[i].end(), c);
//         auto f2 = find(hand2.cardsvaluesdict[i].begin(),
//                        hand2.cardsvaluesdict[i].end(), c);
//         if ((f1 != hand1.cardsvaluesdict[i].end()) &&
//             (f2 == hand2.cardsvaluesdict[i].end())) {
//           return true;
//         } else if ((f1 == hand1.cardsvaluesdict[i].end()) &&
//                    (f2 != hand2.cardsvaluesdict[i].end())) {
//           return false;
//         }
//       }
//     }
//   }

//   return true;
// }

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
  cout << "After sorting \n";
  for (auto &hand : hands) {
    hand.print();
  }

  return 0;
}
