def funcVal(f,x):
    return f(x)

for i in range(6):
    print(funcVal(lambda x: x*x*x-x-1,i))