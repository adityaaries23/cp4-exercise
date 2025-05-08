from datetime import datetime
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