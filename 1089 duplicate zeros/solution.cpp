#include <vector>

class Solution {
public:
    void duplicateZeros(std::vector<int>& arr) {
        int i = 0, sh = 0;
        for (i = 0; sh + i < arr.size(); i++) 
            if (arr[i] == 0)
                sh++;
        for (i = i - 1; sh > 0; i--) {
            if (i + sh < arr.size()) 
                arr[i + sh] = arr[i];
            if (arr[i] == 0) 
                arr[i + --sh] = arr[i];
        }
    }
};