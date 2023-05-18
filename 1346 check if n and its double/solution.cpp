#include <vector>
#include <map>

class Solution {
public:
    bool checkIfExist(std::vector<int>& arr) {
        std::map<int, int> seen;
        for (int num : arr){
            if (seen.count(2*num) > 0)
                return true;
            if (num % 2 == 0 && seen.count(num/2) > 0)
                return true;
            seen.insert({num, 1});
        }
        return false;
    }
};