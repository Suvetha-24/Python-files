name=['GILL', 'ABI','ANU','SANJAY','JOHN']
MARKS=[[20,65,40],[30,55,80],[80,60,50],[90,30,60],[50,76,50]]
for i in range(5):
    per= sum(MARKS[i])//3
    if(per>90):
        grade="S"
    elif(per>60 and per>90):
        grade="A"
    elif(per<40 and per<60):
        grade="B"
    else:
        grade="F"
    print("{},{},{}%-grade {}".format(i+1,name[i],per,grade))
        