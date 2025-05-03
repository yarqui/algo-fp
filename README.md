# Monte Carlo Dice Simulation

This project simulates rolling two 6-sided dice a large number of times using the **Monte Carlo method**. It calculates and compares the empirical probabilities of each possible sum (from 2 to 12) with the theoretical probabilities.

## Description

Two standard dice are rolled repeatedly. Each roll's result is the sum of the two dice. After a specified number of simulations (e.g., 100,000 rolls), the code:

- Counts how often each sum occurs.
- Calculates the empirical (simulated) probabilities.
- Compares these to the theoretical probabilities based on combinatorics.
- Displays a bar chart of simulated probabilities.

## Theoretical Probabilities

| Sum | Probability |
| --- | ----------- |
| 2   | 2.78%       |
| 3   | 5.56%       |
| 4   | 8.33%       |
| 5   | 11.11%      |
| 6   | 13.89%      |
| 7   | 16.67%      |
| 8   | 13.89%      |
| 9   | 11.11%      |
| 10  | 8.33%       |
| 11  | 5.56%       |
| 12  | 2.78%       |

## Features

- Uses only standard Python libraries and `matplotlib`.
- Accurate frequency counting with `collections.Counter`.
- Clean probability calculation and comparison.
- Includes a clear bar chart visualisation.
- Fully reproducible and easy to understand.

## How to Run

```bash
python t7.py
```

## Output

- Printed table comparing Monte Carlo and theoretical probabilities.
- A bar chart of simulated probabilities for each dice sum.

## Conclusion

This Monte Carlo simulation accurately reflects the expected distribution of dice sums and confirms theoretical predictions through empirical observation.
