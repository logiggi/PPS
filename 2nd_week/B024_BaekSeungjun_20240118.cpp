#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> idx;
        int len = score.size();
        for(int i=0; i<len; i++) {
            idx.push_back(make_pair(score[i], i));
        }

        sort(idx.begin(), idx.end(), greater<pair<int, int>>());

        vector<string> ans(len, "");
        for(int i=0; i<len; i++) {
            if(i == 0) {
                ans[idx[i].second] = "Gold Medal";
            } else if(i == 1) {
                ans[idx[i].second] = "Silver Medal";
            } else if(i == 2) {
                ans[idx[i].second] = "Bronze Medal";
            } else {
                ans[idx[i].second] = to_string(i+1);
            }
        }
        
        return ans;
    }
};