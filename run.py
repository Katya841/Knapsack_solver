import knapsack_mip



filename_in, filename_out = "", ""

filename_in = input("Enter the name of the input file:")
filename_out = input("Enter the name of the output file:")

N, b, a, c = knapsack_mip.read_test_filename(filename_in)
ans, best_cost, total_cost, total_weight = knapsack_mip.solve(N, b, a, c)

knapsack_mip.save_test_filename(filename_out, ans, best_cost, total_cost, total_weight, N)
