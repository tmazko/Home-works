import matplotlib.pyplot as mp

def quadratic_fun(x,a,b,c):
    return a*x**2+b*x+c

x,y=[],[]

for i in range(-100,100):
    x.append(i)
    y.append(quadratic_fun(i,1,2,3))

mt.plot(x,y)
mt.show()
