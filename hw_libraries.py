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

def validation(num):
    num=num.replace(" ","")
    if num.isdigit():
        return True
    return False
a=""
b=""
c=""
print("For function ax2+bx+c input a,b,c:")
while not validation(a):
    a=input("a = ")
a=int(a)
while not validation(b):
    b=input("b = ")
b=int(b)
while not validation(c):
    c=input("c = ")
c=int(c)
draw(a,b,c)