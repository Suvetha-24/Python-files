n = int(input("Enter number of packets: "))

arr = list(map(int, input("Enter packets: ").split()))

m = int(input("Enter number of children: "))

arr.sort()
min_diff = float('inf')

for i in range(n - m + 1):
    diff = arr[i + m - 1] - arr[i]
    min_diff = min(min_diff, diff)

print("Minimum difference:", min_diff)