class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = self.prefixSum(nums.copy())
        postfix = self.postfixSum(nums.copy())
        for i in range(len(nums)):
            if i - 1 < 0:
                output.append(postfix[i+1])
            elif i + 1 >= len(nums):
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1]*postfix[i+1])
        return output

    def prefixSum(self, nums):
        i = 1
        for j in range(len(nums)):
            if i < len(nums):
                nums[i] = nums[i-1] * nums[i]
            i = i + 1

        return nums

    def postfixSum(self, nums):
        i = len(nums) - 1
        for j in range(len(nums)):
            if i + 1 < len(nums):
                nums[i] = nums[i+1] * nums[i]
            i = i - 1

        return nums