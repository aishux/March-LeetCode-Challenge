class Solution:      
    def hasAllCodes(self, s: str, k: int) -> bool:
        x = len(set(s[i:i+k] for i in range(0,(len(s)-k)+1)))
        return x == 2**k
        
