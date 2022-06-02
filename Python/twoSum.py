# input: nums = [2,7,11,15] target = 9
# output: [0,1]

# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# hashmap = {2: true, 7: true}
# 9 - 2 = 7 no
# 9 - 7 = 2 yes in hashmap

# 0(1) time 
# 0(1) space 

class Solution(object):
    def twoSum(self, nums,target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [num, hashmap[complement]]
            hashmap[nums[num]] = num
            
