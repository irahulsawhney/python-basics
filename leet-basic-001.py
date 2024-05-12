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
            for accountNumber in range(len(accounts[customerNumber])):
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
        for i in range(1, n + 1):
            answer.append("")
            if i % 3 == 0 or i % 5 == 0:
                if i % 3 == 0:
                    answer[i - 1] = answer[i - 1] + "Fizz"
                if i % 5 == 0:
                    answer[i - 1] = answer[i - 1] + "Buzz"
            else:
                answer[i - 1] = str(i)

        return answer

    def fizzBuzz2(selfself, n):
        """
        :param n: int
        :return: List[str]
        """
        return [
            "FizzBuzz" if number % 3 == 0 and number % 5 == 0 else "Fizz" if number % 3 == 0 else "Buzz" if number % 5 == 0 else str(
                number) for number in range(1, n + 1)]

    # Number of steps to count to 0, if even, halve the number, if odd, reduce by one in each step.
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num == 0):
            return 0
        if (num % 2 == 0):
            return self.numberOfSteps(num / 2) + 1
        else:
            return self.numberOfSteps(num - 1) + 1

    def numberOfSteps2(self, num):
        """
        :type num: int
        :rtype: int
        """
        c = 0
        while num != 0:
            if num%2 == 0:
                num = num/2
                c = c+1
            else:
                num = num-1
                c = c+1
        return c

    # https://leetcode.com/problems/middle-of-the-linked-list/
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = 0
        current_node = head
        while(current_node != None):
            size = size+1
            current_node = current_node.next

        if size % 2==0:
            skip = size/2
        else:
            skip = (size-1)/2
        for i in range (0,skip):
            head=head.next
        return head

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle_node = head
        while (head and head.next):
            middle_node = middle_node.next
            head = head.next.next
        return middle_node


def main():
    solution = Solution()
    answer = solution.sum(12, 5)
    print(answer)

    answer = solution.runningSum([1, 2, 3])
    print(answer)

    answer = solution.fizzBuzz(2)
    print(answer)

    print(solution.fizzBuzz2(150))

    print(solution.numberOfSteps(150))
    print(solution.numberOfSteps2(150))

if __name__ == "__main__":
    main()
