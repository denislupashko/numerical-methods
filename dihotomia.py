def func( x):
    return (x**5+x**2-5)
def find( x0,  x1, eps):
    left = x0
    right = x1
    iter = 0
    print("x0 = ", x0, " x1 = ", x1, " ")
    while abs(func(left)) > eps or func(right) > eps:
        x = (left + right ) / 2.
        f = func(x)
        if (f > 0):
            right = x
        else:
            left = x
        iter += 1
    
    print(iter, "iterations")
    return x
eps = 0.0001
x0 = 0
x1 = 10
print("Dihotomia: ", find(x0, x1, eps)) 

    
    