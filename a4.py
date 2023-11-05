import time

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] 
    for _ in range(n + 1)]
    
    # Build the dynamic programming table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    selected_items.reverse()

    # Display the dynamic programming table
    print("Dynamic Programming Table:")
    for row in dp:
        print(row)

    # Display the selected items
    print("\nSelected items to fill the knapsack:")
    for item in selected_items:
        print(f"Item {item + 1} (Weight: {weights[item]}, Value: {values[item]})")

if __name__ == "__main__":
    # Input example
    capacity = int(input("Enter the capacity of knapsack: "))
    n = int(input("Enter number of items: "))
    start_time = time.time()
    items = []
    for i in range(n):
        values = int(input(f"Enter profit for item {i+1}: "))
        weights = int(input(f"Enter weight for item {i+1}: "))
        items.append([values, weights, values / weights])

    knapsack_dynamic_programming(weights, values, capacity)
    end_time = time.time()