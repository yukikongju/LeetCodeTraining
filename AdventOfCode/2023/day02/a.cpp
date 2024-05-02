#include <array>
#include <cstddef>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

using namespace std;

struct Game {
  int id;
  vector<array<int, 3>> rounds; // RBG
};

void update_color(array<int, 3> &round, string_view ball_str) {
  // find number
  size_t pos = ball_str.find(' ');
  int n = 0;
  for (const char digit : ball_str.substr(0, pos)) {
    n = n * 10 + (digit - '0');
  }

  // find color
  string_view color = ball_str.substr(pos + 1, ball_str.size() - pos - 1);

  // update color
  if (color == "red") {
    round[0] = n;
  } else if (color == "green") {
    round[1] = n;
  } else {
    round[2] = n;
  }
}

array<int, 3> parse_round(string_view round_str) {
  array<int, 3> round = {{0, 0, 0}};
  size_t start = 0;
  size_t end = round_str.find(',', start);
  // cout << round_str << "\n";
  while (end != string::npos) {
    string_view ball_str = round_str.substr(start, end - start);
    // cout << ball_str << "\n";
    update_color(round, ball_str);

    //
    start = end + 2;
    end = round_str.find(',', start);
  }
  // cout << '\n';

  string_view ball_str = round_str.substr(start, round_str.size() - start);
  // cout << ball_str << "\n";
  update_color(round, ball_str);

  return round;
}

Game parse_game(const string_view line) {
  size_t pos = line.find(':');

  // find game id
  int gameId = 0;
  for (const char digit : line.substr(5, pos - 5)) {
    gameId = gameId * 10 + (digit - '0');
  }

  // init game: (1) id (2) rounds
  Game game;
  game.id = gameId;

  size_t start = pos + 1;
  size_t end = line.find(';', start);
  while (end != string::npos) {
    string_view round_str = line.substr(start + 1, end - start - 1);
    // cout << round_str << "\n";
    game.rounds.push_back(parse_round(round_str));
    start = end + 1;
    end = line.find(';', start);
  }
  string_view round_str = line.substr(start + 1, line.size() - start - 1);
  // cout << round_str << "\n";
  game.rounds.push_back(parse_round(round_str));

  return game;
}

int main() {
  // 1. read inputs
  string FILENAME = "inputs/1.txt";
  ifstream file(FILENAME);
  string line;

  vector<Game> games;

  while (getline(file, line)) {
    games.push_back(parse_game(line));
  }

  // printing games
  for (const auto &game : games) {
    cout << game.id << "\n";
    for (const auto &round : game.rounds) {
      cout << round[0] << ' ' << round[1] << ' ' << round[2] << '\n';
    }
    cout << "---- \n";
  }

  // 2.

  return 0;
}
