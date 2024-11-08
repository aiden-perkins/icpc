#include <iostream>
#include <sstream>
using namespace std;

bool subset_sum(int* items, int n, long long d, int &subset_sizes, bool &keep_going, int current_size = 0) {
    if (!keep_going) {
        return false;
    }
    if (d == 0) {
        if (subset_sizes == -1) {
            subset_sizes = current_size;
        } else if (subset_sizes != current_size) {
            keep_going = false;
            return false;
        }
        return true;
    }
    if (n == 0)
        return false;

    if (items[n - 1] > d)
        return subset_sum(items, n - 1, d, subset_sizes, keep_going, current_size);

    bool s1 = subset_sum(items, n - 1, d, subset_sizes, keep_going, current_size);
    bool s2 = subset_sum(items, n - 1, d - items[n - 1], subset_sizes, keep_going, current_size + 1);
    return s1 || s2;
}

int main() {
    string inputLine;
    getline(cin, inputLine);
    int cases = stoi(inputLine);
    
    for (int i = 0; i < cases; i++) {
        getline(cin, inputLine);
        istringstream iss(inputLine);
        int itemCount;
        long long diff;
        iss >> itemCount >> diff;

        getline(cin, inputLine);
        iss.clear();
        iss.str(inputLine);
        int items[itemCount];
        for (int j = 0; j < itemCount; j++) {
            iss >> items[j];
        }
        
        int subset_sizes = -1;
        bool keep_going = true;
        subset_sum(items, itemCount, diff, subset_sizes, keep_going);
        
        cout << "Case #" << i + 1 << ": ";
        if (keep_going && subset_sizes > 0) {
            cout << subset_sizes << endl;
        } else if (!keep_going) {
            cout << "AMBIGIOUS" << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
