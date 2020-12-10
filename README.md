# Decibel
A simple dice mechanic for tabletop role playing games.

## Simple Checks
To make a simple check, players roll a pool of three or more twenty-sided dice (d20s).
The outcome of the check is the difference between the largest and smallest values.
We will write NdB to denote the outcome of a simple check made with a pool of N dice.

Notice that while the set of possible outcomes (i.e. {0, 1, ..., 19}) is always the same,
the size of the pool determines the distribution of the outcome of a check.
In general, larger dice pools are more likely to produce greater outcomes than smaller
dice pools.

### Example
Suppose that  aplayer is making a simple 5dB check.
The player rolls five twenty-sided dice and gets a result of {6,14,3,7,10}.
The outcome of the check is 14 - 3 = 11.
