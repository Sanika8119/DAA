import time

m = int(input("Enter capacity of knapsack: "))
n = int(input("Enter number of items: "))

start_time = time.time()

items = []

for i in range(n):
        profit = int(input(f"Enter profit for item {i+1}: "))
        weight = int(input(f"Enter weight for item {i+1}: "))
        items.append([profit, weight, profit / weight])

items.sort(reverse=True, key=lambda l: l[2])

remaining_capacity = m
knapsack = []
total_profit = 0

for i in items:
        if(i[1] <= remaining_capacity):
                knapsack.append(i)
                remaining_capacity -= i[1]
                total_profit += i[0]
        elif(remaining_capacity != 0):
                new_weight = remaining_capacity
                new_profit = (new_weight / i[1]) * i[0]
                knapsack.append([new_profit, new_weight, i[2]])
                remaining_capacity = 0
                total_profit += new_profit
                break

end_time = time.time()
print(end="")
print(f"Execution Time: {end_time-start_time}ms")
print(f"Total Profit: {total_profit}")
print(f"Included Items: {knapsack}")
