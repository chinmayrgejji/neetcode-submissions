class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle=0
        i=0
        j=len(nums)-1
        while i<=j:
            middle =(i+j)//2

            if nums[middle]==target:
                break
            elif target>nums[middle]:
                i=middle+1
            elif target<nums[middle]:
                j=middle-1
            if i>j :
                middle=-1           
        return middle

        