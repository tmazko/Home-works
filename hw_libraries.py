import matplotlib.pyplot as mt
import numpy as np

def quadratic_fun(x, a, b, c):
    return a * x**2 + b * x + c

def log2(x):
    return np.log2(x)

x1 = np.linspace(-10, 10, 200)
y1 = quadratic_fun(x1, 5, 2, -5)

x2 = np.logspace(-10, 1, 200)
y2 = log2(x2)

mt.plot(x1, y1, label="Quadratic Function", color="blue")
mt.plot(x2, y2, label="Logarithmic Function", color="red", linestyle="--")

mt.ylim(-10, 20)
mt.legend()
mt.show()
