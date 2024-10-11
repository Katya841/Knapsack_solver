import pytest 
import knapsack_mip

eps = 0.0001

def get_correct_ans(test_id):
    filename = f"answers/ans_{test_id}.txt"
    with open(filename, "r") as f:
        value = int(f.read().split()[0])
        return value

test_cases = [
    knapsack_mip.read_test(test_id) + (get_correct_ans(test_id),test_id) 
    for test_id in range(0, 17)
]

# Specify parameter names to match the values in test_cases
@pytest.mark.parametrize("N, b, a, c, total_cost_ans, test_id", test_cases)
def test_solver(N, b, a, c, total_cost_ans, test_id):
    ans, best_cost, total_cost, total_weight = knapsack_mip.solve(N, b, a, c)
    knapsack_mip.save_test(test_id, ans, best_cost, total_cost, total_weight, N)

    assert (total_cost_ans - total_cost) / total_cost_ans <= eps 
    assert sum(ans) % 2 == 1

