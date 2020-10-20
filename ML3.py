import unit10.b_utils as u10
import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d
import numpy as np

random.seed(1)
rnd = random.randrange


def ex0_test():
    X, Y = u10.load_dataB1W3Ex1()
    plt.plot(X, Y, 'b.')
    plt.show()


def cost_f1(xi, yi, a, b):
    return (a * xi + b - yi) ** 2


def ex1_wrap(rep, cost_f):
    X, Y = u10.load_dataB1W3Ex1()
    count = len(X)
    rng = range(0, count)
    plt.plot(X, Y, 'b.')
    line = [min(X), max(X)]
    diff = (0, 0, None) #a, b, cost
    i = 0
    while i < rep:
        a, b = rnd(-20, 20), rnd(-20, 20)
        liney = [(val * a + b) for val in line]
        plt.plot(line,  liney)

        diffvals = [cost_f(X[j], Y[j], a, b) for j in rng]
        cost = sum(diffvals) / count
        if not diff[2] or cost < diff[2]:
            diff = (a, b, cost)
        i += 1

    print(diff)
    plt.show()


def ex1():
    ex1_wrap(10, cost_f1)


def ex2_test():
    X, Y = u10.load_dataB1W3Ex2()
    print(X, Y)
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(X[0], X[1], Y)
    plt.show()


# y(i)^
def fex2a(x1, x2, a, b, c, d):
    return a * x1 ** 2 + b * x1 * x2 + c * x2 ** 2 + d


def fex2(x1, x2, a, b, c, d, y):
    return (fex2a(x1, x2, a, b, c, d) - y) ** 2


def y_function(diff, x1, x2):
    rows = len(x1)
    cols = len(x1[0])
    rng = range(0, cols)
    i = 0
    res = []
    while i < rows:
        y_hat = [fex2a(x1[i][j], x2[i][j], diff[0], diff[1], diff[2], diff[3]) for j in rng]
        res.append(y_hat)
        i += 1

    return np.array(res)


def ex2(rep):
    X, Y = u10.load_dataB1W3Ex2()
    count = len(Y)
    rng = range(0, count)
    diff = [0, 0, 0, 0, None] #a, b, c, d, cost
    i = 0
    while i < rep:
        a, b, c, d = rnd(-10, 10), rnd(-10, 10), rnd(-10, 10), rnd(-10, 10)
        diffvals = [fex2(X[0][j], X[1][j], a, b, c, d, Y[j]) for j in rng]
        cost = sum(diffvals) / count
        if not diff[4] or cost < diff[4]:
            diff[0], diff[1], diff[2], diff[3], diff[4] = a, b, c, d, cost
        i += 1

    #print(diff)

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    X1, X2 = np.meshgrid(np.linspace(-15, 15, 30), np.linspace(-15, 15, 30))
    Ywire = y_function(diff, X1, X2)
    ax.plot_wireframe(X1, X2, Ywire, color='orange')
    ax.scatter3D(X[0], X[1], Y)
    plt.show()


def ex1_challenge(w, low, high):
    x, y = u10.load_dataB1W3Ex1Challenge()
    count = len(x)
    rngp = range(low, high + 1)
    # in case there is no match between number of parameters and low-high range
    c = min(high - low + 1, len(w))
    rng = range(0, c)
    i = 0
    cost = 0
    while i < count:
        xi = x[i]
        err = [xi ** rngp[j] * w[j] for j in rng]
        s = sum(err)
        cost += (s - y[i]) ** 2
        i += 1

    print(cost / count)


def calc_h(x, y, a, b):
    h = abs(-a * x + y - b) / ((a ** 2 + 1) ** 0.5)
    return h


def cost_f2(xi, yi, a, b):
    h = abs(-a * xi + yi - b) / ((a ** 2 + 1) ** 0.5)
    return h ** 2


def ex2_challenge():
    ex1_wrap(10, cost_f2)


ex2_challenge()
#ex1_challenge([-120000, 150000, -31200, 1320, -150, 31.2, -1.2], -1, 5)
#ex1()
#ex2(1000)