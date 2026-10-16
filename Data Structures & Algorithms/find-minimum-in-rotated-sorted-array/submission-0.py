class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        middle=(i+j)//2

        while i<j:
            if nums[middle] > nums[j]:
                i=middle+1
            elif nums[middle] < nums[j]:
                j=middle
            middle=(i+j)//2

        return nums[i]