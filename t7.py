import random
import matplotlib.pyplot as plt
from collections import Counter


def simulate_dice_rolls(trials: int = 100_000) -> dict:
    results = [random.randint(1, 6) + random.randint(1, 6) for _ in range(trials)]
    frequencies = Counter(results)

    for total in range(2, 13):
        frequencies.setdefault(total, 0)

    return dict(sorted(frequencies.items()))


def calculate_probabilities(frequencies: dict, total_trials: int) -> dict:
    return {
        total: round((freq / total_trials) * 100, 2)
        for total, freq in frequencies.items()
    }


def plot_probabilities(probabilities: dict) -> None:
    sums = list(probabilities.keys())
    values = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, values, color="#4c72b0", edgecolor="black")
    plt.xticks(sums)
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability (%)")
    plt.title("Monte Carlo Simulation: Dice Sum Probabilities")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def compare_with_theoretical(probabilities: dict) -> None:
    theoretical = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78,
    }

    print(f"{'Sum':<5}{'Monte Carlo (%)':<20}{'Theoretical (%)':<20}{'Difference (%)'}")
    print("-" * 65)
    for total in range(2, 13):
        mc = probabilities.get(total, 0)
        th = theoretical[total]
        diff = round(abs(mc - th), 2)
        print(f"{total:<5}{mc:<20}{th:<20}{diff}")


if __name__ == "__main__":
    TRIALS = 100_000

    freqs = simulate_dice_rolls(TRIALS)
    probs = calculate_probabilities(freqs, TRIALS)

    plot_probabilities(probs)
    compare_with_theoretical(probs)
