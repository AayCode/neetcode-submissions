class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates
        count1 = count2 = 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1

        res = []
        if count1 > len(nums) // 3:
            res.append(candidate1)
        if count2 > len(nums) // 3:
            res.append(candidate2)

        return res
