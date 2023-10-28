#include <functional>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    // 1. read inputs
    string FILENAME = "inputs/2.in";
    ifstream file(FILENAME);
    string line;
    vector<string> instructions;
    while(getline(file, line)) instructions.push_back(line);

    // 2. [ PART 1 ]
    vector<int> registers;
    int current=1;
    registers.push_back(current);
    registers.push_back(current);
    for (auto &instruction : instructions) {
	if (!instruction.find("noop")) {
	    registers.push_back(current);
	} else { // addx
	    vector<string> tokens;
	    string value; 
	string tmp;
	    istringstream iss(instruction);
	    iss >> tmp >> value;
	registers.push_back(current);
	current += atoi(value.c_str()); // CHECK
	registers.push_back(current);
	}
    }

    // print
    for (int i=0; i<registers.size(); ++i) cout << i << " " << registers[i] << "\n";


    // compute signal strength for every 20 cycles
    int signalStrength = 0;
    vector<int> cycles = {20, 60, 100, 140, 180, 220};
    for (auto &c : cycles) signalStrength += registers[c] * c;

    cout << "[ PART 1 ] Signal Strength: " << signalStrength << '\n';


    // 3. [ PART 2 ]



    return 0;
}


