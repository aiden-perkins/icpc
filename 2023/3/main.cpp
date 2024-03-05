#include <bits/stdc++.h>

using namespace std;

struct Crd {
    int x;
    int y;
};

int main() {
    Crd end{};
    int wormholeCount = 0;
    vector<vector<int>> wormholes;
    string inputLine;
    while (getline(cin, inputLine)) {
        stringstream ss(inputLine);
        vector<int> line(istream_iterator<int>(ss), {});
        if (wormholeCount == 0) {
            end = {line[0], line[1]};
            wormholeCount = line[2];
        } else {
            wormholes.push_back({line[0], line[1], line[2], line[3]});
        }
    }
    // Create adjacency matrix
    int vertexCount = (end.x + 1) * (end.y + 1);
    int graph[vertexCount][vertexCount];
    for (int i = 0; i < vertexCount; i++) {
        for (int j = 0; j < vertexCount; j++) {
            graph[i][j] = 0;
        }
    }
    for (int x = 0; x <= end.x; x++) {
        for (int y = 0; y <= end.y; y++) {
            int currentIndex = x * (end.y + 1) + y;
            if (x + 1 <= end.x) {
                int up = (x + 1) * (end.y + 1) + y;
                graph[currentIndex][up] = 1;
                graph[up][currentIndex] = 1;
            }
            if (y + 1 <= end.y) {
                int left = x * (end.y + 1) + y + 1;
                graph[currentIndex][left] = 1;
                graph[left][currentIndex] = 1;
            }
        }
    }
    for (int i = 0; i < wormholeCount; i++) {
        int whStart = wormholes[i][0] * (end.y + 1) + wormholes[i][1];
        int whEnd = wormholes[i][2] * (end.y + 1) + wormholes[i][3];
        graph[whStart][whEnd] = 1;
        graph[whEnd][whStart] = 1;
    }
    for (int i = 0; i < vertexCount; i++) {
        cout << "index " << i << " has connections to ";
        for (int j = 0; j < vertexCount; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
    // Create a min distance list that will by default be inf
    // create a final array that is a bool if we have found the shortest path
    // Go until min distance is complete and there is the shortest path to all vertices
    // get the next vertex by finding all that are infinite and are false in final array
    // go through all possible edges and turn them from inf to a value
}
