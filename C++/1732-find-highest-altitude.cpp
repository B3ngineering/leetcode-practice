
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0;
        int start = 0;
        for (int value : gain) {
            if (start + value > highest) {
                highest = start + value;
            }
            start = start + value;
        }
        return highest;
    }
};