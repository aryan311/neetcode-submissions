from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counting = Counter(nums)
        newlist = []

        for item, count in counting.most_common():
      
            newlist.append(item)
            if len(newlist) == k:
                break
        return newlist
            
        
        


