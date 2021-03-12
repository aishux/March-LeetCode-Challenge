class Solution:
    def coinChange(self, coins: List[int], sumx: int) -> int:
        
        n = len(coins) 

        t = [[999999999 for i in range(sumx+1)] for j in range(n+1)] 
        
        for i in range(1, n + 1):
            t[i][0] = 0

 
        for j in range(1, (sumx + 1)):
            if j % coins[0] == 0:
                t[1][j] = j // coins[0]
            else:
                t[1][j] = 999999999
                
        for i in range(2, n + 1):

            for j in range(1, (sumx + 1)):
                if coins[i - 1] > j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = min(t[i-1][j], 1 + t[i][j-coins[i-1]]) 

        return -1 if t[n][sumx] == 999999999  else t[n][sumx]
