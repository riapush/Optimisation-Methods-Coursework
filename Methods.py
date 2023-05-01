from scipy.optimize import minimize

def objective(x):
    a, b, c, d = x
    return -(a * b + 2*c * d)

def constraint1(x):
    return h - x[2] - x[3]

def constraint2(x):
    return x[0] - x[2]

def constraint3(x):
    return h - x[0]

def constraint4(x):
    return x[1] - x[3]

def constraint5(x):
    return h - x[1]

h = 10 # задаем ширину канала
x0 = [1, 1, 0.5, 0.5] # начальное приближение

# задаем ограничения
cons = [{'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2},
        {'type': 'ineq', 'fun': constraint3},
        {'type': 'ineq', 'fun': constraint4},
        {'type': 'ineq', 'fun': constraint5}]

# решаем задачу оптимизации
sol = minimize(objective, x0, method='SLSQP', constraints=cons)

# выводим оптимальные параметры
print(sol.x)
