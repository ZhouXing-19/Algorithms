from collections import deque

from collections import deque


class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """

    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []

        dq = deque([])

        for i in range(k - 1):
            self.push(dq, nums, i)
            print('in first for, i =', i, " dq = ", dq)

        result = []
        for i in range(k - 1, len(nums)):
            print('in second for, i =', i, " dq = ", dq)
            self.push(dq, nums, i)
            result.append(dq[0])
            print("res.append:",dq[0])
            if len(dq)==k:
                print("pop left")
                dq.popleft()

        return result

    def push(self, dq, nums, i):
        while dq and dq[-1] < nums[i]:
            dq.pop()
        dq.append(nums[i])

s = Solution()
nums = [1,3,1,2,0,5]
k = 3
res = s.maxSlidingWindow(nums,k)
print(res)

