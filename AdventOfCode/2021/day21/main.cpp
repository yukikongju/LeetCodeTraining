#include <bits/stdc++.h>
#include <bits/types/FILE.h>
#include <string>

using namespace std;

struct Player {
  int position, score;

  Player(int position) : position(position), score(0) {}

  bool hasWon() { return score >= 1000; }
  void addScore(int s) { score += s; }
  void updatePosition(int numStepsForward) {
    position = ((position + numStepsForward) % 10 == 0)
                   ? 10
                   : ((position + numStepsForward) % 10);
  }

  void print() {
    cout << "position: " << position << "; score: " << score << '\n';
  }
};

int getNumberOfStepsForward(int &currentSum) {
  int numStepsForward = currentSum++;
  if (currentSum > 100)
    currentSum = 1;
  numStepsForward += currentSum++;
  if (currentSum > 100)
    currentSum = 1;
  numStepsForward += currentSum++;
  if (currentSum > 100)
    currentSum = 1;
  return numStepsForward;
}

int main() {
  // read inputs
  string FILENAME = "inputs/2.txt";
  ifstream file(FILENAME);
  string line;

  //
  getline(file, line);
  int pos1 = stoi(line.substr(line.find(':') + 2));
  getline(file, line);
  int pos2 = stoi(line.substr(line.find(':') + 2));
  file.close();

  cout << pos1 << ' ' << pos2 << '\n';

  // [ PART 1 ]
  int numTurns = 0;
  int currentSum = 1;
  Player player1 = Player(pos1);
  Player player2 = Player(pos2);
  bool hasWinner = false;
  bool isPlayer1Turn = true;
  while (!hasWinner) {
    numTurns += 1;
    int numStepsForward = getNumberOfStepsForward(currentSum);
    if (isPlayer1Turn) {
      player1.updatePosition(numStepsForward);
      player1.addScore(player1.position);
      if (player1.hasWon())
        hasWinner = true;
      isPlayer1Turn = false;
      cout << numTurns << " Player 1: ";
      player1.print();
    } else {
      player2.updatePosition(numStepsForward);
      player2.addScore(player2.position);
      if (player2.hasWon())
        hasWinner = true;
      isPlayer1Turn = true;
      cout << numTurns << " Player 2: ";
      player2.print();
    }
  }

  //
  int score1 = (isPlayer1Turn) ? player1.score * (numTurns * 3)
                               : player2.score * (numTurns * 3);
  cout << "[PART 1] Score: " << score1 << '\n';

  // [ PART 2 ]

  return 0;
}
