import numpy as np
import random as random
from scipy.optimize import minimize

#Defines the function we are minimizing
def function(x):
    return (x[0]-x[1])**2+(x[1]+x[2]-2)**2+(x[3]-1)**2+(x[4]-1)**2

#Creates a list of 5 random initial guesses
initial_guess=[]
for i in range(5):
    rando=random.randint(-10,10)
    initial_guess.append(rando)

#sets the constraints
constraints = [
    {'type': 'eq', 'fun': lambda x: x[0] + 3*x[1]},
    {'type': 'eq', 'fun': lambda x: x[2] + x[3] - 2*x[4]},
    {'type': 'eq', 'fun': lambda x: x[1] - x[4]}
]

#Sets the range of x values we can use
bounds= []
for i in range(5):
    bound=(-10,10)
    bounds.append(bound)

#minimizes the function using SLSQP given the initial guesses, constraints, and bounds
result=minimize(function, np.array(initial_guess),method='SLSQP', constraints=constraints, bounds=bounds)


print(f"The initial guesses were {initial_guess}")
print(f"The optimized variables were determined to be {result.x}")
print(f"The minimum value of the function is {result.fun}")