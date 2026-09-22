class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i = 0
        j = len(people) - 1
        boat = 0

        # 1 2 2 3 3

        while i <= j:
            if people[i] + people[j] <= limit:
                boat += 1
                i += 1
                j -= 1
            else:
                boat += 1
                j -= 1

        return boat





        