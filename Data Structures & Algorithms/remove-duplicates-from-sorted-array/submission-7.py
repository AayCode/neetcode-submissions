class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0

        # 1 2 3 4 4
        #       k
        #           i

        while i < len(nums):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
            i += 1

        return k + 1