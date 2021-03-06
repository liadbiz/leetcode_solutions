"""
377. Combination Sum IV
source: https://leetcode-cn.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative

"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted([i for i in nums if i > 0 and i <= target])
        dp = [1] + [0] * target
        for i in range(1, target+ 1):
            dp[i] = sum(dp[i-j] for j in nums if j <= i)
        print(dp)
        return dp[target]

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    print(Solution().combinationSum4(nums, target))
