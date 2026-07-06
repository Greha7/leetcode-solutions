class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left = 0
        right = len(nums)-1
        pos = len(nums)-1
        while left<=right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                result[pos]=nums[left]*nums[left]
                left = left + 1
                pos = pos -1
            else:
                result[pos]=nums[right]*nums[right]
                right = right -1 
                pos = pos -1 
        return result

        