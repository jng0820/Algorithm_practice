def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2

        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return 1

    return 0


N = input()
N = int(N)
A = input().split()
A.sort()
M = input()
M = int(M)
number = input().split()

length = len(number)

for i in range(length):
    ans = binary_search(A, number[i])
    print(ans)
