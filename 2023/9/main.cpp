#include <bits/stdc++.h>

using namespace std;

int main() {
    string nextLine;
    getline(cin, nextLine);
    int totalPlayers = stoi(nextLine);  // P
    getline(cin, nextLine);
    int fieldPlayers = stoi(nextLine);  // F
    int jerseyNums[totalPlayers];
    for (int i = 0; i < totalPlayers; i++) {
        getline(cin, nextLine);
        jerseyNums[i] = stoi(nextLine.substr(0, 2));
    }
    int skillLevel[50];
    int skillPlayerCount[50];
    int skillPlayers[50][fieldPlayers];
    int skillCount = 0;
    while (getline(cin, nextLine)) {
        stringstream ss(nextLine);
        vector<int> line(istream_iterator<int>(ss), {});
        skillLevel[skillCount] = line[0];
        skillPlayerCount[skillCount] = line[1];
        for (int i = 0; i < line[1]; i++) {
            skillPlayers[skillCount][i] = line[i + 2];
        }
        skillCount++;
    }
    // TODO: Dynamic programming approach possibly?
    // 4 dimensions in cache: Quarters, Players, Player Limit, Quarters Played
    int cache[4][totalPlayers + 1][fieldPlayers + 1][2];
    // Base case: Quarters or Players is 0.
    //
}
