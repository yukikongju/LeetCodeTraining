#include <functional>
#include <iostream>
#include <fstream>
#include <ostream>
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

    // [ PART 1 - Find elf with maximum calories ]
    auto maxCalories = max_element(calories.begin(), calories.end());
    // 3. find max calories
    if (maxCalories != calories.end()) {
	cout << "The elf with the most calories has " << *maxCalories << '\n';
    }

    // [ PART 2 - Find total calories for top 3 elves ]
    sort(calories.begin(), calories.end(), greater<int>());
    const int NUM_TOP = 3;
    int topCalories = 0;
    for (int i=0; i<NUM_TOP; ++i) topCalories += calories[i];

    cout << "Total Calories for the top " << NUM_TOP << " elves is " << topCalories << '\n';

    return 0;
}

