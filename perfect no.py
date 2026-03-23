n=int(input("Enter the number:"))
sump=0
for i in range(1,n):
    if (n%i ==0):
        sump=sump+i

if sump==n:
    print("it is a perfect Number:")
else:
    print("it is not aperfect Number:")