#include <string>
#include <stack>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> check;
        for (auto ch : s){
            if (ch == '(' || ch == '{' || ch == '['){
                check.push(ch);
            }
            else{
                if (check.size() == 0){
                    return false;
                }
                if ((ch == ')' && check.top() !='(' ) 
                || (ch == '}' && check.top() != '{')
                || (ch == ']' && check.top() != '[')){
                    return false;
                }
                else{
                    check.pop();
                }
            }
        }
        return check.empty();
    }
};