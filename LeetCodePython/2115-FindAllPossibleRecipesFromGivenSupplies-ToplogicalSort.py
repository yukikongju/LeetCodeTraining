#  https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # solution: Topological Sort

        res = []
        seen = set(supplies)
        dq = deque([(r, ings) for r, ings in zip(recipes, ingredients)])

        prev_len = len(seen) - 1 # dummy
        while len(seen) > prev_len:
            prev_len = len(seen)
            for _ in range(len(dq)):
                r, ings = dq.popleft()
                if all(ing in seen for ing in ings):
                    seen.add(r)
                    res.append(r)
                else: 
                    dq.append((r, ings))

        return res


