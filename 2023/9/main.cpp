#include <bits/stdc++.h>

using namespace std;

void combo(int p, int c, int** comboList, int size, int posY, const int &sizeMax) {
    /* This is the python way of doing this.
     * I have this here because I could just use itertools.combinations, but I made this as other languages don't have
     * said function.
    def combo(p, c, current=None):
        if not current:
            return combo(p, c, list(map(lambda x: [x], range(p))))
        if len(current[0]) == c:
            return current
        new = []
        for old in current:
            for i in range(old[-1], p):
                if i not in old:
                    new.append(old + [i])
        return combo(p, c, new)
     */
    if (comboList[0][0] == -1) {
        for (int i = 0; i < p; i++) {
            comboList[i][0] = i;
        }
        return combo(p, c, comboList, p, 1, sizeMax);
    } else if (posY == c) {
        return;
    } else {
        int comboNew[sizeMax][c];
        int cnIdx = 0;
        for (int i = 0; i < size; i++) {
            for (int j = comboList[i][posY - 1]; j < p; j++) {
                bool found = false;
                for (int k = 0; k < posY; k++) {
                    if (comboList[i][k] == j) {
                        found = true;
                    }
                }
                if (!found) {
                    for (int k = 0; k < posY; k++) {
                        comboNew[cnIdx][k] = comboList[i][k];
                    }
                    comboNew[cnIdx][posY] = j;
                    cnIdx++;
                }
            }
        }
        for (int i = 0; i < cnIdx; i++) {
            for (int j = 0; j < posY + 1; j++) {
                comboList[i][j] = comboNew[i][j];
            }
        }
        combo(p, c, comboList, cnIdx, posY + 1, sizeMax);
    }
}

int amountInCommon(const int* first, const int* second, int size) {
    int count = size;
    for (int i = 0; i < size; i++) {
        bool inFirst = false;
        for (int j = 0; j < size; j++) {
            if (second[i] == first[j]) {
                inFirst = true;
                break;
            }
        }
        if (!inFirst) {
            count++;
        }
    }
    return count;
}

int main() {
    string nextLine;
    getline(cin, nextLine);
    int totalP = stoi(nextLine);  // P
    getline(cin, nextLine);
    int fieldP = stoi(nextLine);  // F
    int jerseyNums[totalP];
    for (int i = 0; i < totalP; i++) {
        getline(cin, nextLine);
        jerseyNums[i] = stoi(nextLine.substr(0, 2));
    }
    int skillLevel[50];
    int skillPlayerCount[50];
    int skillPlayers[50][fieldP];
    int skillCount = 0;
    while (getline(cin, nextLine)) {
        stringstream ss(nextLine);
        vector<int> line(istream_iterator<int>(ss), {});
        skillLevel[skillCount] = line[0];
        skillPlayerCount[skillCount] = line[1];
        // Convert the next 'line[1]' jersey numbers to their index in jerseryNums. This makes it so later on when I
        // check for the skill levels I can use 0 to P - 1 and this allows me to simplify the combo function.
        for (int i = 0; i < line[1]; i++) {
            for (int j = 0; j < totalP; j++) {
                if (jerseyNums[j] == line[i + 2]) {
                    skillPlayers[skillCount][i] = j;
                }
            }
        }
        skillCount++;
    }

    // tgamma(n + 1) is equivalent to n factorial.
    // comboSize is the largest amount of combinations it can potentially grow to in the combo function, which is
    // basically half of P, so for example in P / (F! * (P - F)!) we are trying to get F and P - F to be as close as
    // possible, and we can just use half to get there.
    int comboSize = int(tgamma(totalP + 1) / (tgamma(totalP - (totalP / 2) + 1) * tgamma((totalP / 2) + 1)));

    // comobCount is the actual amount of combos we will actually be left with, I am not great with math and because F
    // is always > P / 2, the combo function always needs more space than the true amount of combos in the end.
    int comboCount = int(tgamma(totalP + 1) / (tgamma(fieldP + 1) * tgamma(totalP - fieldP + 1)));

    // We set everything to -1 so in the combo function we can check our progress, though after finishing this I'm
    // looking back and maybe this isn't needed? IDK, ill have to revist sometime.
    int** combinations = new int*[comboSize];
    for (int i = 0; i < comboSize; i++) {
        combinations[i] = new int[fieldP];
        for (int j = 0; j < fieldP; j++) {
            combinations[i][j] = -1;
        }
    }
    // Now we actually populate the combinations array with all possible combinations of P choose F.
    combo(totalP, fieldP, combinations, 0, 0, comboSize);

    // eligible is an array of pairs of combinations that can actually happen in a game, in order for a pair to be able
    // to actually happen it needs to have all P players in the union of the first and second combination.
    int eligibleCount = 0;
    int eligible[(comboCount * (comboCount - 1)) / 2][2 * fieldP];
    for (int i = 0; i < comboCount; i++) {
        for (int j = i + 1; j < comboCount; j++) {
            int amount = amountInCommon(combinations[i], combinations[j], fieldP);
            if (amount == totalP) {
                for (int k = 0; k < fieldP; k++) {
                    eligible[eligibleCount][k] = combinations[i][k];
                    eligible[eligibleCount][k + fieldP] = combinations[j][k];
                }
                eligibleCount++;
            }
        }
    }
    delete [] combinations;

    // Now that we have all possible pairs of combinations that is allowed to happen, we can calculate the skill level
    // of each pair and find the max of all the pairs.
    int skillMax = 0;
    for (int i = 0; i < eligibleCount; i++) {
        int p1Skill = 0;
        int p2Skill = 0;
        for (int j = 0; j < skillCount; j++) {
            int jointSkillLevel = skillLevel[j];
            int p1MatchCount = 0;
            int p2MatchCount = 0;
            int playersInJoint = skillPlayerCount[j];
            for (int k = 0; k < playersInJoint; k++) {
                for (int l = 0; l < fieldP; l++) {
                    if (eligible[i][l] == skillPlayers[j][k]) {
                        p1MatchCount++;
                    }
                    if (eligible[i][l + fieldP] == skillPlayers[j][k]) {
                        p2MatchCount++;
                    }
                }
            }
            if (p1MatchCount == playersInJoint) {
                p1Skill += jointSkillLevel;
            }
            if (p2MatchCount == playersInJoint) {
                p2Skill += jointSkillLevel;
            }
        }
        if (p1Skill + p2Skill > skillMax) {
            skillMax = p1Skill + p2Skill;
        }
    }

    // Finally double the answer because we play 4 quarters and not 2.
    cout << skillMax * 2 << endl;
}
