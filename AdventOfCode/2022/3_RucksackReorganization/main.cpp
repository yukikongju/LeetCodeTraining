#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <math.h>

using namespace std;

bool caseSensitiveCompare(char a, char b) {
    return a < b;
}

int getPriorityValue(char c) {
    if (c >= 'a' && c <= 'z') {
	return c - 'a' + 1;
    } else if (c >= 'A' && c <= 'Z'){
	return c - 'A' + 27;
    } else {
	return 0;
    }
}

int main() {
    // 1. read inputs files
    // string FILENAME = "rucksack.txt";
    string FILENAME = "rucksack2.txt";
    ifstream file(FILENAME);

    string line;
    vector<string> rucksacks;
    while (getline(file, line)) {
	rucksacks.push_back(line);
    } 


    // 3. [ PART 1 ] find elements that occurs in both compartment + compute its priority sum
    int total = 0;
    for (auto &rucksack : rucksacks) {
	int n = floor(rucksack.size() / 2);
	// int n = ceil(rucksack.size() / 2);

	// get compartments
	string c1 = rucksack.substr(0, n);
	string c2 = rucksack.substr(n);

	// cout << c1 << " " << c2 << '\n';


	// compute compartment intersection
	sort(c1.begin(), c1.end(), caseSensitiveCompare);
	sort(c2.begin(), c2.end(), caseSensitiveCompare);

	vector<char> intersection;
	set_intersection(c1.begin(), c1.end(), c2.begin(), c2.end(), back_inserter(intersection));


	// compute priority value
	if (!intersection.empty()) {
	    char dup = intersection[0];
	    int pqValue = getPriorityValue(dup);

	    // cout << dup << " " << pqValue << '\n';


	    total += pqValue;
	} else {
	    cout << "No intersection : " << c1 << " " << c2 << " " << rucksack << '\n';
	}
    }

    cout << "[ PART 1 ] Total : " << total << '\n';


    // 4. 


    return 0;
}

