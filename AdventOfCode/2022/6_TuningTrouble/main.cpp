#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
// #include <unordered_map>
// #include <map>

using namespace std;

int getMarkerPosition(string &sequence, int seqLength){
    int position = 0;
    for (int i=0; i<sequence.size()-seqLength; ++i) {
	set<char> currentSet;
	for (int j=0; j<seqLength; ++j) currentSet.insert(sequence[i+j]);
	if (currentSet.size() == seqLength) {
	    position = i+seqLength;
	    break;
	}
    }
    return position;
}


int main() {
    // 1. read inputs
    string FILENAME = "inputs/6.in";
    ifstream file(FILENAME);
    string sequence;
    getline(file, sequence);

    cout << sequence << '\n';

    // 2. [ PART 1 - Get Marker ]

    // init dict counts for first three char
    int markerPosition = getMarkerPosition(sequence, 4);

    cout << "[ Part 1 ] Marker Position: " << markerPosition << '\n';

    // 3. [ PART 2 - ]

    int messagePosition = getMarkerPosition(sequence, 14);
    cout << "[ Part 2 ] Message Position: " << messagePosition << '\n';


    return 0;
}

