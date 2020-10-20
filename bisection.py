from decimal import Decimal


def bisection(func,a, b,eps=10**-10):
    if (func(a) * func(b) > 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    i=0
    while ((b - a) >= eps):
        i=i+1
        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (-eps<func(c) <eps):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print ("count : "+ str(i))
    return c


# def roots(f,g,factor,eps=0.001):
#     #f=function
#     #eps=epsilon
#     #factor=array of the segments
#     #g=the derivative function
#     root=[]
#
#     for i in range(len(factor)-1):
#         a=factor[i]
#         b=factor[i+1]
#
#
#         x=f(a)
#         y=f(b)
#         if -eps<x<eps:
#             root.append(a)
#
#         if x*y<0:
#             root.append(bisection(f,a,b,eps))
#
#         elif g(a)*g(b)<0 :
#
#             res=bisection(g, a, b, eps)
#             if -eps<f(res)<eps:
#                 root.append(res)
#
#     return root

import math
#print(bisection(lambda x:2*x,-0.5,0.2))
#li=roots(lambda x:x*x,lambda x:2*x,[-0.5,0,0.5])
#print(li)

#li=roots(lambda x:x*x*x+5,lambda x:3*x*x,[-2.3,-1.8,-1.3,-0.8,-0.3,0.2,0.7])
#print(li)

#li=roots(lambda x:x*x*x+2*x*x,lambda x:3*x*x+4*x,[-2.3,-1.8,-1.3,-0.8,-0.4,-0.3,0.2,0.7])
#print(li)

#li=roots(lambda x:math.sin(x),lambda x:math.cos(x),[-4,-3,-2,-1,0,1,2,3,4,5,6,7,8])
#print(li)


print(bisection(lambda x: x*x*x-x-1,1,2 ))