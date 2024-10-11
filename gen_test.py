import random


cnt_tests = 15

def generate_test_case(min_n, max_n, max_weight, max_value,):
    n = random.randint(min_n, max_n)
    weights = [random.randint(1, max_weight) for _ in range(n)]
    values = [random.randint(1, max_value) for _ in range(n)]
    sum_weights = sum(weights)
    W = random.randint(int(0.3 * sum_weights), int(0.5 * sum_weights))
    return n, W, weights, values

def save_test_case(id_test, n, W, weights, values):
    filename = f"test_{id_test}.txt"
    f = open(filename, "w")
    f.write(f"{n} {W}\n")
    for i in range(n):
        f.write(f"{weights[i]} {values[i]}\n")
    return
def generate_test_cases(cnt_tests):
    for i in range(1, cnt_tests + 1):
        n, W, weights, values = generate_test_case(200, 1000, 700, 1000)
        save_test_case(i, n, W, weights, values)
    