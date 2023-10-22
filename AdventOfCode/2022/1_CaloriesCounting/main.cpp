#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main() {

    // 1. read inputs
    // const string FILE_NAME = "calories.txt";
    const string FILE_NAME = "calories_2.txt";
    ifstream file(FILE_NAME);

    // 2. compute number of calories for each elf
    string line;
    vector<int> calories;
    int current = 0;
    while(getline(file, line)) {
	if (!line.empty()) {
	    int calorie = stoi(line);
	    current += calorie;
	} else {
	    calories.push_back(current);
	    current = 0;
	}

    }

    file.close();

    auto maxCalories = max_element(calories.begin(), calories.end());
    // 3. find max calories
    if (maxCalories != calories.end()) {
	cout << *maxCalories << endl;
    }


    return 0;
}

