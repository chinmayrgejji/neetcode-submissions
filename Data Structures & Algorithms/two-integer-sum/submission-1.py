class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:     
        seen ={}
        for i in range(len(nums)):
            current = nums[i]
            required = target-current
            if required in seen :

                return [seen[required],i]
            seen[current] = i
