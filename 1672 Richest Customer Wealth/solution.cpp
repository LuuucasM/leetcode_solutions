#include <vector>
#include <algorithm>
#include <numeric>

class Solution {
public:
    int maximumWealth(std::vector<std::vector<int>>& accounts) {
        int top = -1;
        for (auto &vec : accounts){
            top = std::max(top, std::accumulate(vec.begin(), vec.end(), 0));
        }
        return top;
    }
};