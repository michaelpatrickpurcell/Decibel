# Decibel: A dice mechanic for tabletop role playing games
Dice mechanics lie at the heart of many tabletop role playing games. These mechanics
are often part of a resolution system that players use to determine what actually
happens in the game when their characters attempt to do something risky. These
mechanics provide a source of randomness that is used to model any uncertainty
inherent in the proposed action and their outcome provides an objective measure of
the character's degree of success.

Decibel is a generic dice mechanic that can serve as the chassis on which a complete
tabletop role playing game can be built.  It is a _dice pool_ mechanic.  To use Decibel
as part of a resolution system, players make a _check_ which consists of three steps:

  1. Assemble a pool of twenty-sided dice;
  2. Roll the dice and sort the resulting values from largest to smallest;
  3. Compute the outcome of the check.  

The size of the dice pool depends on the action being attempted and any circumstances
that might affect a characters performance. The outcome of the check is the difference
between the largest and smallest values of the rolled dice. This outcome is then compared
to some other quantity, which could be a fixed _target number_ or the outcome of another
check, to determine what happens in the game.  

## Simple Checks
To make a _simple check_, players roll a pool of three or more twenty-sided dice (d20s).
The outcome of the check is the difference between the largest and smallest values of
the rolled dice. We will write NdB to denote the outcome of a simple check made with a
pool of N dice.

Notice that while the set of possible outcomes (i.e. {0, 1, ..., 19}) is always the same,
the size of the pool determines the distribution of the outcome of a check.
In general, a larger dice pool is more likely to produce greater outcomes than a smaller
dice pool.

#### Example
Suppose that a player is making a simple 5dB check.
The player rolls five twenty-sided dice and gets a result of {14, 10, 7, 6, 3}.
The outcome of the check is 14 - 3 = 11.

#### Figure
This figure depicts the distribution for the outcome of simple checks for various
values of N.

<img src="outcome_distributions.png" width="750" height="550">

## Standard Checks
One shortcoming of simple checks is that the distributions of the outcome of all
such checks are skewed in the same direction. Distributions that are skewed in the
other direction can be generated by discarding dice with the greatest values after
rolling. The outcome of the check is the difference between the largest and smallest
of the remaining values. We will write (N-X)dB to denote the outcome of a
_standard check_ made with a pool of N dice and where the X dice with the greatest
values are discarded before computing the outcome of the check.

Notice that a standard (N-X)dB check is not the same as a simple MdB check where
M = N-X. The distributions of the outcomes of these two checks are generally quite
different.

#### Example
Suppose a player is making a standard (7-3)dB check.  The player rolls seven
twenty-sided dice and gets a result of {18, 15, 11, 10, 7, 6, 4}.  The player then
discards the three dice with the greatest values which yields the intermediate result
of {10, 7, 6, 4}.   The outcome of the check is 10-4 = 6.

#### Figure
This figure depicts the distribution for the outcome of standard checks for various
values of N and X = N-3.

<img src="discard_distributions.png" width="750" height="550">

## Modifiers
A common feature of dice mechanics used in many role playing systems is _modifiers_.
There are two kinds of modifiers, positive and negative.  A positive modifier increases
the probability that a player succeeds at a static resolution roll or wins a dynamic
resolution roll. A negative modifier decreases the probability that a player succeeds
at a static resolution roll or wins a dynamic resolution roll.
In Decibel, as in many dice pool systems, modifiers change the composition of a dice
pool before a check is made. Positive modifiers can be implemented by simply adding dice
to the dice pool. That is, by increasing the value of N in a standard (N-X)dB check.
Negative modifiers can be implemented by both adding dice to the dice pool and increasing
the number of dice that are discarded before computing the outcome of the check.
That is, by increasing both the value of N and X by the same amount in a standard
(N-X)dB check.

Notice that, because they both add dice to the dice pool, positive and negative modifiers
do not simply cancel each other out.  In general, as the number of modifiers increases
the variance of the outcome of a check decreases. That said, allowing positive and
negative modifiers to cancel each other out before applying the remaining modifiers leads
to simpler accounting and more manageable dice pools. So, any game system that uses the
Decibel dice system will need to specify how to handle opposing modifiers.

#### Example
Suppose that a player is making a 5dB check with one positive modifier and two negative
modifiers.  The net result is that the player will make a (8-2)dB check.

#### Figure
This figure depicts the distribution of the outcome of a modified 3dB check for
various amounts of positive and negative modifiers.

<img src="modified_distributions.png" width="750" height="550">

## Static Resolution
In a _static resolution_ roll, the outcome of a Decibel check is compared to a fixed
target number. This is frequently called a "skill check" in many role playing systems.
If the outcome of the Decibel check is greater than or equal to the target number,
then the check is considered a success.  Otherwise, the check is considered a failure.

#### Table
This table describes the probability of succeeding at a static resolution roll
(i.e. NdB >= k) for various values of N and k.

|       |   k = 0 |   k = 1 |   k = 2 |   k = 3 |   k = 4 |   k = 5 |   k = 6 |   k = 7 |   k = 8 |   k = 9 |
|:------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| N = 3 |    1.00 |    1.00 |    0.98 |    0.96 |    0.92 |    0.87 |    0.81 |    0.75 |    0.68 |    0.61 |
| N = 4 |    1.00 |    1.00 |    1.00 |    0.99 |    0.98 |    0.96 |    0.93 |    0.90 |    0.85 |    0.79 |
| N = 5 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    0.99 |    0.98 |    0.96 |    0.93 |    0.89 |
| N = 6 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    0.99 |    0.98 |    0.97 |    0.94 |
| N = 7 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    0.99 |    0.99 |    0.97 |
| N = 8 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    1.00 |    0.99 |    0.99 |

|       |   k = 10 |   k = 11 |   k = 12 |   k = 13 |   k = 14 |   k = 15 |   k = 16 |   k = 17 |   k = 18 |   k = 19 |
|:------|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|
| N = 3 |     0.54 |     0.46 |     0.39 |     0.32 |     0.25 |     0.18 |     0.13 |     0.08 |     0.04 |     0.01 |
| N = 4 |     0.73 |     0.65 |     0.56 |     0.48 |     0.39 |     0.30 |     0.22 |     0.14 |     0.08 |     0.03 |
| N = 5 |     0.84 |     0.78 |     0.70 |     0.62 |     0.52 |     0.42 |     0.31 |     0.21 |     0.12 |     0.04 |
| N = 6 |     0.91 |     0.87 |     0.80 |     0.72 |     0.63 |     0.52 |     0.40 |     0.28 |     0.16 |     0.06 |
| N = 7 |     0.95 |     0.92 |     0.87 |     0.80 |     0.72 |     0.61 |     0.49 |     0.35 |     0.21 |     0.08 |
| N = 8 |     0.97 |     0.95 |     0.92 |     0.86 |     0.79 |     0.69 |     0.56 |     0.42 |     0.26 |     0.10 |

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

#### Table
This table describes the probability of winning a dynamic resolution roll (i.e. MdB > NdB)
for various values of M and N.

|       |   N = 3 |   N = 4 |   N = 5 |   N = 6 |   N = 7 |   N = 8 |
|:------|--------:|--------:|--------:|--------:|--------:|--------:|
| M = 3 |    0.48 |    0.35 |    0.26 |    0.20 |    0.16 |    0.13 |
| M = 4 |    0.60 |    0.46 |    0.37 |    0.30 |    0.24 |    0.20 |
| M = 5 |    0.68 |    0.56 |    0.46 |    0.38 |    0.32 |    0.27 |
| M = 6 |    0.75 |    0.63 |    0.54 |    0.45 |    0.39 |    0.34 |
| M = 7 |    0.79 |    0.68 |    0.59 |    0.51 |    0.45 |    0.39 |
| M = 8 |    0.82 |    0.73 |    0.64 |    0.56 |    0.50 |    0.44 |

## Degree of Success
In some cases we may be interested in how well (or badly) an attempted task is
accomplished instead of simply determining whether the attempt succeeded or failed.
One natural way to accomplish this for a static resolution roll is to compute the
difference between the outcome of a check and the target number. Similarly, a simple way
to accomplish this for a dynamic resolution roll is to compute the difference between
the two checks. In either case, this difference is called the _degree of success_ for the
resolution roll. Greater greater degrees of success correspond to better performance
whilst lesser degrees of success correspond to worse performance. The interpretation of
what a given degree of success means is task-specific. The players should, either
by adopting formal mechanics or by informal agreement, decide on how to interpret the
results before the dice are rolled.

#### Example
Suppose a player is making a 5dB check as part of a static resolution roll with a
target number of 13.  The player rolls five twenty-sided dice and gets a result of
{20, 17, 12, 8, 5}. The outcome of the check is 20 - 5 = 15.  The degree of success is
15 - 13 = 2.

## Secondary Effects
The values of dice that are not used to compute the outcome of a check can be
be used to determine whether any _secondary effects_ occur as a part of the check.
Because dice pools may have as few as three dice, two of which will be used to compute
the outcome of the check, secondary effects may need to be determined by the value of a
single die. One way to accomplish this is to use the largest value that was not used to
determine the outcome of the check to govern any secondary effects.

#### Example
Suppose that a player is making a 4dB check. The player rolls four twenty-sided dice
and gets a result of {17, 15, 11, 3}.  The outcome of the check is 17 - 3 = 14.
Discarding the two dice used to compute the outcome of the check yields a result of
{15, 11}.  The value that governs any secondary effects is 15.

## Compound Checks
In a _compound check_ a dice pool is used to resolve more than one check with a single
roll. To do so, compute the outcome of the first check as normal. Then discard the two
dice whose values were used to compute the first outcome and treat the remaining dice
as if they were the result of a simple check.

Notice that even if the first check is a standard check (X > 0), all subsequent checks
are simple checks (X = 0).  That is, dice are only discarded once prior to computing the
outcome of the first check. Therefore, if five or more dice remain after discarding the
required number of dice, then that dice pool can be used to make a compound check.

#### Example
Suppose that a player is making a (6-1)dB check.  The player rolls six twenty-sided dice
and gets a result of {19, 13, 8, 6, 5, 2}.  They then discard the die with the greatest
value which yields a result of {13, 8, 6, 5, 2}.  The outcome of the first
check is 13 - 2 = 11. Discarding the two dice used to compute the outcome of the first
check yields a result of {8, 6, 5}. The outcome of the second check is
8 - 5 = 3.
