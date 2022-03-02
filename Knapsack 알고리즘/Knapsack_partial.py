def get_optimal_value(capacity, weights, values, name):
    size = len(weights)
    vpw = [(values[i] / weights[i], weights[i], name[i]) for i in range(size)]
    densities = sorted(vpw, reverse=True)
    finalValue = 0
    for i, v in enumerate(densities):
        a = min(capacity, densities[i][1])
        finalValue += a * densities[i][0]
        print(densities[i][2], a, "gram is taken")
        capacity -= a
    print('\n')
    return finalValue


capacity = 200
values = [500000, 470000, 430000, 390000, 360000,
          340000, 280000, 265500, 200000, 180000]
weights = [50, 48, 35, 34, 30, 28, 26, 24, 20, 19]
names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
opt_value = get_optimal_value(capacity, weights, values, names)

print("Value of the knapsack is", opt_value)
