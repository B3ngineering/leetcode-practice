#include <vector>
using namespace std;

void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // If we see a 0, we swap it with our other pointer
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] != 0) {
                // We can use temp variables instead, but this is more readable
                swap(nums[r], nums[l]);
                l++;
            }
        }
    }
};