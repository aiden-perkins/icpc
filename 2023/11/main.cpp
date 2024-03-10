#include <bits/stdc++.h>

using namespace std;

int main() {
    cout << fixed;
    cout << setprecision(6);
    string inputLine;
    getline(cin, inputLine);
    int playerCount = stoi(inputLine);
    int scores[playerCount][playerCount];
    for (int i = 0; i < playerCount; i++) {
        getline(cin, inputLine);
        stringstream ss(inputLine);
        vector<int> line(istream_iterator<int>(ss), {});
        for (int j = 0; j < playerCount; j++) {
            scores[i][j] = line[j];
        }
    }

    // First round is calculated a little differently.
    double total = 0;
    for (int i = 0; i < playerCount; i++) {
        for (int j = i; j < playerCount; j++) {
            total += scores[i][j];
        }
    }
    total = total / ((double(playerCount * (playerCount - 1)) / 2) / (double(playerCount) / 2));

    // Find out how large our numerator table needs to be.
    int tournamentRounds = int(log2(playerCount));
    int numeratorTableX = 2;
    for (int i = 1; i < tournamentRounds; i++) {
        numeratorTableX += (((i - 1) * i) / 2) + 1;
    }
    
    // Fill out the numerator table.
    int numeratorTable[numeratorTableX][playerCount];
    for (int i = 0; i < numeratorTableX; i++) {
        for (int j = 0; j < playerCount; j++) {
            if (!j || !i) {
                numeratorTable[i][j] = 1;
            } else {
                numeratorTable[i][j] = numeratorTable[i - 1][j] + numeratorTable[i][j - 1];
            }
        }
    }

    // Fill out the probability table.
    int posX = 0;
    double probTable[tournamentRounds][playerCount];
    for (int i = 0; i < tournamentRounds; i++) {
        int playersLeft = playerCount - (int(pow(2, i)) - 1);
        int denominator = numeratorTable[posX][playersLeft - 1];
        for (int j = 0; j < playersLeft; j++) {
            if (j < playersLeft) {
                int numerator = numeratorTable[posX][playersLeft - j - 1];
                probTable[i][j] = (double(numerator) / denominator);
                if (i) {
                    probTable[i][j] *= probTable[i - 1][j];
                }
            } else {
                probTable[i][j] = 0;
            }
        }
        posX += ((i * (i - 1)) / 2) + 1;
    }

    /*  This is just to make sure the probabilities are correct.
    for (int i = 0; i < tournamentRounds; i++) {
        for (int j = 0; j < playerCount; j++) {
            cout << probTable[i][j] << " ";
        }
        cout << endl;
    }
    */

    // Go through each possible pair in each round and add that to the total.
    for (int i = 1; i < tournamentRounds; i++) {
        int playersLeft = playerCount - (int(pow(2, i)) - 1);
        int playersLost = playersLeft - (playerCount - (int(pow(2, i + 1)) - 1));
        for (int j = 0; j < playersLeft - playersLost; j++) {
            double p1m = probTable[i][j];
            for (int k = j + 1; k < playersLeft; k++) {
                double p2m = probTable[i][k];
                int score = scores[j][k];
                total += score * p1m * p2m;
            }
        }
    }

    // Here we are, this is supposed to be the correct answer, but I have made a fatal mistake. I was calculating the
    // probability that a specific seed makes it to a specific round, generating all possible pairs in a specific
    // round and then multiplying each seed's probability it made it there by each other in the pair, then multiplying
    // that by the excitement score, and hoping that is how it works. This works for 1.in, because I calculate the first
    // round correctly and the last round correctly, so when there are only 2 rounds, this code works. However, with 8
    // or more, there are 3 or more rounds, thus my code is incorrect. In order to fix this I need to somehow calculate
    // the probability a specific pair happens in a specific round, which I do not know how yet. :( I have wasted 20+
    // hours on this, and I am hesitant to continue working on it again, maybe another time.
    cout << total << endl;
}
