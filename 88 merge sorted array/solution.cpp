#include <vector>
class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int back = m+n -1;
        int c1 = m - 1;
        int c2 = n - 1;
        while (c1 >= 0 && c2 >= 0){
            if (nums1[c1] >= nums2[c2]){
                nums1[back] = nums1[c1];
                c1--;
                back--;
            }
            else{
                nums1[back] = nums2[c2];
                c2--;
                back--;
            }
        }
        while (c1 >= 0){
            nums1[back] = nums1[c1];
            c1--;
            back--;
        }
        while (c2 >= 0){
            nums1[back] = nums2[c2];
            c2--;
            back--;
        }
    }
};