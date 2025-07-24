class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
       int  pairs=0;
     int frequency[101] ={0};
        for(int i=0; i<nums.size(); i++){
        pairs += frequency[nums[i]];
            frequency[nums[i]]++;
        
        
        }
        return pairs;
    }
};