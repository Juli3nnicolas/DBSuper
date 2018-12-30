from GameState import GameState
import single_player_state_functions as functions

choose_first_player = GameState(
    name="Choose first player", state_values={
        "a": "",
    }, run_function=functions.choose_first_player)
