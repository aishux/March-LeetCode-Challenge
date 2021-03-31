class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## Similar to Leetcode : 300 Longest Increasing Subsequence ##
        
		## TIME COMPLEXITY : O(NlogN) ##
		## SPACE COMPLEXITY : O(N) ##

        ## LIS : replace larger number with small one, append larger numbers ##
        ## NUMS  [100, 89, 53, 68, 45, 81] ##
        ## DP ##
        # [100]
        # [89]
        # [53]
        # [53, 68]
        # [45, 68]
        # [45, 68, 81]
        
        def lis(nums):
            # print(nums)
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
                # print(dp)
            return len(dp)
        
        # sort increasing in first dimension and decreasing on second
        # take a moment and think why ? ( we want to perform LIS on second dimension, think in terms when a set of boxes have same first dimension)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # extract the second dimension and run the LIS
        return lis([envelope[1] for envelope in envelopes])  
