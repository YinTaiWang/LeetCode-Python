class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in numDict:
                return [numDict[result], i]
            else:
                numDict[nums[i]] = i
        return []