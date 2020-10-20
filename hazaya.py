def calcFunc (a):
    return a*a*a-a-1

a=1
b=2
count=0
flag=0
while (b-a)>10**-10:
    count=count+1
    c=(a+b)/2.
    if(calcFunc(c)==0):
        print(c)
        print(count)
        flag=1
    if(calcFunc(a)*calcFunc(c)>0):
        a=c
    else:
        b=c
if(flag==0):
    print(c)
    print(count)
