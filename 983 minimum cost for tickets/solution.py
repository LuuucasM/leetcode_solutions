class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        window = [0] * 366
        travelling_days = set(days)
        for i in range(1, len(window)):
            if i not in travelling_days:
                window[i] = window[i-1]
            else:
                window[i] = min(window[i-1]+costs[0], window[max(0, i-7)]+costs[1], window[max(0, i-30)]+costs[2])

        return window[365]