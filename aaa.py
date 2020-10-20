import numpy

a=(3*(27/13))+(2*(51/26))-(5*(16/13))
print (a)
epsilon=numpy.finfo(float).eps
print(epsilon)
print((3*27/13+2*51/26-5*16/13)-epsilon)

#print(b)