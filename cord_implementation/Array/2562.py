arr = [int(input()) for _ in range(9)]
arr2 = sorted(arr)
maxVal = arr2[-1]
if maxVal in arr:
    print(maxVal)
    print(arr.index(maxVal)+1)