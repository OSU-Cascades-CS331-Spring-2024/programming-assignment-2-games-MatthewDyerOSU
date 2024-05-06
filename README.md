[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.


Analysis:
    - Four games between myself and the minimax player on 4x4 board.
        - The results of each game were that the minimax player won on depths of 5, 3 and 2, and I was able to win with a depth of 1.
        - The minimax player's moves definitely changed as the depth got smaller and smaller, as it was less able to predict what the best move to take was.
        - Average times for minimax turns:
            - Depth 5: 0.013077 seconds
            - Depth 3: 0.003109 seconds
            - Depth 2: 0.002002 seconds
            - Depth 1: 0.000302 seconds
            - The average time changes because of the depth of the search tree that needs to be explored. As the depth is increased, the minimax algorithm spends more time exploring possible states, and thus takes longer to make its move.

    - Two games between myself and the minimax player on a 8x8 board.
        - The results of each game were that the minimax player beat me at both depths of 5 and 2.
        - I believe the minimax player's moves changed, although I changed my opening moves so that probably influenced what the minimax player did.
        - Average times for minimax turns:
            - Depth 5: 4.161264 seconds
            - Depth 2: 0.011171 seconds
            - Here there was a large difference in average time and this is because of not only the depth increasing but also the size of the board has dramatically increased the amount of possible states, especially as the amount of pieces on the board increase. The amount of time per turn actually increased until about halfway through the game, where there was a balance of many pieces on the board but still many open cells to place pieces. Near the beginning there were less pieces to move, and towards the end of the game there were less empty cells to place them in, and those turns were quicker. 
    