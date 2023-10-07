#include <bits/stdc++.h>
#include <iterator>
#include <stdio.h>
using namespace std;

int main() {
    // 1. read inputs
    int n, m;
    string s, t;
    cin >> n >> m;
    cin >> s;
    cin >> t;
    // cout << s << " " << t << endl;

    // 2. check if preffix or/and suffix
    bool prefix = t.substr(0, n) == s;
    bool suffix = t.substr(m-n, n) == s;
    if (prefix && suffix) cout << 0 << endl;
    else if (prefix) cout << 1 << endl;
    else if (suffix) cout << 2 << endl;
    else cout << 3 << endl;

    return 0;
}

