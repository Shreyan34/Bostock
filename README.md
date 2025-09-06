                                BOSTOCK (0.1)
                        A Simple Card-Picking Math Game

OBJECTIVE
---------
Pick 4 cards from a shuffled standard 52-card deck. Convert each card to a point
value, add them up, and try to meet or exceed a randomly chosen target sum
(the "bet").

COMPONENTS
----------
- One standard 52-card deck (no jokers).
- Or run the supplied Python program.

SETUP
-----
1. Shuffle the deck thoroughly.
2. Generate a target sum ("bet") between 14 and 34.
3. The player chooses four distinct card positions from the shuffled deck
   (positions 1 through 52). Reveal those four cards.

CARD VALUES
-----------
Assign each revealed card a numeric value as follows:

- Number cards: face value (2 → 2, 3 → 3, ..., 10 → 10)
- Jack  (J) : 5 points
- Queen (Q) : 15 points
- King  (K) : 10 points
- Ace   (A) : 5 points

SUM & WIN CONDITION
-------------------
1. Add the four card values to get YOUR SUM.
2. If YOUR SUM is greater than or equal to the target bet, you win the round.
3. Otherwise, you lose the round.

EXAMPLE
-------
Suppose the shuffled deck yields these picks:
- 4  → 7 of Diamonds   → 7 points
- 12 → Queen of Spades → 15 points
- 30 → 10 of Clubs     → 10 points
- 47 → Ace of Hearts   → 5 points

YOUR SUM = 7 + 15 + 10 + 5 = 37  
If the bet was 34, you win (37 ≥ 34).

RULES FOR PYTHON VERSION
------------------------
- Enter four distinct integers between 1 and 52 inclusive when prompted.
- Duplicate numbers or out-of-range values are not allowed.
- Indexing is 1-based: 1 = first card, 52 = last card.

FAQ
---
Q: Can I pick the same position twice?  
A: No, all four positions must be unique.   

Q: What if my sum is below the bet?  
A: You lose that round. Play again!  

--------------------------------------------------------------------------------
Have fun playing BOSTOCK — simple to learn, quick to play, and full of surprises!
--------------------------------------------------------------------------------
