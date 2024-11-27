import matplotlib.pyplot as mt
import numpy as np

def quadratic_fun(x, a, b, c):
    return a * x**2 + b * x + c

def log2(x):
    return np.log2(x)

def draw(a,b,c):
    x1 = np.linspace(-10, 10, 200)
    y1 = quadratic_fun(x1, a, b, -c)

    x2 = np.logspace(-10, 1, 200)
    y2 = log2(x2)

    mt.plot(x1, y1, label="Quadratic Function", color="blue")
    mt.plot(x2, y2, label="Logarithmic Function", color="red", linestyle="--")

    mt.ylim(-10, 20)
    mt.legend()
    mt.show()


print("For function ax2+bx+c input a,b,c:")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
draw(a,b,c)