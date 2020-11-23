# poker
CS 565 HW3

## Description
This program emulates a version of 5 card draw without betting. 

It can be played with 2-5 computer simulated players who are each given 5 cards. 

A function within the class which represents each player decides which cards to swap for new cards.

## Strategy
The function I created in the class MarleeBryant follows a series of rules to hopefully achieve the best hand.

1. If the 5 original cards are a flush, straight, full house, or 4 of a kind, do not swap any cards.

2. If the 5 original cards contain none of the above, but 3 of a kind, swap the other 2 cards.

3. If the 5 original cards contain none of the above, but 2 pairs, swap the other 1 card.

4. If the 5 original cards contain none of the above, but 1 pair, swap the 3 other cards.

5. If the 5 original cards contain none of the above, but are 1 card away from a flush, swap that card.

6. If the 5 original cards contain none of the above, but are 1 card away from a straight, swap that card.

7. If the 5 original cards contain none of the above, keep the highest card and trade in the other 4.

## Performance
I tested the performance of my class with 10,000 randomly generated hands.

It took 115 seconds to process 10,000 hands and achieved a mean rank of 4544.


