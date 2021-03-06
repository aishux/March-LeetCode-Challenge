class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(word[::-1] for word in words) # reverse & sort 
        ans, prev = 0, ""
        for word in words: 
            if not word.startswith(prev): ans += len(prev) + 1
            prev = word
        return ans + len(prev) + 1
        
