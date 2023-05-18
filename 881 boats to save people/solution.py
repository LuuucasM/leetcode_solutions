class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        num_boats = 0
        i = 0
        j = len(people)-1
        while i <= j:
            num_boats += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return num_boats