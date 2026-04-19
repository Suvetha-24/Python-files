n = int(input("Enter a number: "))
max_digit=9
min_digit=1
while n>0:
    digit=n%10
    
    if digit > max_digit:
        max_digit=digit
    if digit < min_digit:
        min_digit=digit
    n = n//10
print("the maximum digit:",max_digit)
print("the minimum digit is:",min_digit)
