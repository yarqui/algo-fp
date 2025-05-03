from typing import Dict, List

items: Dict[str, Dict[str, int]] = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> List[str]:
    # Sort by calories/cost ratio
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_cost = 0
    selected = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]

    return selected


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> List[str]:
    item_names = list(items.keys())
    n = len(item_names)

    # Initialize DP table
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_names[i - 1]
            selected.append(name)
            w -= items[name]["cost"]

    selected.reverse()
    return selected


# Test both approaches
if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy selection:", greedy_result)
    print("Dynamic programming selection:", dp_result)
