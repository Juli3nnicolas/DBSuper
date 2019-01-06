import single_player_game_states as states


def choose_first_player():
    values = states.choose_first_player.get_state_values()
    values["p1_starts"] = True
    print(states.choose_first_player)


def transition_from_choose_first_player_to_p1_turn():
    return states.choose_first_player.get_state_values()["p1_starts"]


def transition_from_choose_first_player_to_p2_turn():
    return states.choose_first_player.get_state_values()["p2_starts"]


def run_player1_turn():
    values = states.player1_turn.get_state_values()
    values["deck_size"] -= 1
    print(states.player1_turn, values)


def run_player2_turn():
    values = states.player2_turn.get_state_values()
    values["deck_size"] -= 1
    print(states.player2_turn)


def transition_from_player1_turn_to_end_of_game():
    values = states.player1_turn.get_state_values()
    print("transition_from_player1_turn_to_end_of_game", values)
    if values["deck_size"] == 0 or values["life_points"] == 0:
        states.end_of_game.get_state_values()["winner"] = "player 1"
        return True

    return False


def transition_from_player2_turn_to_end_of_game():
    values = states.player2_turn.get_state_values()
    print("transition_from_player2_turn_to_end_of_game", values)
    if values["deck_size"] == 0 or values["life_points"] == 0:
        states.end_of_game.get_state_values()["winner"] = "player 2"
        return True

    return False


def run_end_of_game():
    values = states.player1_turn.get_state_values()
    print(states.end_of_game, values)
