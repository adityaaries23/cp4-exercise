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