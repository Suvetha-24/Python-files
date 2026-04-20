n = int(input("Enter number of books: "))

arr = list(map(int, input("Enter days late: ").split()))

k = int(input("Allowed days: "))

fine = 0

for days in arr:
    if days > k:
        fine += days - k

print("Total fine:", fine)