from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_deque = deque()
        d_deque = deque()

        for i, ele in enumerate(senate):
            if ele == "R":
                r_deque.append(i)
            else:
                d_deque.append(i)
        
        while r_deque and d_deque:
            r_turn = r_deque.popleft()
            d_turn = d_deque.popleft()

            if r_turn > d_turn:
                d_deque.append(d_turn + len(senate))
            else:
                r_deque.append(r_turn + len(senate))

        return "Radiant" if r_deque else "Dire"