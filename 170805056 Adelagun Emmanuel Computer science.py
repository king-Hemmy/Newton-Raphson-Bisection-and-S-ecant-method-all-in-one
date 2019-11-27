from timeit import default_timer as timer

def newton_raphson(func, dfunc, x0, tol, iter_max):
    begin = timer()
    if func(x0) * dfunc(x0) > 0:
        print("Incorrect initial guess")
        return
        
    abs_err= 0
    x = 0
    
    for n in range(1, iter_max+1):
        fx0 = func(x0)
        dfx0 = dfunc(x0)
        if dfx0 is not 0:
            x = x0 - (fx0/dfx0)
        
        if x is not 0:
            abs_err= abs((x - x0)/x * 100)
        
        x0 = x
        
        print("n: {0} \t x0: {1:8f} \t x: {2:8f} \t ea: {3:8f}".format(n, x0, x, abs(abs_err)))
        if abs_err and abs_err<= tol:
            break 
    end = timer()
    print("x was gotten in {}s".format(end - begin))

def secant(func, a, b, err, imax):
    begin = timer()
    if func(a) - func(b) == 0:
        print("Invalid initial guesses")
        return

    for n in range(1, imax+1):
        if (func(b) - func(a)) == 0:
            break
        else:
            x = b - (b - a) * func(b) / ( func(b) - func(a) )
            abs_err = (x - b)/x

        print("n: {0} \t x: {1:8f} \t a: {2:8f} \t b: {3:8f}  \t ea: {4:8f}".format(n, x, a, b, abs(abs_err)))
        a = b
        b = x

    end = timer()
    print("x was gotten in {}s".format(end - begin))

def bisection(func, a, b, err, imax):
    begin = timer()
    funcA = func(a)
    funcB = func(b)

    if funcA * funcB > 0:
        print("Initial Guesses are wrong: ")
        return
    
    for i in range(1, imax+1):
        x = (a + b) / 2

        if func(a) * func(x) < 0:
            abs_err = abs((x - b) / x)
            b = x
        else:
            abs_err = abs((x - a) / x)
            a = x
        
        if abs_e < err:
            break
        
        print("n: {0} \t a: {1:8f} \t b: {2:8f} \t x: {3:8f} \t abs_e: {4:8f}".format(i, a, b, x, abs(abs_err)))
        

    end = timer()
    print("x was gotten in {}s".format(end - begin))



option = eval(input("Select a method: \n 1 - Newton Raphson \t 2 - Bisection \t 3 - Secant: "))
order = eval(input("The polynomial is of order: "))

inputs = []

differential = []

for i in range(order, -1, -1):
    val = eval(input("The coefficient of x^" + str(i) + " is : "))
    inputs.append(val)

def func(x): 
    output = 0
    for i in range(0, order+1):
        output += inputs[i]*x**abs(order - i) 
    return output

def dfunc(x): 
    power = order
    for i in inputs:
        differential.append(i * (power))
        power = power - 1

    output = 0
    for i in range(0, order):
        output += differential[i]*x**abs(order - i) 
    return output

if option is 1:
    a = eval(input("Guess: "))
    it_max = eval(input("Maximum number of iterations: "))
    err = eval(input("Tolerable error: "))
    newton_raphson(func, dfunc, a, err, it_max)

elif option is 2:
    a = eval(input("First guess: "))
    b = eval(input("Second guess: "))
    it_max = eval(input("Maximum number of iterations: "))
    err = eval(input("Tolerable error: "))
    bisection(func, a, b, err, it_max)

elif option is 3:
    a = eval(input("First guess : "))
    b = eval(input("Second guess: "))
    it_max = eval(input("Maximum number of iterations: "))
    err = eval(input("Tolerable error: "))
    secant(func, a, b, err, it_max)
    