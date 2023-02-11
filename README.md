# Python Mini Baccarat
#### Video Demo:  <URL https://youtu.be/iHUqDMv_f_8>
#### Description:
Apart from Poker and Blackjack, another card game my friends and I enjoy playing is Baccarat. However, compared to the plethora of Poker and Blackjack apps, there aren't as many Baccarat apps, especially for the version we play. Thus, my project is a simple Baccarat game created on Python, following the rules of the version I usually play.

In Baccarat, players place bets simillar to in Player Vs Player Blackjack, and the winner between the player and the banker wins the bet. However, instead of looking at the sum of each hand and which hand is closest to 21, we instead only look at the last digit of the sum -- the bigger, the better. Similar to 21 being a Blackjack and an instant win, 8s and 9s are called naturals and also are instant wins in Baccarat. In Baccarat, players are also limited to only drawing one additional card. Thus, Baccarat is a much faster game than Blackjack, which makes it perfect for quick winnings (but also losing fast).

Because I wanted to focus on getting the logic of the game right, I elected to just start with a text-based, command line prompt game in python. It is also a single player game where the user plays directly against the CPU AI, rather than in real life where multiple players play against a single banker. Thus, my project is a simplified version of the real thing, so that I could ensure that the game works as it should according to its rules.

Before the game starts, I define and create a deck of 52 cards and also initialise a variable called "earnings" to keep track of the user's winnings according to their bets. Then, the game starts and the user is prompted to place their bet. After the bet is placed, cards are dealt out to the player and CPU. For every card, the number on the card is added to two variable representing the player's score and opponent's score. The remainder of the variables after being divided by 10 is then taken to get the last digit for the final score.

If the score is 8 or 9, the player wins instantly unless the computer matches the score or beats it. Bets will then be distributed. Else, if the score is 7 and below, the player has the option to hit (draw another card) or stand (keep his hand the same). In the case of the CPU, it will always hit if it's current score is 4 or below.

After that round of hitting and standing, the scores are recalculated and compared again. If the player's score is greater, he earns his bet amount from the CPU (+bet). If the player's score is lesser, he loses his bet amount to the CPU. If their scores are tied, player's earnings stay the same.

The additional cases are: If either side already has a greater score and wins, and has two or three cards of the same suit or value, the amount earned will be double or triple of the bet amount respectively.

After the bets are distributed and the player's earnings are updated, they will be prompted to continue playing and place another bet, after which the cycle will repeat again.