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

## Static Resolution
In a _static resolution_ roll, the outcome of a Decibel check is compared to a fixed
target number. This is frequently called a "skill check" in many role playing systems.
If the outcome of the Decibel check is greater than or equal to the target number,
then the check is considered a success.  Otherwise, the check is considered a failure.

## Dynamic Resolution
In a _dynamic resolution_ roll, the outcome of a Decibel check is compared with the
outcome of another Decibel check.  This is frequently called an "opposed roll" in many
role playing systems.  These checks are often used to determine which of two opposing
forces prevails in a direct conflict between the two.  As such, we say that that
whichever check produces the greater outcome wins while the other loses.

If the outcomes of the two checks are equal, then neither check wins (or loses).
In this case, some method of breaking the tie may be required.  Simple options include
re-rolling one or both checks until a winner can be declared, comparing the size of
the dice pools used in the checks, or comparing the results of the dice in the dice
pools that were not used to compute the outcome of the checks.
