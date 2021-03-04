from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        lst = []
        
        #Finding the duplicate number
        cnts = collections.Counter(nums)
        dup = cnts.most_common()[0][0] #finding duplicate function
        lst.append(dup)
        
        #Finding the missing number  
        num_set = tuple(nums) 
        n = len(nums)  
        for number in range(1,n+1):  
            if number not in num_set:  
                lst.append(number)
                
        return lst
