Instructions on compiling and running my program:
    To play the game against the bot:
        Simply run python jrespinal.py to run the program, then enter either 'blue' or 'orange' to decide the color of the bot
    Against the referee:
        Run cs4341-referee tictactoe -p "python jrespinal.py" --visual

The utility function that your program uses:
    The utility function can be found within the jrespinal.py file, I gave 100 points if blue won and -100 if orange won.
    Who I gave the point to depended on which player was taking its turn at the time. If it was Blues turn, then they'd get 1 if they won and -1 if they lost, with 0 for the draw.
    The same thing would happen if the orange player was going
    Function:
        def utility(game: dict, player_token):
            winning_combinations = [
                    # Rows
                    ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
                    # Columns
                    ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
                    # Diagonals
                    ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3']
            ]

            for combo in winning_combinations:
                if all(game[pos] == "X" for pos in combo):
                    return 1 if player_token == "X" else -1
                if all(game[pos] == "O" for pos in combo):
                    return 1 if player_token == "O" else -1
            # if it passes all of these tests, then it must be a draw
            return 0


Results:
Describe which tests you ran to try out your program:
    Other than testing it with the referee program, I played against it myself to see what moves it would make if I wasn't playing "optimally"

Did your program play against human players?
    Yes, I played against it myself for testing

Did your program play against itself?
    Yes, the referee program makes it play against itself. if we are speaking about just my program then no, it plays against a human inputting their moves

Did your program play against other programs?
    If playing against itself is considered another program then yes.
    If it is not then no, not yet but, in the future it will. Although id like to make additions to it and write it in C++ for lower latency

How did your program do during those games?
    My program seems to make the optimal move at each step, if I am about to get 3 in a row, it knows to block me from winning.
    The best I was able to get against it was a draw, but that could mean im just bad at tic tac toe.
    Additionally, it makes moves very fast, with it taking only about .2 seconds on average

describe the strengths and the weaknesses of your program.
    Since my algorithm uses alpha beta pruning, it saves a lot of time by not exploring certain tree branches that lead to losses
    When it comes to tic tac toe, I do not think it has any weaknesses, but I could see issues in the future with game trees which are bigger with a higher branching factor