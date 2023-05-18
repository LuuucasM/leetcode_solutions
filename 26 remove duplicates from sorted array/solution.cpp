#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.size() == 1){
            return 1;
        }
        int unique = 0;
        for (int i = 1; i < nums.size(); i++){
            if (nums[unique] != nums[i]){
                unique++;
                nums[unique] = nums[i];
            }
        }
        unique++;
        return unique;
    }
};