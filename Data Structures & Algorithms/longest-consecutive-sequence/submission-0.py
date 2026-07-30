class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dictionary = {}
        for i, num in enumerate(nums):
            dictionary[num] = i

        count = 0
        build_arr = []
        for num in dictionary.keys():
            if num - 1 not in dictionary.keys():
                build_arr.append(num)

        if len(build_arr) == 1:
            return len(set(nums))

        for num in build_arr:
            walk = 1
            while num + 1 in dictionary.keys():
                num = num + 1
                walk = walk + 1
            if count < walk:
                count = walk
        
        return count