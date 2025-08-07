# Task
# Given 2 sets of integers, m and n,
# print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

m = int(input().strip())
a = list(map(int, input().split()))
n = int(input().strip())
b = list(map(int, input().split()))

set_a = set(a)
set_b = set(b)

result = sorted(set_a.symmetric_difference(set_b))

for i in result:
    print(i)
