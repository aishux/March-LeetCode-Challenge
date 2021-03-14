class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Use OrderedDict to get smaller keys up front
        dp = OrderedDict()
        for a in sorted(arr):
            total = 1  # The tree with the number itself
            for b in dp:
                div, mod = divmod(a, b)
                if b > div:
                    # Break early when sqrt reached
                    break
                elif mod == 0:
                    # Multiple by 1 if the two children nodes are the same
                    total += dp[b] * dp.get(div, 0) * (1 if b == div else 2)
            dp[a] = total
        return sum(dp.values()) % (10 ** 9 + 7)
