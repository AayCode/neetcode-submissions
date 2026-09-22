class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        total = 0

        # 0 2 0 3 1 0 1 3 2 1
        #               j
        #   i

        while i < j:
            while i < j and height[j] <= height[j - 1]:
                j -= 1
            while i < j and height[i] <= height[i + 1]:
                i += 1

            if height[i] <= height[j]:
                temp = i
                i += 1

                while i < j and height[i] <= height[temp]:
                    total -= height[i]
                    i += 1

                total += (i - temp - 1) * height[temp]

            else:
                temp = j
                j -= 1

                while i < j and height[j] <= height[temp]:
                    total -= height[j]
                    j -= 1

                total += (temp -j - 1) * height[temp]

        return total
            



                





            