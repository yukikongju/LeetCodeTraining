#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;


struct Elf {
    int start, end;
};



template <typename T>
vector<T> splitString(string s, char delimiter) {
    stringstream ss(s);
    string word;
    T t;
    vector<T> results;
    while(!ss.eof()) {
	getline(ss, word, delimiter);
	istringstream tmp(word);
	tmp >> t >> ws;
	results.push_back(t);
    }
    return results;
}


int main() {
    // 1. read inputs
    // string FILENAME = "camp.txt";
    string FILENAME = "camp2.txt";
    ifstream file(FILENAME);
    string line;
    vector<pair<Elf,Elf>> pairings;

    while(getline(file, line)) {
	vector<string> intervals = splitString<string>(line, ',');
	vector<int> interval1 = splitString<int>(intervals[0], '-');
	vector<int> interval2 = splitString<int>(intervals[1], '-');

	Elf elf1 = {interval1[0], interval1[1]};
	Elf elf2 = {interval2[0], interval2[1]};
	pairings.push_back(make_pair(elf1, elf2));
    }

    // 2. [ PART 1 - Count intervals within the other ]
    int counts = 0;
    for (auto &p: pairings) {
	Elf &elf1 = p.first;
	Elf &elf2 = p.second;

	if ((elf1.start <= elf2.start && elf2.end <= elf1.end) || 
		(elf2.start <= elf1.start && elf1.end <= elf2.end)) counts++;
    }

    cout << "[ PARTIE 1 ] Total: " << counts << '\n';


    return 0;
}
