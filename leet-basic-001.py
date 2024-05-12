class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1 + num2

    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    """
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arrayLength = len(nums)
        answer = [nums[0]]
        for i in range(1, arrayLength):
            answer.append(answer[i - 1] + nums[i])
        return answer

    """ https://leetcode.com/problems/richest-customer-wealth/ """
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for customerNumber in range(len(accounts)):
            customerWealth = 0
            for accountNumber in range (len(accounts[customerNumber])):
                customerWealth += accounts[customerNumber][accountNumber]
            if customerWealth > maxWealth:
                maxWealth = customerWealth
        return maxWealth

def main():
    solution = Solution()
    answer = solution.sum(12, 5)
    print(answer)

    answer2 = solution.runningSum([1, 2, 3])
    print(answer2)


main()
