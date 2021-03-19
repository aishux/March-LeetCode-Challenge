class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len( nums )
        
        # length of wiggle sequence, ending in positive difference, negative difference
        positive, negative = 1, 1
        
        
        # scan from secnond number to last number
        for i in range(1, n):
        
            if nums[i] > nums[i-1]:
                
                # difference is positive, concatenated with negative prefix wiggle subsequence
                positive = negative + 1
                
            elif nums[i] < nums[i-1]:
                
                # differnce is negative, concatenated with positive prefix wiggle subsequence
                negative = positive + 1
                
        # compute the longest length of wiggle sequence                
        return max(positive, negative)
