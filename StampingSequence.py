class Solution:
    def movesToStamp(self, s: str, t: str) -> List[int]:
        options = {i*'*' + s[i:j] + (len(s)-j)*'*' for i in range(len(s)) for j in range(i, len(s)+1)} - {'*'*len(s)}
        res = []
        target = list(t)
        
        updates = -1
        while updates:
            i = updates = 0
            t = ''.join(target)
            while i <= len(t) - len(s):
                if t[i:i+len(s)] in options:
                    res.append(i)
                    target[i:i+len(s)] = ['*']*len(s)
                    updates += 1
                i += 1
                
        return res[::-1] if set(target) == {'*'} else []
