name=['GILL', 'ABI','ANU','SANJAY','JOHN']
age=[22,14,33,56,89]
place=['chennai','ooty','theni','pondy','madurai']
res=list(zip(age,name,place))
res2= sorted(res)
for i in range(5):
    print("{},age is {},lives in {}".format(i+1,res2[i][1],res2[i][0],res[i][2]))