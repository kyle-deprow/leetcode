#include<numeric>

class Solution {
public:
    int myAtoi(string s) {
        // Iniatilize result
        int res = 0;
        int sign_flag = 0;

        // Iterate through string and calculate int value
        // From corresponding ASCII character char values.
        // This is done by first verifying char is a numeric
        // and then subtracting '0' from the char to get int
        // value.  10's place is handled by multiplying the
        // residual by 10 to shift digits to the left
        for (auto &ch : s) {
            // If reading in a signed character, assign value to flag
            if ((sign_flag == 0) && ((ch == '-') || (ch == '+'))) {
                sign_flag = (ch == '-') ? -1 : 1;
            }

            else if (isdigit(ch)) {
                // Assume return is positive if not specified
                if (sign_flag == 0) {
                    sign_flag = 1;
                }

                // Perform type casting here for comparison checks
                int char_val = ch - '0';
                if (res > ((std::numeric_limits<int>::max() - char_val)/10)) {
                    if (sign_flag == -1) {
                        return std::numeric_limits<int>::min();
                    }
                    else {
                        return std::numeric_limits<int>::max();
                    }
                }
                // Perform calculation and save into residual
                else {
                    res = res*10 + char_val;
                }
            }
            // Break if reading in a non-numeric character or a space after having read in a number
            else if ((ch != ' ') || (ch == ' ' && sign_flag != 0)) {
                break;
            }
        }

        return res*sign_flag;
    }
};