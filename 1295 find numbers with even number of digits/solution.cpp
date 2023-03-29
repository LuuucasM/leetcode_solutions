#include <vector>
#include <string>

class Solution {
public:
    int findNumbers(std::vector<int>& nums) {
        int evens = 0;
        for (auto num : nums){
            if (std::to_string(num).length() % 2 == 0){
                evens++;
            }
        }
        return evens;
    }
};