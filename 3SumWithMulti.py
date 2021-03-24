class Solution:
    def threeSumMulti(self, A, target):
        d = [0] * 300
        res = 0
        for i in range(len(A)):
            res += d[target-A[i]] if target-A[i] >=0 else 0
            res %= (10**9+7)
            for j in range(i):
                d[A[i] + A[j]] += 1
        return res % (10**9+7)
        
