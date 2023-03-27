#include <vector>
#include <string>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        std::vector<int> letters(255, 0);
        for (char l : magazine)
            letters[l]++;
        for (char l : ransomNote){
            if (letters[l] == 0){
                return false;
            }
            letters[l]--;
        }
        return true;
    }
};