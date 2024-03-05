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
    // Creating the adjacency matrix:
    // Start with an empty graph
    int vertexCount = (end.x + 1) * (end.y + 1);
    int graph[vertexCount][vertexCount];
    for (int i = 0; i < vertexCount; i++) {
        for (int j = 0; j < vertexCount; j++) {
            graph[i][j] = 0;
        }
    }
    // Populate that graph with the known grid
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
    // Add the wormholes to connect everything.
    for (int i = 0; i < wormholeCount; i++) {
        int whStart = wormholes[i][0] * (end.y + 1) + wormholes[i][1];
        int whEnd = wormholes[i][2] * (end.y + 1) + wormholes[i][3];
        graph[whStart][whEnd] = 1;
        graph[whEnd][whStart] = 1;
    }
    // Create a min distance list that will hold the min distances to each vertex, INT_MAX by default.
    int minDistance[vertexCount];
    // Create a finished array that is full of false that represents if we have found the min path to that vertex.
    int finished[vertexCount];
    int minPathCount[vertexCount];
    for (int i = 0; i < vertexCount; i++) {
        minDistance[i] = INT_MAX;
        finished[i] = false;
        minPathCount[i] = 1;
    }
    minDistance[0] = 0;
    // minPathCount[0] = 1;
    // Loop enough times that finished becomes all true.
    for (int _ = 0; _ < vertexCount; _++) {
        // Get the next vertex by finding an index that is false in finished, and if there is more than one, find the min.
        int currentIdx = -1;
        int nextMinDistance = INT_MAX;
        for (int i = 0; i < vertexCount; i++) {
            if (minDistance[i] <= nextMinDistance && !finished[i]) {
                nextMinDistance = minDistance[i];
                currentIdx = i;
            }
        }
        if (currentIdx == -1) {
            throw runtime_error("finished is complete");
        }
        finished[currentIdx] = true;
        // Go through all possible edges from the current vertex and update the correct things.
        for (int i = 0; i < vertexCount; i++) {
            // Check for unfinished neighbors of our current index.
            if (!finished[i] && graph[currentIdx][i]) {
                // Check if the new path is shorter than previously known.
                if (minDistance[currentIdx] + 1 < minDistance[i]) {
                    minDistance[i] = minDistance[currentIdx] + 1;
                    minPathCount[i] = minPathCount[currentIdx];
                } else if (minDistance[currentIdx] + 1 == minDistance[i]) {
                    minPathCount[i] += minPathCount[currentIdx];
                }
            }
        }
    }
    cout << minPathCount[vertexCount - 1] << endl;
}
