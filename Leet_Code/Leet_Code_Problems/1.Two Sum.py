from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i in range(len(nums)):
            m=target-nums[i]
            if(m in d.keys()):
                return list([d.get(m),i])
            else:
                d[nums[i]]=i
            
        return list([])

    
        