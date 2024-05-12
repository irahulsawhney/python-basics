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

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        answer = []
        for i in range(1, n+1):
            answer.append("")
            if i % 3 == 0 or i % 5 == 0:
                if i % 3 == 0:
                    answer[i - 1] = answer[i - 1] + "Fizz"
                if i % 5 == 0:
                    answer[i - 1] = answer[i - 1] + "Buzz"
            else:
                answer[i - 1] = str(i)

        return answer

def main():
    solution = Solution()
    answer = solution.sum(12, 5)
    print(answer)

    answer2 = solution.runningSum([1, 2, 3])
    print(answer2)

    answer2 = solution.fizzBuzz(2)
    print(answer2)

main()
