class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        tracker = set(nums)

        count = 0
        build_arr = []
        for num in tracker:
            if num - 1 not in tracker:
                build_arr.append(num)

        if len(build_arr) == 1:
            return len(set(nums))

        for num in build_arr:
            walk = 1
            while num + 1 in tracker:
                num = num + 1
                walk = walk + 1
            if count < walk:
                count = walk
        
        return count