
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Pattern {
    vector<pair<int, int>> ranges;  // Valid ranges for this pattern

    Pattern(const string& s, int r) {
        if (s[0] != '?' && s[1] != '?') {
            // Fixed number
            int num = (s[0] - '0') * 10 + (s[1] - '0');
            if (num <= r) ranges.emplace_back(num, num);
        }
        else if (s[0] != '?' && s[1] == '?') {
            // First digit fixed
            int start = (s[0] - '0') * 10;
            int end = min(start + 9, r);
            if (start <= r) ranges.emplace_back(start, end);
        }
        else if (s[0] == '?' && s[1] != '?') {
            // Second digit fixed
            int digit = s[1] - '0';
            for (int i = 0; i <= 9 && i * 10 + digit <= r; i++) {
                ranges.emplace_back(i * 10 + digit, i * 10 + digit);
            }
        }
        else {
            // Both wild
            ranges.emplace_back(1, r);
        }
    }
};

long long solve(const vector<Pattern>& patterns, int r) {
    int n = patterns.size();
    vector<vector<long long>> dp(2, vector<long long>(r + 1, 0));
    int curr = 0, prev = 1;

    // Initialize for first pattern
    for (const auto& range : patterns[0].ranges) {
        for (int num = range.first; num <= range.second; num++) {
            dp[curr][num] = 1;
        }
    }

    // For each subsequent pattern
    for (int i = 1; i < n; i++) {
        swap(curr, prev);
        fill(dp[curr].begin(), dp[curr].end(), 0);

        // For each valid range in current pattern
        for (const auto& range : patterns[i].ranges) {
            for (int num = range.first; num <= range.second; num++) {
                // Add all valid combinations from previous numbers
                for (int prevNum = 1; prevNum < num; prevNum++) {
                    dp[curr][num] += dp[prev][prevNum];
                }
            }
        }
    }

    // Sum all valid combinations
    long long result = 0;
    for (int i = 1; i <= r; i++) {
        result += dp[curr][i];
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int n, r;
        cin >> n >> r;

        vector<string> pattern_strings(n);
        for (int i = 0; i < n; i++) {
            cin >> pattern_strings[i];
        }

        // Process patterns
        vector<Pattern> patterns;
        patterns.reserve(n);
        bool impossible = false;
        int lastFixed = 0;

        for (const string& s : pattern_strings) {
            patterns.emplace_back(s, r);
            // Check if this pattern is fixed and creates an impossible sequence
            if (s[0] != '?' && s[1] != '?') {
                int num = (s[0] - '0') * 10 + (s[1] - '0');
                if (num <= lastFixed || num > r) {
                    impossible = true;
                    break;
                }
                lastFixed = num;
            }
        }

        if (impossible) {
            cout << "0\n";
            continue;
        }

        cout << solve(patterns, r) << "\n";
    }

    return 0;
}
