def bisectionMethod(function , a , b ):
    faInterval = f(a)
    fbInterval = f(b)

    if faInterval * fbInterval > 0:
        print("f(a) and f(b) Must Be Different Signs To Find The root ")
        return None

    for _ in range(100): 
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            return c
        if faInterval * fc > 0:
            a = c
            faInterval = fc
        if fbInterval * fc > 0:
            b = c
            fbInterval = fc

    return c


func = lambda x: x**2 - 2*x -1

a = 2
b = -2
print(f"From : {a}")
print(f"To : {b}")
root= bisectionMethod(func, a, b)

print(f"Solution   :  {root}")
print("--------------------")
a = 1
b = 4

print(f"From : {a}")
print(f"To : {b}")

root= bisectionMethod(func, a, b)

print(f"Solution   :  {root}")
