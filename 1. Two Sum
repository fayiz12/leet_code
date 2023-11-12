class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dic={}
        
        for i, num in enumerate(nums):
            num1=target-num

            if num1 in new_dic:
                return [new_dic[num1],i]


            new_dic[num]=i
