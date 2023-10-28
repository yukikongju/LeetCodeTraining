#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <math.h>

using namespace std;

struct Move {
    char direction;
    int step;

    Move(char direction, int step) : direction(direction), step(step) {}

    pair<int,int> getDxDy() {
	pair<int, int> deltas(0,0);
	if (direction == 'R') deltas.second = step;
	if (direction == 'L') deltas.second = -step;
	if (direction == 'U') deltas.first = -step;
	if (direction == 'D') deltas.first = step;

	return deltas;
    }

};

struct Position {
    int x,y;

    Position(int x, int y): x(x), y(y) {}

    bool operator<(const Position & other) const {
	if (x != other.x) {
	    return x < other.x;
	}
	return y < other.y;
    }
};

void updateTailPosition(Position &tail, Position &head) {
    // double distance = sqrt(pow(head.x - tail.x, 2) + pow(head.y - tail.y, 2));
    int dx = head.x - tail.x;
    int dy = head.y - tail.y;
    if ((abs(dx)>1) || (abs(dy)>1)) {
	int x = (dx == 0) ? 0 : dx / abs(dx);
	int y = (dy == 0) ? 0 : dy / abs(dy);
	tail.x += x;
	tail.y += y;
    }
}


void updateHeadTailPosition(Position &head, Position &tail, Move move, set<Position> &positions) {
    if (move.direction == 'R') {
	while (move.step > 0) {
	    ++head.y;
	    updateTailPosition(tail, head);
	    positions.insert(tail);
	    --move.step;
	}
    } else if (move.direction == 'L') {
	while (move.step > 0) {
	    --head.y;
	    updateTailPosition(tail, head);
	    positions.insert(tail);
	    --move.step;
	}
    } else if (move.direction == 'U') {
	while (move.step > 0) {
	    --head.x;
	    updateTailPosition(tail, head);
	    positions.insert(tail);
	    --move.step;
	}
    } else if (move.direction == 'D') {
	while (move.step > 0) {
	    ++head.x;
	    updateTailPosition(tail, head);
	    positions.insert(tail);
	    --move.step;
	}
    }
}


int getNumberVisitedPositions(vector<Move> &moves) {

    // 1. get all tail positions
    // set<pair<int,int>> positions;
    set<Position> positions;
    // pair<int, int> head(0,0), tail(0,0);
    Position head(0,0), tail(0,0);
    for (auto &move: moves) {
	// get dx, dy
	// pair<int, int> deltas = move.getDxDy();
	// cout << move.direction << " " << move.step << " dx: " << deltas.first << " dy: " << deltas.second << '\n';

	// update head and tail new positions
	updateHeadTailPosition(head, tail, move, positions);

    }

    int numMoves = positions.size();
    return numMoves;
}



int main() {
    // 1. read inputs
    string FILENAME = "inputs/2.in";
    ifstream file(FILENAME);
    char direction;
    int step;

    vector<Move> moves;

    while(file >> direction >> step) {
	Move move(direction, step);
	moves.push_back(move);
    }

    // 2. [ PART 1 - Find number of positions T has visited]
    int numTailPosition = getNumberVisitedPositions(moves);
    cout << "[ PART 1 ] Number of Visited Positions: " << numTailPosition << '\n';


    // 3. [ PART 2 - ]



    return 0;
}
