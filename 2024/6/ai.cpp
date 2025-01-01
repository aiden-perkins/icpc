
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;

// Function to find all possible ways to combine two words
vector<string> getAllCombinations(const string& s, const string& t) {
    vector<string> results;
    // Try all possible overlaps
    for(int len = min(s.length(), t.length()); len > 0; len--) {
        // Check if suffix of s matches prefix of t
        if(s.substr(s.length() - len) == t.substr(0, len)) {
            results.push_back(s + t.substr(len));
        }
        // Check if suffix of t matches prefix of s
        if(t.substr(t.length() - len) == s.substr(0, len)) {
            results.push_back(t + s.substr(len));
        }
    }
    return results;
}

string solve(vector<string>& words) {
    if(words.size() == 1) return words[0];
    
    string best = "";
    int bestLen = INT_MAX;
    
    // Try combining each pair of words
    for(int i = 0; i < words.size(); i++) {
        for(int j = i + 1; j < words.size(); j++) {
            vector<string> combinations = getAllCombinations(words[i], words[j]);
            
            for(const string& combined : combinations) {
                // Create new vector without used words and add combined word
                vector<string> newWords;
                for(int k = 0; k < words.size(); k++) {
                    if(k != i && k != j) newWords.push_back(words[k]);
                }
                newWords.push_back(combined);
                
                // Recursive call
                string result = solve(newWords);
                if(result != "-1") {
                    if(result.length() < bestLen || 
                       (result.length() == bestLen && result < best)) {
                        best = result;
                        bestLen = result.length();
                    }
                }
            }
        }
    }
    
    return bestLen == INT_MAX ? "-1" : best;
}

int main() {
    int n;
    cin >> n;
    
    vector<string> words(n);
    for(int i = 0; i < n; i++) {
        cin >> words[i];
    }
    
    // If there's only one word, return it
    if(n == 1) {
        cout << words[0] << endl;
        return 0;
    }
    
    string result = solve(words);
    cout << result << endl;
    
    return 0;
}
