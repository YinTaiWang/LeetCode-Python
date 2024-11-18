class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return true if any value appears at least twice in the array
    
        # only 1 value -> False, because for sure distinct
        if len(nums) == 1:
            return False
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False