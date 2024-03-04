#include <bits/stdc++.h>

using namespace std;

struct Coord {
    int x;
    int y;
};

int main() {
    string inputLine;
    Coord end{};
    int wormholeCount = 0;
    vector<pair<Coord, Coord>> wormholes;
    while (getline(cin, inputLine)) {
        stringstream ss(inputLine);
        vector<int> line(istream_iterator<int>(ss), {});
        if (wormholeCount == 0) {
            end = {line[0], line[1]};
            wormholeCount = line[2];
        } else {
            wormholes.push_back({{line[0], line[1]}, {line[2], line[3]}});
        }
    }
    cout << "end (x, y) are (" << end.x << ", " << end.y << "), wormhole count is " << wormholeCount << ", at: " << endl;
    for (pair<Coord, Coord> wormhole: wormholes) {
        cout << wormhole.first.x << ", " << wormhole.first.y << " to ";
        cout << wormhole.second.x << ", " << wormhole.second.y;
    }
    // Plan:
    // 1. Make a graph of the grid only
    // 2. Connect the vertices that are wormholes
    // 3. Once I have this completed graph I can use a path finding algorithm (dijkstra) to find the min distance.
    // 4. Then I can run a BFS and eliminate distances that go above that min, and count the ones that reach the end.
    // OR
    // 3. I modify dijkstra to not stop when it finds the min and just keep a count of equal distances.
    // I will probably try the later first but if it's too confusing then I'm sure the former will work.
}
