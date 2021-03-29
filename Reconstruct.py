class Solution:
    def originalDigits(self, s: str) -> str:
        class Solution:
    def originalDigits(self, s: str) -> str:
        # count char appearance
        charDict = collections.Counter(s)
        # a list to hold our number counts
        resArr = [0]*10
        # check for w, u, x, g as they only exist in two, four, six, eight
        if 'w' in charDict:
            resArr[2]  = charDict['w']
            charDict['t'] -= resArr[2]
            charDict['w'] -= resArr[2]
            charDict['o'] -= resArr[2]
        if 'u' in charDict:
            resArr[4]  = charDict['u']
            charDict['f'] -= resArr[4]
            charDict['o'] -= resArr[4]
            charDict['u'] -= resArr[4]
            charDict['r'] -= resArr[4]
        if 'x' in charDict:
            resArr[6]  = charDict['x']
            charDict['s'] -= resArr[6]
            charDict['i'] -= resArr[6]
            charDict['x'] -= resArr[6]
        if 'g' in charDict:
            resArr[8]  = charDict['g']
            charDict['e'] -= resArr[8]
            charDict['i'] -= resArr[8]
            charDict['g'] -= resArr[8]
            charDict['h'] -= resArr[8]
            charDict['t'] -= resArr[8]
        # check for s and f as they only exist in five and seven now
        if 'f' in charDict:
            resArr[5]  = charDict['f']
            charDict['f'] -= resArr[5]
            charDict['i'] -= resArr[5]
            charDict['v'] -= resArr[5]
            charDict['e'] -= resArr[5]
        if 's' in charDict:
            resArr[7]  = charDict['s']
            charDict['s'] -= resArr[7]
            charDict['e'] -= resArr[7]*2
            charDict['v'] -= resArr[7]
            charDict['n'] -= resArr[7]
        # check for t, i, z as they only exist in three, nine, zero now
        if 't' in charDict:
            resArr[3]  = charDict['t']
            charDict['t'] -= resArr[3]
            charDict['h'] -= resArr[3]
            charDict['r'] -= resArr[3]
            charDict['e'] -= resArr[3]*2
        if 'i' in charDict:
            resArr[9]  = charDict['i']
            charDict['n'] -= resArr[9]*2
            charDict['i'] -= resArr[9]
            charDict['e'] -= resArr[9]
        if 'z' in charDict:
            resArr[0]  = charDict['z']
            charDict['z'] -= resArr[0]
            charDict['e'] -= resArr[0]
            charDict['r'] -= resArr[0]
            charDict['o'] -= resArr[0]
        # the rest should be one
        resArr[1]  = charDict['o']
        # build our res
        res = ''
        for i in range(10):
            res+=str(i)*resArr[i]
        return res
