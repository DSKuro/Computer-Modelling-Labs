from pulp import LpVariable, LpProblem, LpMaximize, value
from cvxopt.modeling import variable, op
import time

def calculate_goal_function() -> tuple:
    start = time.time()
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    x4 = LpVariable("x4", lowBound=0)
    problem = LpProblem("maximize-profit", LpMaximize)
    problem += 5*x1 + 8*x2 + 7*x3 + 9*x4, "Goal Function"
    problem += 0.6*x1 + 0.8*x2 + 0.6*x3 + 0.4*x4 <= 840, "1"
    problem += (0.1*x1 + 0.2*x2 + 0.4*x3 + 0.1*x4 <= 180, "2")
    problem.solve()
    print("result")
    variables = {}
    for variable in problem.variables():
        print(variable.name, "=", variable.varValue)
        variables[variable.name] = variable.varValue

    print("Profit: ", value(problem.objective))
    stop = time.time()
    print("Time: ", stop - start)
    return variables, value(problem.objective)

def calculate_cvxopt():
    start = time.time()
    x = variable(4, 'x')
    problem = -(5*x[0] + 8*x[1] + 7*x[2] + 9*x[3]) #goal
    mass1 = (0.6*x[0] + 0.8*x[1] + 0.6*x[2] + 0.4*x[3] <= 840)
    mass2 = (0.1*x[0] + 0.2*x[1] + 0.4*x[2] + 0.1*x[3] <= 180)
    x_non_negative = (x >= 0)
    z = op(problem, [mass1, mass2, x_non_negative])
    z.solve(solver="glpk")
    z.status

    print("Profit:")
    print(abs(z.objective.value()[0]))
    print("Result:")
    print(x.value)
    stop = time.time()
    print("Time:")
    print(stop - start)

if __name__ == "__main__":
    calculate_cvxopt()