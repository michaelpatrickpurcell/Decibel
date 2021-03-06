# Combat
This example shows how
[Decibel](README.md)
can be used as part of a traditional tabletop role playing game system.
The mechanical focus of many such games is on the rules governing how combat works.
One common paradigm is to subdivide a combat encounter into a sequence of rounds.
During each round, each character has an opportunity to act.  On a player's turn, they
decide what action their character will take and then resolve that action
immediately. Characters act in some initiative order that is the same
during each round and determined by some independent preliminary process.

In this example, we will use these same basic components but rearrange the order in
which they are performed. During each round:
  1. All of the players decide what actions their characters will attempt to perform.
  2. All of the players declare their characters' intentions.
  3. All of the players assemble a dice pool that will be used to resolve their
     character's action and roll the dice.
  4. All of the players use the results of these rolls to determine initiative order.
  5. In descending initiative order, each player resolves their character's action.  

Details of how initiative order is determined, what kinds of actions can be attempted
in combat, and how those actions should be resolved are given below.   

## Initiative
The order in which actions occur changes from round to round and is determined by the
characters' _initiative_. Every action during combat requires a check to determine how
successfully that action was accomplished. Initiative is a
[secondary effect](README.md#secondary-effects)
of these checks. That is, a character's initiative during each round is determined by
the largest value that was not used to determine the outcome of their action check for
that round. Actions are resolved in descending initiative order.

## Actions
A round represents several seconds during which each character involved in a combat
encounter has an opportunity to take a single _action_. There are two kinds of actions
that a character can take during a round: attack and manoeuvre.

### Attack
An _attack_ is any action taken during combat with the intention of damaging another
character. Attacks are resolved using
[static resolution](README.md#static-resolution)
rolls that are used to determine if a character is successful in their attempt to
attack another character.  The size of the dice pool used for the check is determined
by the attacking characters attack skill while the target number for the check is
determined the defending character's defence rating.

[Modifiers](README.md#modifiers)
can be applied to attack roll checks.  Weapons used to make the attack and
tactically advantageous circumstances could contribute positive modifiers to the check.
Tactically disadvantageous circumstances could contribute negative modifiers to the
check. The effects of armour are generally incorporated into the defending character's
defence rating rather than directly affecting the dice pool used to make the check.

If an attack is successful, then the attacking character will deal damage to the
defending character.  The damage dealt is equal to the
[degree of success](README.md#degree-of-success)
of the attack roll. If the outcome of the attack roll check is equal to the defending
character's defence rating, then the attack succeeds but deals no damage.

If the dice pool used to resolve a character's action is large enough, then it can be
used to make multiple attacks in a single round using the rules for
[compound checks](README.md#compound-checks).
While all of the attacks occur on the same initiative each attack is resolved
independently and each attack can be made against a different defending character.

### Manoeuvre
A _manoeuvre_ is any action taken in combat which is not an attack. Typical examples
include: moving, interacting with an object, or using a skill.  Any action that a
character attempts during combat requires a check. Any activity that the players deem too
trivial to require a check and that can be reasonably accomplished during a single round
can be done "for free" in addition to a "real" action. For example, drawing a weapon
should not in itself constitute a manoeuvre action.  Similarly, shouting a brief warning
to a comrade should not require a manoeuvre action but attempting to negotiate a
ceasefire in the heat of battle certainly should.

Some manoeuvre actions can be resolved using
[static resolution](README.md#static-resolution)
rolls. This is appropriate when an action can be accomplished regardless of whether
other characters accomplish their goals during a given round.  For example, if a character
tries to swing above across a room on a chandelier or a character tries to lift a boulder
off of a fallen companion as an ancient temple collapses around them then a static
resolution roll would be appropriate.

Other manoeuvre actions pit two or more characters against one another in direct
opposition. That is, the characters' goals are mutually exclusive and if one character
accomplishes their goal then the other characters must necessarily fail to accomplish
theirs. In such cases,
[dynamic resolution](README.md#dynamic-resolution)
rolls are more appropriate. For example, if two characters lock blades during a duel
and are struggling to gain an advantage or if several characters are racing to be the
first to grab an ancient artefact from a dragon's hoard, then a dynamic resolution roll
would be appropriate.  

In the case of opposed manoeuvres, the actions of all of the characters involved
are resolved on the winning character's initiative.  
