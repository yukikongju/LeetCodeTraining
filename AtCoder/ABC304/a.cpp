#include <bits/stdc++.h>
#include <utility>
#include <vector>
using namespace std;

int main() {
    // 1. read inputs
    int N; 
    cin >> N;
    vector<pair<string, int>> people(N);
    for(int i=0; i<N; ++i) {
	pair<string, int> person;
	cin >> person.first >> person.second;
	people[i] = person;
    }

    // for (auto &person : people) {
    //     cout << person.first << " " << person.second << endl;
    // }

    // 2. find youngest person
    int idx_youngest = 0;
    for (int i=0; i < people.size(); ++i) {
	if (people[i].second < people[idx_youngest].second) idx_youngest = i;
    }

    // 3. print
    for (int i=idx_youngest; i < people.size(); ++i) {
	cout << people[i].first << endl;
    }
    for (int i=0; i < idx_youngest; ++i) {
	cout << people[i].first << endl;
    }

    return 0;
}
