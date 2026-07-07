class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pos = len(nums1)-1
        left = m-1
        right = len(nums2)-1
        while left>=0 and right>=0:
            if nums1[left]>nums2[right]:
                nums1[pos]=nums1[left]
                left = left-1
                pos = pos-1

            else:
                nums1[pos]=nums2[right]
                pos = pos-1
                right = right -1

        while right>=0:
            nums1[pos]=nums2[right]
            right=right-1
            pos = pos -1

        
        