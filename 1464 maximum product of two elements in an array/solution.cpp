#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        if (nums.size() == 2){
            return ((nums[0]-1) * (nums[1]-1));
        }
        
        std::make_heap(nums.begin(), nums.end());
        return ((nums[0]-1)*(std::max(nums[1], nums[2])-1));
    }
};