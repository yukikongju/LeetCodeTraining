#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
// #include <unordered_map>
// #include <map>

using namespace std;

int main() {
    // 1. read inputs
    string FILENAME = "inputs/6.in";
    ifstream file(FILENAME);
    string sequence;
    getline(file, sequence);

    cout << sequence << '\n';

    // 2. [ PART 1 - Get Marker ]

    // init dict counts for first three char
    int seqLength = 4;
    int markerPosition = 0;
    for (int i=0; i<sequence.size()-seqLength; ++i) {
	set<char> currentSet;
	for (int j=0; j<seqLength; ++j) currentSet.insert(sequence[i+j]);
	if (currentSet.size() == seqLength) {
	    markerPosition = i+4;
	    break;
	}
    }

    cout << "[ Part 1 ] Marker Position: " << markerPosition << '\n';

    // 3. [ PART 2 - ]



    return 0;
}

