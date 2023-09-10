class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # sol: backtracking-ish
        solutions = []
        seen = set()

        def backtracking(v):
            number = int(v)
            if number not in seen and number <= n:
                solutions.append(number)
                seen.add(number)

                for i in range(0, 10):
                    w = v + f'{i}'
                    backtracking(w)

        for i in range(1,10):
            backtracking(f'{i}')

        return solutions
