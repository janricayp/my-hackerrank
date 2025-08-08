# HackerRank Problem collections.Counter()
# Link: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true


from collections import Counter

x = int(input())
shoes_sizes = list(map(int, input().split()))
store = Counter(shoes_sizes)
n = int(input())
earnings = 0
for _ in range(n):
    size, price = (map(int, input().split()))
    if store[size] > 0:
        earnings += price
        store[size] -= 1
print(earnings)
