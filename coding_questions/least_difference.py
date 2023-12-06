# 1. Input [3,9,50,15,99,7,98,65]
# Output = [98,99] Least diff among elements
def find_min_difference(arr):
    arr.sort()
    print(arr)

    min_diff = float('inf')
    # first_num, second_num = 0, 0

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]

        if diff < min_diff:
            min_diff = diff
            # first_num, second_num = arr[i], arr[i + 1]

    print("Min Difference:", min_diff)
    # print("Min Difference numbers:", first _num, "and", second_num)


arr = [3, 9, 50, 15, 99, 7, 98, 65]
find_min_difference(arr)
