from mip import Model, xsum, maximize, BINARY, INTEGER, ProgressLog
import csv
from cut_generator import OddConstraintCutGenerator
import sys


def read_test_filename(file_name):
    a = []
    c = []
    N, b = 0, 0
    with open(file_name,"r") as f:
        cnt = 0
        while (line := f.readline().strip()):
            num1, num2 = (int(x) for x in line.split())
            if cnt == 0:
                N = num1
                b = num2
            else:
                a.append(num1)
                c.append(num2)
            cnt += 1
    return N, b, a, c 

def read_test(test_id):
    file_name = f"tests/test_{test_id}.txt"
    return read_test_filename(file_name)


def save_test_filename(filename_out, ans, best_cost, total_cost, total_weight, N):
     with open(filename_out,"w") as f:
        f.write(f"{best_cost} {sum(ans)} {total_cost} {total_weight}\n")
        for i in range(N):
            f.write(f"{ans[i]} ")

def save_test(test_id, ans, best_cost, total_cost, total_weight, N):
    filename_out = f"output/out_{test_id}.txt"
    save_test_filename(filename_out, ans, best_cost, total_cost, total_weight, N)


   
def solve(N, b, a, c):
  
    m = Model("Knapsack")
    # Disable logs 
    m.verbose = 0 
    
    m.max_seconds = 10
    x = [m.add_var(var_type=BINARY) for i in range(N)]
    y =  m.add_var(var_type=INTEGER)
    m.objective = maximize(xsum(c[i] * x[i] for i in range(N)))

    m += xsum(a[i] * x[i] for i in range(N)) <= b
    m.lazy_constrs_generator = OddConstraintCutGenerator()
    m.optimize()

   
    total_cost, total_weight = 0, 0
    ma = [v.x for v in x]
    ans = [0 for _ in range(N)]
    for idx, v in enumerate(x):
        if v.x >= 0.99:
            ans[idx] = 1
            total_cost += c[idx]
            total_weight += a[idx]
    
    return ans, m.objective_value, total_cost, total_weight


