from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        # buckets[i] = numbers that appear i times
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        # Start from highest frequency
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        