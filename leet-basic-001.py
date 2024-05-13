import math
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

    # https: // leetcode.com / problems / ransom - note / description /
    # Slow solution, using loops
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)<1 or len(magazine)>10**5:
            print("Error: input conditions not met", len(magazine), len(ransomNote))
            return None

        returnValue = True
        i = 0
        while i in range (0, len(magazine)) and returnValue is True:
            searchChar = magazine[i]
            found = False
            j = 0
            while j in range (0, len(ransomNote)) and found is False:
                if searchChar==ransomNote[j]:
                    x=ransomNote[:j]
                    y=ransomNote[j+1:]
                    ransomNote = x + y
                    found=True
                j += 1
            if found is False:
                returnValue = False
            i += 1
        return returnValue

    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        allChars = {}
        for myChar in ransomNote:
            if myChar not in allChars:
                allChars[myChar] = 1
            else:
                allChars[myChar] += 1

        found = True
        for myChar in magazine:
            if found is True:
                if myChar in allChars and allChars[myChar]>0:
                    allChars[myChar] -= 1
                else:
                    found = False
        return found

    def findMax3x3(self,smallGrid):
        maximum = smallGrid[0][0]
        for i in range (0, len(smallGrid)):
            for j in range (0, len(smallGrid[0])):
                maximum = max(maximum, smallGrid[i][j])
        return maximum

    # https://leetcode.com/problems/largest-local-values-in-a-matrix
    # My own try
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []

        for i in range (0, len(grid)-2):
            answer.append([])
            for j in range (0, len(grid[0])-2):
                answer[i].append([])
                smallGrid = []
                for smallGridX in range(0, 3):
                    smallGrid.append([])
                    for smallGridY in range(0, 3):
                        smallGrid[smallGridX].append([])
                        smallGrid[smallGridX][smallGridY] = grid[i+smallGridX][j+smallGridY]
                answer[i][j] = self.findMax3x3(smallGrid)
        return answer

    def largestLocal2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        res = [[0 for j in range(n - 2)] for i in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                # evaluation = grid[i][j: j + 3] + grid[i + 1][j: j + 3] + grid[i + 2][j: j + 3]
                # This consitutues flattening three rows of the grid
                res[i][j] = max(grid[i][j: j + 3] + grid[i + 1][j: j + 3] + grid[i + 2][j: j + 3])

        return res

    # Find numbers with even number of digits
    def findDigits(self, num):
        result = 0
        while num != 0:
            num = num // 10
            result += 1
        return result

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evens = 0
        for num in nums:
            if self.findDigits(num) % 2 == 0:
                evens += 1
        return evens

    def findNumbers2(self, nums):
        count = 0
        for number in nums:
            # while number > 0:
            #     number = number // 10
            #     digits += 1
            digits = (math.log10(number) // 1) + 1
            if digits % 2 == 0:
                count += 1
        return count

    def findNumbers3(self, nums):
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedSquares = [num*num for num in nums]
        sortedSquares.sort()
        return sortedSquares

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

    print(solution.canConstruct("cfadfeiedidcdedhhijbficadgfecjiibgdbd\
    eigcabegifjjabefejiggacbbgfbdjhejjaddjbdhdgagigdbjcjhecfgfcjdgdgbce\
    fgejjhicjdhhaciabhgaeiecbgcifbgcjcbiegcacbjjgbbgjbaeffahdfffiaaefcdi\
    cbeafbgghbjeddhdbgdcdafacaiafhchfdgegecajfbefgdjcefdiefijfdjbdjiecegc\
    adefcbhcihgibbghdifjigfahjhfdaccacicffjchijhdaehgdbaffdcjgiafdiegjaibj\
    hbdaceddbhccgbbfibcfhcbhggjgchj", "jeibchbhacgefabbciecceiacdifigjfd\
    gjhbagejbbbdbccjbecdhighfhhdifibjbbjcegchdfbbiffidhhcchdjececjadggbcf\
    gdhadbegfdgcdjcabcaijjihfabaaaahghccjjehihihbhgfdhdacdhjcggbchijgcbbbe\
    bcbbgibbdfchfdddiefifgcfebajgdbgfdeajbdcigghaidaeiaibfabcbbjbficgcaeieh\
    igaigfaegibjhicfddjefcgffefhdijgejfjfjdggibdfehhfgjchfaejheaadeebchbh\
    iacjcceieiiabcaaggfffdjghhjaiigjchbchgachjhgibgfeccdehadjafiheajecjiga\
    becjgceiahcagebiabiaijcgaeddgejiiihggfgiddhabafijbhdjcfgedgcidhhacfdbeh\
    behbajebjebcajdfccfejfgfcdabdjgajhcacdjdjdcfajcdaabbcbjjjddbihfbeccfhggj\
    eifejfgbgaahccjaeefigdeiaadfhgeccgjfjfgegbfbjagbahhebejgffiejffdfjdefijdg\
    ejgbbcebihhhcbiehejcgefddeeeeggdegggjccifacbjedhdgdihbbbdjeghhhjhfeibhehdj\
    hdadbfbhcfcdjjeefcachgdgfjijebf"))

    print(solution.canConstruct("aa", "aa"))

    print(solution.canConstruct2("aa", "aa"))

    print(solution.canConstruct2("aa", "aaa"))

    print(solution.canConstruct2("aaa", "aa"))

    print(solution.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))

    print(solution.largestLocal2([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))

    print(solution.findNumbers([120,12,4122,123,1234,12,124]))

    print(solution.findNumbers2([120,12,4122,123,1234,12,124]))

    print(solution.findNumbers3([120, 12, 4122, 123, 1234, 12, 124]))

if __name__ == "__main__":
    main()
