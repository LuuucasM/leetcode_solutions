#include <vector>

class Solution {
public:
    std::vector<int> sortedSquares(std::vector<int>& nums) {
        std::vector<int> ans;
        int left=-1, right=0;
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] < 0)
                left = i;
        right = left + 1;

        while (left >= 0 && right < nums.size()){

            if (-1*nums[left] < nums[right]){
                ans.push_back(nums[left]*nums[left]); 
                left--;
            }        
            else{
                ans.push_back(nums[right]*nums[right]);
                right++;
            }
        }
        while (left >= 0){
            ans.push_back(nums[left]*nums[left]);
            left--;
        }
            
        while (right < nums.size()){
            ans.push_back(nums[right]*nums[right]);
            right++;
        }

        return ans;
    }
};