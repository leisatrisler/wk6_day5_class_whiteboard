# Write a Python program to add the digits of a positive integer 
# repeatedly until the result has a single digit.


# EX
# Input:
n1=48
# 4+8=12
# 1+2=3
# Output:
# 3

# Input
n2=59
# Output
# 5
def solution(n):
    if len(str(n)) == 1:
        return n
    return solution(sum(map(int,[*str(n)])))