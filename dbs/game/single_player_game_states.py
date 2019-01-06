from GameState import GameState
import single_player_state_functions as functions

choose_first_player = GameState(
    name="Choose first player",
    state_values={
        "p1_starts": False,
        "p2_starts": False
    },
    run_function=functions.choose_first_player)

player1_turn = GameState(
    name="Player 1 turn",
    state_values={
        "deck_size": 5,
        "life_points": 8
    },
    run_function=functions.run_player1_turn)

player2_turn = GameState(
    name="Player 2 turn", state_values={
        "deck_size": 5,
        "life_points": 8
    }, run_function=functions.run_player2_turn)

end_of_game = GameState(name="End of game", state_values={"winner": ""}, run_function=functions.run_end_of_game)
