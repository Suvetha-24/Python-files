def sq():
    side=int(input("enter the side of sq:"))
    print("area of Square is", side*side)
def rect(l,b):
    print(" Area of rectangle" ,l*b)
def tri():
    base=int(input("enter the base of traingle:"))
    height=int(input("enter the height of traingle:"))
    return 0.5*base*height
def circ(r):
    
    return 3.14*r*r
  


print("______MENU_______")
print("1.square")
print("2.rectangle")
print("3.triangle")
print("4.circle")
ch=int(input("enter  the choice"))
if(ch==1):
    sq()
elif(ch==2):
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    rect(l,b)
elif(ch==3):
    x=tri()
    print("area of triangle is",x)
elif(ch==4):
    r=int(input(" the radius of the circle : "))
    y=circ(r)
    print("area of circle",y)
   
else:
    print("Shape not available")
  
    