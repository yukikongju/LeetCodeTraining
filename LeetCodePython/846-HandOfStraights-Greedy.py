class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Solution: Greedy with minHeap
        # we sort the cards because the first card has to be matched

        # --- base case
        if len(hand) % groupSize != 0:
            return False

        # --- sort cards
        sorted(hand, reverse=False)

        # --- greedy algorithm
        heapq.heapify(hand)
        current_group = []
        tmp = []
        while hand:
            card = heapq.heappop(hand)
            if current_group:
                if card == current_group[-1] + 1:
                    current_group.append(card)
                else:
                    tmp.append(card)
            else:
                current_group.append(card)

            if len(current_group) == groupSize:
                current_group = []
                for c in tmp:
                    heapq.heappush(hand, c)
                tmp = []

        return True if len(tmp) == 0 and len(hand) == 0 else False
