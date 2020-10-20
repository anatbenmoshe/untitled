from sympy.physics.quantum.circuitplot import matplotlib
#הדפסה בצורה סימבולית של הנגזרת
import inline as inline
import sympy as sp
import numpy as np
x =sp.symbols('x')
my_f=x**3+2*x+5
print(my_f)
print(sp.diff(my_f,x))
my_f1=sp.diff(my_f,x)
d1=sp.diff(my_f1)
print(d1)


# #חישוב הנגזרת בערך מסויים ( במקרה שלנו בערך 2.0 )
# from scipy.misc import derivative
# def f(x):
#     return x**3-4*x**2-1
# def d(x):
#     return derivative(f,x)
#
# print('f(x)=',f(2.0))
# print('d(x)=',d(2.0))

#
# #הדפסת הפונקציה
# import matplotlib.pyplot as plt
# import numpy as np
# y=np.linspace(-2,5)
# plt.show(plt.plot(y,f(y)))


