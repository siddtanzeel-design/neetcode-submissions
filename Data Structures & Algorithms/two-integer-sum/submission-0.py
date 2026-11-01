class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            x = nums[i]
            compare = target - x

            if compare in seen:
                return [seen[compare], i]
            
            seen[x] = i