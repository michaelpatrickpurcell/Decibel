import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats

from collections import Counter


def decibel_check(N, X, s=20):
    """
    Make a (N-X)dB check. Default values for s and X yield a standard NdB check.

    args:
        N: The number of dice in the dice pool.
        s: The number of sides for each die in the dice pool.
        X: The number of dice to discard before computing the outcome of the check.

    Returns:
        The outcome of a (N-X)dB check.
    """

    results = np.random.randint(1, s + 1, size=N)
    results.sort()
    results = results[: (N - X)]
    return results[-1] - results[0]


# ========================================================================================
# Visualize the effect of varying the size of the dice pool.
# ========================================================================================
TRIALS = 2 ** 16
X = 0
for N in range(3, 9):
    outcomes = np.array([decibel_check(N, X) for i in range(TRIALS)])
    c = Counter(outcomes)
    for k in c.keys():
        c[k] /= TRIALS
    plt.plot(*list(zip(*sorted(c.items()))), label="N=%i" % N)

plt.title("Distribution of NdB Outcomes")
plt.xlabel("k")
plt.xticks(np.arange(20))
plt.ylabel("P{NdB = k}")
plt.legend()
plt.show()


# ========================================================================================
# Visualize the probability of succeeding at a static resolution roll.
# ========================================================================================
TRIALS = 2 ** 16
X = 0
hits = np.zeros((6, 20))
for i, N in enumerate(range(3, 9)):
    for k in range(20):
        print((N, k))
        outcomes = np.array([decibel_check(N, X) for i in range(TRIALS)])
        hits[i, k] = (outcomes >= k).mean()

df = pd.DataFrame(
    hits,
    columns=["k = %i" % i for i in range(20)],
    index=["N = %i" % i for i in range(3, 9)],
)
print(df.iloc[:, :10].to_markdown(floatfmt=".2f"))
print(df.iloc[:, 10:].to_markdown(floatfmt=".2f"))

plt.imshow(hits, aspect="auto")
plt.title("P{NdB >= k}")
plt.xlabel("k")
plt.xticks(np.arange(20))
plt.ylabel("N")
plt.yticks(np.arange(6), np.arange(3, 9))
plt.show()


# ========================================================================================
# Visualize the probability of winning a dynamic resolution roll.
# ========================================================================================
TRIALS = 2 ** 16
X = 0
hits = np.zeros((6, 6))
for i, M in enumerate(range(3, 9)):
    for j, N in enumerate(range(3, 9)):
        print((M, N))
        outcomes_1 = np.array([decibel_check(M, X) for i in range(TRIALS)])
        outcomes_2 = np.array([decibel_check(N, X) for i in range(TRIALS)])
        hits[i, j] = (outcomes_1 > outcomes_2).mean()

df = pd.DataFrame(
    hits,
    columns=["N = %i" % i for i in range(3, 9)],
    index=["M = %i" % i for i in range(3, 9)],
)
print(df.to_markdown(floatfmt=".2f"))

plt.imshow(hits)
plt.title("P{MdB > NdB}")
plt.xlabel("N")
plt.xticks(np.arange(6), np.arange(3, 9))
plt.ylabel("M")
plt.yticks(np.arange(6), np.arange(3, 9))
plt.show()


# ========================================================================================
# Visualize the effect of discarding dice before computing the outcome of a check.
# Here we fix the size of the dice pool and vary the number of dice that are kept.
# ========================================================================================
TRIALS = 2 ** 16
N = 9
s = 20
for X in range(N - 2):
    outcomes = np.array([decibel_check(N, X) for i in range(TRIALS)])
    c = Counter(outcomes)
    for k in c.keys():
        c[k] /= TRIALS
    plt.plot(*list(zip(*sorted(c.items()))), label="X=%i" % X)

plt.title("Distribution of (9-X)dB Outcomes")
plt.xlabel("k")
plt.xticks(np.arange(20))
plt.ylabel("P{(9-X)dB = k}")
plt.legend()
plt.show()


# ========================================================================================
# Visualize the effect of discarding dice before computing the outcome of a check.
# Here we fix the number of dice kept and vary the size of the dice pool.
# ========================================================================================
TRIALS = 2 ** 16
for N in range(3, 9):
    X = N - 3
    outcomes = np.array([decibel_check(N, N - 3) for i in range(TRIALS)])
    c = Counter(outcomes)
    for k in c.keys():
        c[k] /= TRIALS
    plt.plot(*list(zip(*sorted(c.items()))), label="(%i-%i)dB" % (N, X))

plt.title("Distribution of (N-X)dB Outcomes")
plt.xlabel("k")
plt.xticks(np.arange(20))
plt.ylabel("P{(N-X)dB = k}")
plt.legend()
plt.show()


# ========================================================================================
# Visualize the effect of modifiers.
# ========================================================================================
TRIALS = 2 ** 16
N0 = 3
for m in range(-3, 4, 1):
    if m < 0:
        N = N0 - m
        X = -m
    else:
        N = N0 + m
        X = 0
    outcomes = np.array([decibel_check(N, X) for i in range(TRIALS)])
    c = Counter(outcomes)
    if m < 0:
        plt.plot(*list(zip(*sorted(c.items()))), label="(%i-%i)dB" % (N, X))
    else:
        plt.plot(*list(zip(*sorted(c.items()))), label="%idB" % N)

plt.title("Distribution of Modified Checks")
plt.xlabel("k")
plt.xticks(np.arange(20))
plt.ylabel("P{(N-X)dB = k}")
plt.legend()
plt.show()


# ========================================================================================
# Visualize distribution of the roll-and-keep alternative to Decibel
# ========================================================================================
TRIALS = 2 ** 16

for N in range(3, 9):
    results = np.random.randint(1, 7, size=(TRIALS, N))
    results.sort()
    outcomes = results[:, :3].sum(axis=1)
    c = Counter(outcomes)
    for k in c.keys():
        c[k] /= TRIALS
    plt.plot(*list(zip(*sorted(c.items()))), label="N = %i" % N)

plt.legend()
plt.show()

# ========================================================================================
# Visualize distribution of the secondary effect results
# ========================================================================================
TRIALS = 2 ** 22
N = 3
X = 0
s = 10
results = np.random.randint(0, s, size=(TRIALS, N))
results.sort(axis=1)
results = results[:, : (N - X)]
outcomes = results[:, -1] - results[:, 0]
secondary_outcomes = results[:, -2]

combined_outcomes = np.zeros((s, s))
for outcome, secondary_outcome in zip(outcomes, secondary_outcomes):
    combined_outcomes[outcome, secondary_outcome] += 1

for i in range(s):
    plt.plot(combined_outcomes[i] / sum(combined_outcomes[i]), label="outcome = %i" % i)

plt.legend()
plt.show()
