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

    // 4. [ PART 2 - Find Safety Badge ]
    int total2 = 0;
    for (int i=0; i<rucksacks.size(); i+=3) {
	string elf1 = rucksacks[i];
	string elf2 = rucksacks[i+1];
	string elf3 = rucksacks[i+2];


	set<char> set1, set2, set3;
	for (char c: elf1) set1.insert(c);
	for (char c: elf2) set2.insert(c);
	for (char c: elf3) set3.insert(c);

	vector<char> vset1(set1.begin(), set1.end());
	vector<char> vset2(set2.begin(), set2.end());
	vector<char> vset3(set3.begin(), set3.end());

	sort(vset1.begin(), vset1.end(), caseSensitiveCompare);
	sort(vset2.begin(), vset2.end(), caseSensitiveCompare);
	sort(vset3.begin(), vset3.end(), caseSensitiveCompare);

	vector<char> intersection1, intersection2;
	set_intersection(vset1.begin(), vset1.end(), vset2.begin(), vset2.end(), back_inserter(intersection1));
	set_intersection(intersection1.begin(), intersection1.end(), vset3.begin(), vset3.end(), back_inserter(intersection2));

	char badge = intersection2[0];

	int pqValue = getPriorityValue(badge);

	// cout << badge << " " << pqValue << '\n';
	// cout << '\n';

	total2 += pqValue;
    }

    cout << "[ PART 2 ] Total: " << total2 << '\n';

    return 0;
}

