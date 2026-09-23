class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}

        for i in range(len(nums)):
            if nums[i] in lookup and i - lookup[nums[i]] <= k:
                return True
            lookup[nums[i]] = i

        return False