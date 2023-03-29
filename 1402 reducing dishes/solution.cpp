#include <vector>
#include <algorithm>

class Solution {
public:
    int maxSatisfaction(std::vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end(), std::greater<int>());

        int total = 0;
        int thesum = 0;

        for (int ele : satisfaction){
            thesum += ele;
            if (thesum <= 0){
                break;
            }
            total += thesum;
        }
        return total;
    }
};