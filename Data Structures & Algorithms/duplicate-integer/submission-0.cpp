class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // int numLength = len(nums);
        // int counter = 0;
        // vector numBank = [];
        // while(counter < numLength){
        //     if (nums[numLength] != numBank) {
        //         numBank.append(nums[numLength])
        //     }

        // }

        vector<int> seen;
        int counter = 0;
        while(nums.size() > counter){
            int counterInner = 0;
            while (seen.size() > counterInner){
                if (nums[counter] == seen[counterInner]) {
                    return true;
                }
                counterInner++;
            }
            seen.push_back(nums[counter]);
            counter++;
        }

        return false;
    
    }
};

// thought process, I'm going to checke every value of the array with a simple while loop using a number bank