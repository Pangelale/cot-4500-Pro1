import math

def approximation_alg(x0, tol):
    iter = 0
    diff = x0
    x = x0
    
    print(f"{iter} : {x}")
    
    while(diff >= tol):
        iter += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter} : {x}")
        diff = abs(x - y)
    
    print(f"\nConvergence after {iter} iterations")

# Test Case for approximation algorithm
print("Approximation Algorithm:")
approximation_alg(1.5, .000001)

def bisection_method(left, right, tol):
    max_iter = 100
    i = 0
    while (abs(right - left) > tol and i < max_iter):
        i += 1
        mid = (left + right) / 2
        if (func(left) < 0 and func(mid) > 0) or (func(left) > 0 and func(mid) < 0):
            right = mid 
        else:
            left = mid
            
    return i

def func(x):
    return x**3 + 4*x**2 - 10

# Test Case for bisection
bisection_result = bisection_method(1, 2, 10 ** -3)
print("\nBisection Method:")
print(f"Necessary number of iterations: {bisection_result}\n")

def fixedpoint_iter(p0, tol, n0):
    i = 1
    while(i <= n0):
        p = p0 - p0*p0*p0 - 4*p0*p0 + 10
        
        if math.isnan(p):
            print(f"\nResult diverges")
            break
        
        print(f"{i} : {p}")
        
        if(abs(p - p0) < tol):
            print(f"Success after {i} iterations")
            break
            
        i += 1
        p0 = p 
        
    print(f"Failure after {i} iterations")
    
# Test Case for Fixed-Point Iter.
print("Fixed-Point Iteration:")
fixedpoint_iter(1.5, .000001, 50)

def function(x):
    return math.cos(x) - x

def derivative(x):
    return -math.sin(x) - 1

def newton_raphson(initial_approx, tol):
    prev = initial_approx
    max = 100
    i = 1

    print(f"0 : {prev}") # Prints iteration 0
    
    while(i <= max):
        if(derivative(prev) != 0):
            pnext = prev - (function(prev) / derivative(prev))
            print(f"{i} : {pnext}")
            if(abs(pnext - prev) < tol):
                return pnext
            
            prev = pnext
            i += 1
            
        else:
            print("Error: Division by zero")
        
    print("Error: Maximum iterations reached")

# Test Case for Newton Raphson 
print("\nNewton_Raphson Method: ")
newton_raphson(math.pi/4, 25 * 10**-17)
