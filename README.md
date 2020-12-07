# poker
CS 565 HW3

## Description
This program emulates a version of 5 card draw without betting. 

It can be played with 2-5 computer simulated players who are each given 5 cards. 

A function within the class which represents each player decides which cards to swap for new cards.

## How to use
1. Download the files in the repository and open them in a Python IDE (I used PyCharm).

2. Ensure that the interpreter is set to Python 2.7, the deuces library is downloaded, and the working directory is the one containing the downloaded files.

3. Run PyPokerMain.py and enter a number between 2 and 5 for the number of players.

4. For each player, enter the exact name of the class, for example MarleeBryant and Student1.

5. The final hand of cards and rank is displayed for each player, and the player with the lowest rank is the winner.

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


