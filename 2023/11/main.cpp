#include <bits/stdc++.h>

using namespace std;

long int binomial_coefficient(int top, int bottom, long int** cache) {
    if (bottom == 0 || bottom == top) {
        cache[top][bottom] = 1;
        return 1;
    }
    if (cache[top][bottom] != -1) {
        return cache[top][bottom];
    }
    if (bottom == 1) {
        cache[top][bottom] = top;
        return top;
    }
    cache[top][bottom] = binomial_coefficient(top - 1, bottom - 1, cache) +
        binomial_coefficient(top - 1, bottom, cache);
    return cache[top][bottom];
}

int main() {
    cout << fixed;
    cout << setprecision(10);
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
    auto** cache = new long int*[playerCount];
    for (int i = 0; i < playerCount; i++) {
        cache[i] = new long int[playerCount];
        for (int j = 0; j < playerCount; j++) {
            cache[i][j] = -1;
        }
    }

    long double total = 0;
    int rounds = int(log2(playerCount));
    for (int r = 1; r < rounds + 1; r++) {
        int playersLeft = playerCount - (int(pow(2, r - 1)) - 1);
        int playersMovingOn = playerCount - (int(pow(2, r)) - 1);
        double pA = pow(2, r - 1) / (pow(2, rounds) - 1);
        long int denominatorB = binomial_coefficient(int(pow(2, rounds) - 2), int(pow(2, r - 1) - 1), cache);
        long int denominatorC = binomial_coefficient(
            int(pow(2, rounds) - 1 - pow(2, r - 1)), int(pow(2, r - 1) - 1), cache
        );
        for (int i = 1; i < playersMovingOn + 1; i++) {
            long int numeratorC = binomial_coefficient(
                int(pow(2, rounds) - i - pow(2, r - 1)), int(pow(2, r - 1)) - 1, cache
            );
            for (int j = i + 1; j < playersLeft + 1; j++) {
                long int numeratorB = binomial_coefficient(int(pow(2, rounds)) - j, int(pow(2, r - 1)) - 1, cache);
                total += scores[i - 1][j - 1] * (pA * ((long double) numeratorB / denominatorB) * ((long double) numeratorC / denominatorC));
            }
        }
    }
    delete [] cache;
    // https://math.stackexchange.com/questions/4878862/fixed-single-elimination-tournament-probabilities
    // I gave up and asked this question, binomial coefficients and pascals triangle. It's funny because in my notebook
    // and in my google sheets notes page, I had made an entire pascals triangle without even realizing, and when
    // I asked some math major friends, they gave me formulas with factorials, but I was too stupid to realize that is
    // a binomial coefficient, which I have learned before, and knew it had to do with probability, well at least I know
    // now, hopefully next time I can solve this alone.
    cout << total << endl;
}
