def newton(f, d, a, b, eps=0.0001):
    #f=function
    #d=derived

    if f(a)*f(b)>0:
        return

    xr=(a+b)/2
    xr1=xr+0.001
    count=0
    while abs(xr-xr1)>eps:
        count = count + 1
        xr=xr1
        xr1=xr-f(xr)/d(xr)
    print(count, "iteration to find root (",xr, ", 0 )")
    return

#---------------------------------------------------------------

#def meitar()
for i in range(-5,5):
    newton(lambda x: x**2-6, lambda x:2*x,i,i+1)
