#include <bits/stdc++.h>

using namespace std;

int main() {
    string input;
    while (getline(cin, input)) {
        stringstream ss(input);
        string dimension;
        getline(ss, dimension, ' ');
        int m = stoi(dimension);
        getline(ss, dimension, ' ');
        int n = stoi(dimension);
        cout << (max(m, n) * (min(m, n) - 1)) + (max(m, n) - 1) << endl;
    }
}
