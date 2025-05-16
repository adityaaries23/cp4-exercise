from datetime import datetime
from functools import reduce
from typing import List


def print_date():
    # 13025 Back to the Past (UVa)
    today = datetime(2013,5,29)
    formatted_date = today.strftime("%B %d, %Y %A")
    print(formatted_date)

def find_r2():
    # https://open.kattis.com/problems/carrots
    inp = input()
    ars = inp.split(sep=" ")
    r1 = int(ars[0])
    s = int(ars[1])

    print(2*s-r1)

def convert_temperature(self, celsius: float) -> List[float]:
    # https://leetcode.com/problems/convert-the-temperature/
    temp = [celsius + 273.15, celsius * 1.8 + 32.0]
    return temp

def farewell():
    # https://open.kattis.com/problems/thelastproblem
    name = input()
    print(f"Thank you, {name}, and farewell!")

def check_date():
    # https://open.kattis.com/problems/isithalloween
    month, day = input().split(sep=" ")
    print("yup" if (month == "DEC" and day == "25") or (month == "OCT" and day == "31") else "nope")


def check_sticker_laptop():
    # https://open.kattis.com/problems/laptopsticker
    wc, hc, ws, hs = map(int, input().split(sep=" "))
    print(1 if wc > ws + 1 and hc > hs + 1 else 0)


def moscow_dream():
    # https://open.kattis.com/problems/moscowdream
    a, b, c, n = map(int, input().split())

    print("YES" if 3 <= n <= a + b + c and a >= 1 and b >= 1 and c >= 1 else "NO")


def grading():
    # https://open.kattis.com/problems/grading
    thresholds = list(map(int, input().split(sep=" ")))
    exam_grade = int(input())

    grades = 'ABCDEF'
    for i, threshold in enumerate(thresholds):
        if exam_grade >= threshold:
            print(grades[i])
            return
    print('F')

def isSameAfterReversals(self, num: int) -> bool:
    # https://leetcode.com/problems/a-number-after-a-double-reversal/
    if num == 0 or num % 10 != 0:
        return True
    return False


def subtractProductAndSum(n: int) -> int:
    # https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
    total, product = 0, 1
    for digit in str(n):
        d = int(digit)
        total += d
        product *= d
    return product - total


def differenceOfSums(self, n: int, m: int) -> int:
    #https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
    a = [a for a in range(0, n + 1) if a % m != 0 ]
    b = [a for a in range(0, n + 1) if a % m == 0 ]
    return sum(a) - sum(b)

def averageValue(nums: List[int]) -> int:
    # https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
    divisible_nums = [num for num in nums if num % 6 == 0]
    return sum(divisible_nums) // len(divisible_nums) if divisible_nums else 0

def countEven(num: int) -> int:
    # https://leetcode.com/problems/count-integers-with-even-digit-sum/
    nums = 0
    for a in range(1, num + 1):
        t = sum([int(x) for x in str(a)])
        if t % 2 == 0:
            nums += 1
    return nums

def average(self, salary: List[int]) -> float:
    # https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
    maximum = max(salary)
    minimum = min(salary)
    return (sum(salary) - maximum - minimum) / (len(salary) - 2)


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    # https://leetcode.com/problems/transpose-matrix/
    return [*zip(*matrix)]

def distanceTraveled(mainTank: int, additionalTank: int) -> int:
    # https://leetcode.com/problems/total-distance-traveled/
    t = mainTank
    a = 0
    for i in range(1, additionalTank+1):
        if t < 5:
            break
        t -= 4
        a += 1
    return (a + mainTank)*10

def reverse(x: int) -> int:
    # https://leetcode.com/problems/reverse-integer/
    s = str(x)
    sign = -1 if s[0] == '-' else 1

    # Remove sign for processing if needed
    s = s[1:] if sign == -1 else s

    # Reverse and convert back to integer with sign
    reversed_num = sign * int(s[::-1])

    # Check 32-bit integer bounds
    return reversed_num if -2 ** 31 <= reversed_num <= 2 ** 31 - 1 else 0

def lengthOfLastWord(s: str) -> int:
    # https://leetcode.com/problems/length-of-last-word/
    s = s.strip()
    split = s.split(sep=" ")
    return len(split[-1]) if split else 0

def decodeMessage(key: str, message: str) -> str:
    # https://leetcode.com/problems/decode-the-message/
    unique_chars = dict.fromkeys(key.replace(" ", ""))
    chars = {}

    for i,k in enumerate(unique_chars):
        if  i < 26:
            chars[k] = chr(97 + i)

    result = ''
    for ch in message:
        if ch.isalpha():
            result = result + chars.get(ch.lower())
        else:
            result += ch

    return result

def interpret(command: str) -> str:
    #https://leetcode.com/problems/goal-parser-interpretation/
    return command.replace("(al)","al").replace("()","o").replace("G","G")


def defangIPaddr(address: str) -> str:
    # https://leetcode.com/problems/defanging-an-ip-address/
    return address.replace(".", "[.]")

def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    # https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
    sentence = sentence.split(sep=" ")
    for i, word in enumerate(sentence):
        if word.startswith(searchWord):
            return i + 1
    return -1

def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    # https://leetcode.com/problems/check-if-word-equals-summation-of-two-words
    var1 = int("".join([str(ord(a) - 97) for a in firstWord]))
    var2 = int("".join([str(ord(a) - 97) for a in secondWord]))
    var3 = int("".join([str(ord(a) - 97) for a in targetWord]))

    return var1 + var2 == var3

def getLucky(s: str, k: int) -> int:
    # https://leetcode.com/problems/sum-of-digits-of-string-after-convert
    value = "".join(str(ord(char) - 96) for char in s)

    # Apply k transformations
    for _ in range(k):
        value = str(sum(int(digit) for digit in value))

    return int(value)

def bestHand(ranks: List[int], suits: List[str]) -> str:
    # https://leetcode.com/problems/best-poker-hand/
    if len(set(suits)) == 1:
        return "Flush"

    a = [ranks.count(a) for a in ranks]
    if 3 in a or 4 in a: return "Three of a Kind"
    if 2 in a: return "Pair"

    return "High Card"

def judgeCircle(moves: str) -> bool:
    # https://leetcode.com/problems/robot-return-to-origin
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

def finalPositionOfSnake(n: int, commands: List[str]) -> int:
    # https://leetcode.com/problems/snake-in-matrix
    return  (commands.count("DOWN") * n) - (commands.count("UP") * n) + (commands.count("RIGHT") * 1) - (commands.count("LEFT") * 1)

def dayOfYear(date: str) -> int:
    # https://leetcode.com/problems/day-of-the-year/
    datetime_object = datetime.strptime(date, '%Y-%m-%d')
    return datetime_object.timetuple().tm_yday

def romanToInt(s: str) -> int:
    # https://leetcode.com/problems/roman-to-integer/
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    last_val = 0

    for i in s[::-1]:
        if roman[i] >= last_val:
            int_val += roman[i]
            last_val = roman[i]
        else:
            int_val = int_val - roman[i]
    #
    # for i in range(len(s)):
    #     if i > 0 and roman[s[i]] > roman[s[i - 1]]:
    #         int_val += roman[s[i]] - 2 * roman[s[i - 1]]
    #     else:
    #         int_val += roman[s[i]]
    #     print(int_val)
    return int_val

def detectCapitalUse(word: str) -> bool:
    # https://leetcode.com/problems/detect-capital/description/
    return word.isupper() or word.islower() or word.istitle()

def findFinalValue(nums: List[int], original: int) -> int:
    # https://leetcode.com/problems/keep-multiplying-found-values-by-two
    while original in nums:
        original = original * 2
    return original

def scoreOfString(s: str) -> int:
    # https://leetcode.com/problems/score-of-a-string/
    if len(s) == 1:
        return ord(s)
    
    return sum(abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1))

def minOperations(nums: List[int], k: int) -> int:
    # https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
    return sum(nums) % k

def isPalindrome(x: int) -> bool:
    # https://leetcode.com/problems/palindrome-number/
    return str(x) == str(x)[::-1]

def arraySign(nums: List[int]) -> int:
    # https://leetcode.com/problems/sign-of-the-product-of-an-array/
    a = reduce(lambda x, y: x * y, nums)
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def maximumCount(nums: List[int]) -> int:
    # https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-intege
    a = len([i for i in nums if i >= 0])
    b = len([i for i in nums if i < 0])
    return max(a,b)

def sumOfMultiples(n: int) -> int:
    # https://leetcode.com/problems/sum-multiples/
    return sum([i for i in range(1,n+1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0])

def sumOfSquares(nums: List[int]) -> int:
    # https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
    return sum([n * n for i,n in enumerate(nums) if len(nums) % (i+1) == 0])

def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    # https://leetcode.com/problems/number-of-employees-who-met-the-target/
    return len([i for i in hours if i >= target])

def returnToBoundaryCount(nums: List[int]) -> int:
    # https://leetcode.com/problems/ant-on-the-boundary/
    count = 0
    a = 0
    for i in nums:
        a += i
        if a == 0:
            count += 1
    return count

def maxOperations(nums: List[int]) -> int:
    # https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/description/
    target_sum = nums[0] + nums[1]
    count = 0

    for i in range(0, len(nums)-1, 2):  # Skip by 2 instead of checking i % 2
        current_sum = nums[i] + nums[i+1]
        if current_sum != target_sum:
            break
        count += 1

    return count

def stableMountains(height: List[int], threshold: int) -> List[int]:
    # https://leetcode.com/problems/find-indices-of-stable-mountains/
    return [i for i in range(1, len(height)) if height[i - 1] > threshold]
