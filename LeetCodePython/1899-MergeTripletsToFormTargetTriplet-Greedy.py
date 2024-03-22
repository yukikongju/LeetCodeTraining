class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Solution: Greedy

        # --- base case: zero operations needed
        for triplet in triplets:
            if triplet == target:
                return True

        # --- keep candidates => triplet that whose values don't surpass target
        candidates = [
            t for t in triplets if self.is_smaller_than_target(t, target)]
        if not candidates:
            return False

        # --- sort triplets
        sorted_triplets = sorted(candidates, key=lambda x: (x[0], x[1], x[2]))

        # --- update greedily
        current_triplet = sorted_triplets[0]
        idx = 0
        for triplet in sorted_triplets[1:]:
            # determine if we want to swap => if all triplets[i] less than target
            if self.is_smaller_than_target(triplet, target):
                current_triplet = self.update(current_triplet, triplet)

            # check if we have the target
            if self.is_target(current_triplet, target):
                return True

        return False

    def is_smaller_than_target(self, t, target):
        return (t[0] <= target[0]) and (t[1] <= target[1]) and (t[2] <= target[2])

    def is_target(self, t, target):
        return t == target

    def update(self, t1, t2):
        return [max(t1[0], t2[0]), max(t1[1], t2[1]), max(t1[2], t2[2])]
