#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;


map<char, int> mapPoints = {{'X', 1}, {'Y', 2}, {'Z', 3}}; // X: Rock; X: Paper; Z: Scissors
map<char, int> mapOutcomes = {{'W', 6}, {'D', 3}, {'L', 0}}; // W: wins; D: draws; L: loss
map<char, int> mapOutcomes2 = {{'Z', 6}, {'Y', 3}, {'X', 0}}; // X: lose; Y: draws; Z: wins

struct Game {
    char playerMove, opponentMove;
};

enum OpponentMove {
    OPPONENT_ROCK = 'A',
    OPPONENT_PAPER = 'B', 
    OPPONENT_SCISSORS = 'C'
};

enum PlayerMove {
    PLAYER_ROCK = 'X', 
    PLAYER_PAPER = 'Y', 
    PLAYER_SCISSORS = 'Z'
};

enum Outcome {
    WIN = 'Z',
    DRAW = 'Y', 
    LOSS = 'X'
};

char getPlayerMove(char outcome, char opponent) { 
    if ((outcome == Outcome::WIN && opponent == OpponentMove::OPPONENT_SCISSORS) || 
	    (outcome == Outcome::DRAW && opponent == OpponentMove::OPPONENT_ROCK) || 
	    (outcome == Outcome::LOSS && opponent == OpponentMove::OPPONENT_PAPER)) {
	return PlayerMove::PLAYER_ROCK;
    } else if ((outcome == Outcome::WIN && opponent == OpponentMove::OPPONENT_PAPER) || 
	    (outcome == Outcome::DRAW && opponent == OpponentMove::OPPONENT_SCISSORS) || 
	    (outcome == Outcome::LOSS && opponent == OpponentMove::OPPONENT_ROCK)) {
	return PlayerMove::PLAYER_SCISSORS;
    } else {
	return PlayerMove::PLAYER_PAPER;
    }

}


char getOutcome(char player, char opponent) {
    if ((player == PlayerMove::PLAYER_ROCK && opponent == OpponentMove::OPPONENT_ROCK) 
	    || (player == PlayerMove::PLAYER_PAPER && opponent == OpponentMove::OPPONENT_PAPER) 
	    || (player == PlayerMove::PLAYER_SCISSORS && opponent == OpponentMove::OPPONENT_SCISSORS)) {
	return 'D';
    } else if ((player == PlayerMove::PLAYER_ROCK && opponent == OpponentMove::OPPONENT_SCISSORS) || 
	    (player == PlayerMove::PLAYER_PAPER && opponent == OpponentMove::OPPONENT_ROCK) || 
	    (player == PlayerMove::PLAYER_SCISSORS && opponent == OpponentMove::OPPONENT_PAPER)) {
	return 'W';
    } else {
	return 'L';
    }
}

int main() {
    // 1. read inputs
    // const string FILE_NAME = "game.txt";
    const string FILE_NAME = "game2.txt";
    ifstream file(FILE_NAME);

    // 2. get total points following strategy
    string line;
    int strategy1_total = 0;
    vector<Game> games;

    while (getline(file, line)) {
	Game game;
	game.playerMove = line[2];
	game.opponentMove = line[0];
	games.push_back(game);
    }

    file.close();

    for (auto &game: games) {
	int pointsMove = mapPoints[game.playerMove];
	char outcome = getOutcome(game.playerMove, game.opponentMove);
	int pointsOutcome = mapOutcomes[outcome];
	strategy1_total += pointsMove + pointsOutcome;

	// cout << pointsMove << " " << pointsOutcome << " " << game.playerMove << game.opponentMove << outcome << '\n';

    }

    cout << endl;
    cout << "[ PART 1 ] Total Points: " << strategy1_total << '\n';

    // 3. [ PART 2 - Strategy 2]
    int pointsStrategy2 = 0;
    for (auto &game: games) {
	char outcome = game.playerMove;
	int pointsOutcome = mapOutcomes2[outcome];
	char playerMove = getPlayerMove(outcome, game.opponentMove);
	int pointsMove = mapPoints[playerMove];

	cout << outcome << game.opponentMove << " " << pointsOutcome << " " << pointsMove << '\n';

	pointsStrategy2 += pointsOutcome + pointsMove;
    }

    cout << "[ PART 2 ] Total points " << pointsStrategy2 << '\n';

    // 4. 



    return 0;
}

