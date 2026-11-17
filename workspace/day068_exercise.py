from math import cos
from scipy.optimize import minimize

def quantum_model(theta):
    return cos(theta[0])

def loss(theta):
    prediction = quantum_model(theta)
    return (prediction - 0.25) ** 2

result = minimize(loss, x0=[0.5])
print(result.x, result.fun)
