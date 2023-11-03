#include <vector>
#include <queue>

using namespace std;

// The solution to this problem includes tracking two pointers i on the right and j on the left
// while always incrementing i and adding nums[i] to the sum and whenever sum >= target subtracting
// nums[j] from sum and counting the length.
class Solution {
public:
  int minSubArrayLen(int target, vector<int>& nums) {
    int i=0, j=0, sum=0, ans=INT_MAX, n=nums.size();
    while(i < n){
      sum += nums[i];
      while(j <= i && sum >= target) {
        ans = min(ans, i-j+1);
        sum -= nums[j];
        j++;
      }
      i++;
    }
    return ans == INT_MAX ? 0 : ans;
  }
};