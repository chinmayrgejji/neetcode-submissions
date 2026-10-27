class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        i=0
        for i in range(n):
            nums.append(nums[i])
            i+=1
        return nums