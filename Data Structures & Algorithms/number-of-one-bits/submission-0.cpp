class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        vector<int> ones;
        while(n>0) {
            ones.push_back(n%2);
            n/=2;
        }
        for (int i=0; i<ones.size(); i++) {
            if (ones[i]==1) {
                count++;
            }
        }
        return count;
    }
};
