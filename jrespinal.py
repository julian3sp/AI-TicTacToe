import math
import sys
import time


def minimax(game: dict, a, b, player_token):
    value, move = max_value(game, a, b, player_token)
    return move


def max_value(game, a, b, player_token):
    # check if game is in a terminal state, if it is then return the utility value
    if is_terminal(game, player_token):
        return utility(game, player_token), None

    v = -math.inf
    move = ""

    for action in actions(game):
        new_game = result(game, action, player_token)
        next_player = "O" if player_token == "X" else "X"  # Alternate turns
        v2, a2 = min_value(new_game, a, b, next_player)  # Swap player
        if v2 > v:
            v, move = v2, action
            a = max(a, v)
        if v >= b:
            return v, move
    return v, move



def min_value(game, a, b, player_token):
    # check if game is terminal, if so return utility
    if is_terminal(game, player_token):
        return utility(game, player_token), None

    v = math.inf
    move = ""
    for action in actions(game):
        # make copy of game with move made to not change the actual game board
        new_game = result(game, action, player_token)
        next_player = "O" if player_token == "X" else "X" # Alternate turn
        v2, a2 = max_value(new_game, a, b, next_player)  # Swap player
        if v2 < v:
            v, move = v2, action
            b = min(b, v)
        if v <= a:
            return v, move
    return v, move



def actions(game: dict):
    # return all the keys that do not have assigned values in the hashmap
    return [k for k in game if game[k] == " "]


def result(game: dict, action, player_token):
    game_copy = game.copy()
    game_copy[action] = player_token
    return game_copy


def utility(game, player_token):
    winning_combinations = [
        ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],  # Rows
        ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],  # Columns
        ["a1", "b2", "c3"], ["a3", "b2", "c1"]  # Diagonals
    ]

    # Check if any of the two players have won
    # if all the game positions listed in one of the combinations above is populated by solely a "X" or "O", then the game is won
    if any(all(game[pos] == "X" for pos in combo) for combo in winning_combinations):
        return 100  # X wins
    elif any(all(game[pos] == "O" for pos in combo) for combo in winning_combinations):
        return -100  # O wins
    else:
        return 0  # No winner yet



def is_terminal(game: dict, _):
    # Check if the board is full (draw condition)
    if all(game[key] != " " for key in game):
        return True
    # Check if either X or O has won
    if utility(game, "X") == 100 or utility(game, "O") == -100:
        return True
    return False




def is_valid_move(game: dict, move: str):
    # simply check if that square has been filled o not
    if move in game and game[move] == " ":
        return True
    return False


def calculate_winner(game, winner):
    if utility(game, "X") == 100:
        print("Player " + winner + " wins!")
    elif utility(game, "O") == -100:
        print("Player " + winner + " wins!")
    else:
        print("There has been a draw, both players receive 0 points!")
    sys.exit(0)

def main():
    game = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

    # Read initial color/symbol
    player_id = input().strip()
    a = -math.inf
    b = math.inf
    player_token = "X"
    opponent_token = "O"
    if player_id == "blue":
        player_turn = True
    elif player_id == "orange":
        player_turn = False
    else:
        print("Please enter a valid player name. Either 'blue' or 'orange'")
        sys.exit(0)
    while True:
        # if I am X, produce the first move
        try:
            if not player_turn:
                # collect move
                game_input = input().strip()
                # determine if the move is valid
                if is_valid_move(game, game_input):
                    game[game_input] = opponent_token
                    # check if the game has ended, this is only in effect if the game is won without the referee
                    if is_terminal(game, player_token):
                        calculate_winner(game, "orange")
                else:
                    print("Player " + opponent_token + " has given an invalid move with move "
                          + game_input + "! Player X wins!")
                    sys.exit(0)
                player_turn = True

            else:
                start_time = time.time()
                # Your move logic here
                move = minimax(game, a, b, player_token)
                end_time = time.time()
                elapsed_time = end_time - start_time
                # check if move was made in time
                if elapsed_time > 2:
                    print("Time limit exceeded")
                    sys.exit(0)

                # check if move is valid
                if is_valid_move(game, move):
                    game[move] = player_token
                    # send move to referee
                    print(move, flush=True)
                    if is_terminal(game, player_token):
                        calculate_winner(game, "blue")
                else:
                    print("Player " + player_token + " has given an invalid move " + move + "! Player O wins!")
                    sys.exit(0)
                # no longer our players turn
                player_turn = False

        except EOFError:
            break


if __name__ == "__main__":
    main()
