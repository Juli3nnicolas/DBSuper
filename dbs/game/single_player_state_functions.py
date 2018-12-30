import single_player_game_states as states


def choose_first_player():
    values = states.choose_first_player.get_state_values()
    values["bob"] = "hey"
    print(states.choose_first_player)
