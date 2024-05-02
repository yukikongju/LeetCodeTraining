#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Hand {
  string cards;
  // array<int, 5> cardsValues; // each position is the value of the "kind" we
  // have
  int bid;
};

void updateCardValue(Hand &hand) { // TODO
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

    // compute cards value
    updateCardValue(hand);

    hands.push_back(hand);
  }

  // print hand
  for (const auto &hand : hands) {
    cout << "Cards: " << hand.cards << ' ' << "; Bid: " << hand.bid << "\n";
  }

  // 2. Implement sorting algorithm to rank hands

  return 0;
}
