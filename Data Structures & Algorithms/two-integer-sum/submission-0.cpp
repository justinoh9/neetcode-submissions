class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /* initial thouhgts
            have the first pointer point to first number 
            then do the target - first pointer = second pointer
        */
        vector<int> answer;
        for(size_t i = 0; i < nums.size(); i++) {
            for (size_t j = i+1; j < nums.size(); j++) {
                if (target - nums[i] == nums[j]) {
                    answer.push_back(i);
                    answer.push_back(j);
                }
            }
        }
        return answer;
    }
};
