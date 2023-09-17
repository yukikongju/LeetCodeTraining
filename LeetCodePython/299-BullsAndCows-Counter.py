#  https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # solution: count dict

        # --- count bulls + build count dict for cows
        bulls = 0
        secret_counts, guess_counts = defaultdict(int), defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[s] += 1
                guess_counts[g] += 1
        print(secret_counts, guess_counts)
        # --- counts cows: 
        cows = 0
        for g, gcount in guess_counts.items():
            scount = secret_counts[g]
            
            if (scount == gcount) or (gcount > scount): cows += scount
            elif (gcount < scount): cows += gcount
            
        # --- build output string
        output = f"{bulls}A{cows}B"
        return output

