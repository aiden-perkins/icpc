#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> denoms(n);
    for (int i = 0; i < n; i++) {
        cin >> denoms[i];
    }

    vector<pair<char, int>> events;
    set<int> x_denoms;
    vector<int> queries;
    int max_v = 0;

    for (int i = 0; i < m; i++) {
        char c;
        int v;
        cin >> c >> v;
        events.push_back({c, v});
        if (c == 'X') {
            x_denoms.insert(v);
        } else {
            queries.push_back(v);
            max_v = max(max_v, v);
        }
    }

    vector<int> initial_coins;
    for (int d : denoms) {
        if (x_denoms.find(d) == x_denoms.end()) {
            initial_coins.push_back(d);
        }
    }
    sort(initial_coins.rbegin(), initial_coins.rend());

    const int INF = INT_MAX/2;
    vector<int> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int coin : initial_coins) {
        if (coin > max_v) continue;
        for (int i = coin; i <= max_v; i++) {
            if (dp[i - coin] + 1 < dp[i]) {
                dp[i] = dp[i - coin] + 1;
            }
        }
    }

    vector<int> res;
    for (int i = events.size() - 1; i >= 0; i--) {
        char c = events[i].first;
        int v = events[i].second;

        if (c == 'Q') {
            if (v > max_v) {
                res.push_back(-1);
            } else {
                res.push_back(dp[v] == INF ? -1 : dp[v]);
            }
        } else {
            int coin = v;
            if (coin > max_v) continue;
            for (int j = coin; j <= max_v; j++) {
                if (dp[j - coin] + 1 < dp[j]) {
                    dp[j] = dp[j - coin] + 1;
                }
            }
        }
    }

    reverse(res.begin(), res.end());
    for (int ans : res) {
        cout << ans << "\n";
    }

    return 0;
}
