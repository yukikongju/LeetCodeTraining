#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;


map<char, int> mapPoints = {{'X', 1}, {'Y', 2}, {'Z', 3}}; // X: Rock; X: Paper; Z: Scissors
map<char, int> mapOutcomes = {{'W', 6}, {'D', 3}, {'L', 0}}; // W: wins; D: draws; L: loss
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
    int total = 0;
    char player, opponent;
    while (getline(file, line)) {
	// cin >> player >> opponent;
	opponent = line[0];
	player = line[2];
	int pointsMove = mapPoints[player];
	char outcome = getOutcome(player, opponent);
	int pointsOutcome = mapOutcomes[outcome];

	cout << pointsMove << " " << pointsOutcome << " " << player << opponent << outcome << '\n';

	// cout << player << opponent << pointsMove << pointsOutcome << endl;

	total += pointsMove + pointsOutcome;
    }

    file.close();

    cout << endl;
    cout << "[ PART 1 ] Total Points: " << total << '\n';


    // 3. 


    // 4. 



    return 0;
}

