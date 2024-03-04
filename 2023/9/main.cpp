#include <bits/stdc++.h>

using namespace std;

struct skillLevels {
    int skillLevel = -51;
    int playerCount;
    int pIndexes[50];
};

int main() {
    string inputLine;
    int players = 0;
    int playersOnField = 0;
    map<int, int> jNumtoIdx;
    vector<skillLevels> adjustments;
    while (getline(cin, inputLine)) {
        if (!players) {
            players = stoi(inputLine);
        } else if (!playersOnField) {
            playersOnField = stoi(inputLine);
        } else if (jNumtoIdx.size() < players) {
            jNumtoIdx[stoi(inputLine.substr(0, 2))] = int(jNumtoIdx.size());
        } else {
            string value;
            stringstream ss(inputLine);
            int playerCount = -1;
            skillLevels currentLine{};
            while (getline(ss, value, ' ')) {
                if (currentLine.skillLevel == -51) {
                    currentLine.skillLevel = stoi(value);
                } else if (playerCount == -1) {
                    currentLine.playerCount = stoi(value);
                    playerCount = stoi(value);
                } else {
                    currentLine.pIndexes[playerCount - 1] = jNumtoIdx[stoi(value)];
                    playerCount--;
                }
            }
            adjustments.push_back(currentLine);
        }
    }
    cout << "total players: " << players << ", players allowed on the field: " << playersOnField << ", adjustments: " << endl;
    for (const skillLevels& sk: adjustments) {
        cout << "players ";
        for (int i = 0; i < sk.playerCount; i++) {
            cout << sk.pIndexes[i] << " ";
        }
        cout << "have a combined skill level of " << sk.skillLevel << "." << endl;
    }
    // TODO: Dynamic programming approach possibly?
}
