#include <bits/stdc++.h>

using namespace std;

bool dfs(unordered_map<string, vector<string>> &graph, const string &current, string &destination, unordered_set<string> &visited, vector<string> &path) {
    path.push_back(current);

    if (current == destination) {
        return true;
    }

    visited.insert(current);

    for (string &neighbor : graph[current]) {
        if (visited.find(neighbor) == visited.end()) {
            if (dfs(graph, neighbor, destination, visited, path)) {
                return true;
            }
        }
    }

    path.pop_back();
    return false;
}

int main() {

    unordered_map<string, vector<string>> unit_graph;
    unordered_map<string, unordered_map<string, pair<double, double>>> equations;

    string input_line;

    while (getline(cin, input_line)) {
        stringstream ss(input_line);
        int spaces = count(input_line.begin(), input_line.end(), ' ') + 1;

        vector<string> vars;
        string sp;

        while (spaces--) {
            ss >> sp;
            vars.push_back(sp);
        }

        if (vars[0] == "K") {

            double extra = 0;

            if (vars.size() > 5) {
                extra = stod(vars[6]);
            }

            if (vars[5] == "-") {
                extra *= -1;
            }

            double r1 = 1 / stod(vars[3]);
            double r2 = extra * -1 / stod(vars[3]);

            equations[vars[1]][vars[4]] = pair(stod(vars[3]), extra);
            equations[vars[4]][vars[1]] = pair(r1, r2);

            unit_graph[vars[1]].push_back(vars[4]);
            unit_graph[vars[4]].push_back(vars[1]);

        } else if (vars[0] == "H") {

            double v1 = stod(vars[1]);
            string n1 = vars[2];
            string n2 = vars[5];
            unordered_set<string> visited;
            vector<string> path;
            visited.reserve(100);
            path.reserve(100);

            bool canSolve = dfs(unit_graph, n1, n2, visited, path);

            if (!canSolve) {
                cout << "Too hard!" << endl;
            } else {
                string prev = n1;
                for (auto it = path.begin() + 1; it != path.end(); it++ ) {
                    string path_part = *it;
                    v1 *= equations[path_part][prev].first;
                    v1 += equations[path_part][prev].second;
                    prev = path_part;
                }
                cout << v1 << endl;

            }
        } else {
            return 0;
        }
    }
}
