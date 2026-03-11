import random
a=random.randint(1,10)
b=random.randint(1,10)
name1=input("Enter player1: ")
name2=input("Enter player1: ")
s1=0
s2=0
g1=0
g2=0
print("palyer 1 trun !!!")
while(g1!=a):
    g1=int(input("enter the guess :"))
    s1=s1+1
print("player 2 turn !!!")
while(g2!=b):
    g2=int(input("enter the guess"))
    s2=s2+1
if(s1<s2):
    print("{} is winner" .format(name1))
elif(s2<s1):
    print("{} is winner" .format(name1))
else:
    print("draw")


