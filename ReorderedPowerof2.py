class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        if N and (not(N & (N - 1))):
            return True
        q = [''.join(tups) for tups in permutations([i for i in str(N)]) if tups[0] != "0"]
        for i in q:
            if int(i) and (not(int(i) & (int(i) - 1))):
                return True
        return False
