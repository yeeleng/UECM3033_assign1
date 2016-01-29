import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.sin(x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,2,4,9,8,1,5,0,2], [1,2,3,4,5,6,7,8,9,0], 
                   [2,3,4.5,5,6,7,8,9,0,0], [3,4,25,6,7,8,9,1,1,2.3],
                   [4,5,6,7,8,9,0,1,2,3], [5.5,6,7,8,9,20,1,2,3,4],
                   [6,7,8,9,0,1,2,3,4,5], [7,8,9,0,1,2,3,4,5,6],
                   [8,9,0,1,2,3,4,5,6,7], [9,10,1,2,3,4,5,6,7,8]] )
    b = np.array([9,8,7,6,5,4,3,2,1,5])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1204756
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())