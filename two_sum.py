"""Two sum Module"""
class Solution:
    "Two sum Class"
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for key,num in enumerate(nums):
            compliment = target - num
            # print(num_map)
            if compliment in num_map:
                print(compliment)
                print(num_map)
                print('')
                return [num_map[compliment],key]
            
            print(num_map)
            print(num)
            print(key)
            print("")
            num_map[num] = key
        return []
answer = Solution()
values = answer.two_sum([2,7,11,15],9)
print(values)
