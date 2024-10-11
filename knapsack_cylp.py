from mip import Model, xsum, maximize, BINARY, INTEGER, ProgressLog
import csv
from cut_generator import OddConstraintCutGenerator
import sys


def read_test(test_id):
    file_name = f"tests/test_{test_id}.txt"
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

def save_test(test_id, ans, best_cost, total_cost, total_weight, N):

    filename_out = f"output/out_{test_id}.txt"

    with open(filename_out,"w") as f:
        f.write(f"{best_cost} {sum(ans)} {total_cost} {total_weight}\n")
        for i in range(N):
            f.write(f"{ans[i]} ")
    


def solve(N, b, a, c):
  
    print(N, ' ', b)
   
    #for i in range(N):
    #   print(a[i], c[i])
    #"""
    m = Model("Knapsack")
    m.verbose = 1
    
    m.max_seconds = 10
    x = [m.add_var(var_type=BINARY) for i in range(N)]
    y =  m.add_var(var_type=INTEGER)
    m.objective = maximize(xsum(c[i] * x[i] for i in range(N)))

    m += xsum(a[i] * x[i] for i in range(N)) <= b
    #m += y >= 0
    #m += xsum(x[i] for i in range(N) ) == 2 * y + 1
    
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
    #print('WORK:',m.lazy_constrs_generator.calls)
    
    return ans, m.objective_value, total_cost, total_weight


"""
test_id = int(input())
print(f"Номер теста: {test_id}")

N, b, a, c = read_test(test_id)

ans, best_cost, total_cost, total_weight = solve(N, b, a, c)

save_test(test_id, ans, best_cost, total_cost, total_weight, N)
"""
