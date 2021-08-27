# Project Euler #254: Sums of Digit Factorials
import math

factorials = [math.factorial(i) for i in range(10)]


def functionsf(num):
    # Convert int into string, iterate through every digit in the string and store individually as elements of a list.
    # Iterate through the list, compute the factorial of each element and sum all of the.
    f = sum([factorials[k] for k in [int(a) for a in str(num)]])
    # Convert int into string, iterate through every digit in the string and store individually as elements of a list.
    # Iterate through the list and sum all of the elements together
    return sum([int(a) for a in str(f)])


def functiong(num):
    i = 1
    while True:
        if functionsf(i) == num:
            return i
        else:
            i += 1


def functionsg(num):
    return sum([int(a) for a in str(functiong(num))])


def finalfunction(nums):
    result = []
    for i in range(1, (int(nums[0]) + 1)):
        result.append(functionsg(i))
    return sum(result) % int(nums[1])


n = int(input())
query = []
for i in range(n):
    query = input().split()
    print(finalfunction(query))
