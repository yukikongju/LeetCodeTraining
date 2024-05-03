#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map<char, int> cardValuesDict = {
    {'2', 2}, {'3', 3},  {'4', 4},  {'5', 5},  {'6', 6},  {'7', 7}, {'8', 8},
    {'9', 9}, {'T', 10}, {'J', 11}, {'Q', 12}, {'K', 13}, {'A', 14}};

struct Hand {
  string cards;
  int bid;
  unordered_map<int, vector<char>> cardsValues;

  void setCardValues() {
    // count each type of cards
    unordered_map<char, int> counts;
    for (char &c : cards) {
      ++counts[c];
    }

    // get ordered dict for each cards
    for (const auto &pair : cardValuesDict) {

      if (counts[pair.first] > 0) {
        cardsValues[counts[pair.first]].push_back(pair.first);
      }
    }
  }

  void print() {
    cout << "Cards: " << cards << ' ' << "; Bid: " << bid;
    cout << "; Values => ";
    for (const auto &pair : cardsValues) {
      cout << pair.first << ": ";
      for (char c : pair.second)
        cout << c;
      cout << "; ";
    }
    cout << "\n";
  }
};

bool compareHandByCards(Hand &hand1, Hand &hand2) { // TODO
  // compute value hand 1

  // compute value hand 2

  // compare them

  return true;
}

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

  return 0;
}
