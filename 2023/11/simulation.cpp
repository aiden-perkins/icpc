#include <algorithm>
#include <random>
#include <ctime>
#include <map>
#include <iomanip>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    srand(time(0));
    const long int runs = stol(argv[1]);
    const int n = stoi(argv[2]);
    const int rounds = stoi(argv[3]);

    int counts[n] = {0};
    map<string, int> pairs[rounds];
    for (int k = 0; k < rounds; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                pairs[k][to_string(i) + to_string(j)] = 0;
            }
        }
    }
    int seeds[n];

    for (int i = 0; i < runs; i++) {
        for (int j = 1; j <= n; j++) {
            seeds[j - 1] = j;
        }
        random_shuffle(seeds, seeds + n);
        for (int j = 0, size = n; j < rounds; ++j, size /= 2) {
            for (int k = 0; k < size; k += 2) {
                int mn = min(seeds[k], seeds[k + 1]);
                int mx = max(seeds[k], seeds[k + 1]);
                string combined = to_string(mn) + to_string(mx);
                pairs[j][combined] += 1;
                seeds[k / 2] = mn;
            }
        }
        for (int j = 0, size = n / (1 << rounds); j < size; ++j) {
            counts[seeds[j] - 1] += 1;
        }
    }
    cout << fixed;
    cout << setprecision(10);

    for (int i = 0; i < rounds; i++) {
        cout << "round " << i + 1 << endl;
        for (auto it = pairs[i].cbegin(); it != pairs[i].cend(); it++) {
            if (it -> second) {
                int games = n / pow(2, i + 1);
                int totalGames = games * runs;
                // cout << it -> first << ": " << double(it -> second) / totalGames * 100 << endl;
                cout << double(it -> second) / totalGames * 100 << endl;
            }
        }
    }
    cout << "After " << runs << " runs, probabilities are:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << i + 1 << ": " << (static_cast<double>(counts[i]) / runs) * 100 << endl;
    }
    return 0;
}
