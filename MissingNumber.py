class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        num_set = tuple(nums) 
        n = len(nums)  
        for number in range(n+1):  
            if number not in num_set:  
                return number
                
