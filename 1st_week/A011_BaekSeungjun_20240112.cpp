#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<float, int>& a, const pair<float, int>& b) {
    if(a.first == b.first)
        return a.second < b.second;
    return a.first > b.first;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<float, int>> arr(N);

    int s, f;
    for(int i=1; i<=N; i++) {
        arr[i-1].second = i;
        s = 0;
        f = 0;
        
        for(auto e : stages) {
            if(e >= arr[i-1].second) {
                if(e == arr[i-1].second)
                    f++;
                s++;
            }
        }
        
        if(s == 0)
            arr[i-1].first = 0;
        else
            arr[i-1].first = float(f)/float(s);
    }

    sort(arr.begin(), arr.end(), compare);

    for(auto e : arr) {
        answer.push_back(e.second);
    }
    
    return answer;
}