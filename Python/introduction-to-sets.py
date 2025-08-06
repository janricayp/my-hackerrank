# Complete the average function in the editor below.

# average has the following parameters:

# int arr: an array of integers
# Returns

# float: the resulting float value rounded to 3 places after the decimal

def average(array):
    # your code goes here
    sets = set(array)
    total = sum(sets)
    size = len(sets)
    avg = total / size
    return f"{avg:.3f}"


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
