def supply_chain_optimization(cost_matrix):
    n_warehouses = len(cost_matrix[0])
    n_suppliers = len(cost_matrix)
    
    # Initialize a DP table
    dp = [[float('inf')] * n_warehouses for _ in range(n_suppliers)]
    
    # Base case: first warehouse costs
    for i in range(n_suppliers):
        dp[i][0] = cost_matrix[i][0]
    
    # Fill the DP table
    for j in range(1, n_warehouses):
        for i in range(n_suppliers):
            dp[i][j] = min(dp[k][j-1] + cost_matrix[i][j] for k in range(n_suppliers))
    
    # Find the minimum cost for the last warehouse
    return min(dp[i][-1] for i in range(n_suppliers))

# Example cost matrix (suppliers x warehouses)
cost_matrix = [
    [4, 2, 5],
    [3, 7, 4],
    [6, 3, 8]
]

print("Minimum Supply Chain Cost:", supply_chain_optimization(cost_matrix))
m
