from SinglePlayerStateMachine import single_player_state_machine

_ERROR_MODE = -1


def main_menu():
    _print_main_menu()
    mode = _ERROR_MODE
    while mode == _ERROR_MODE:
        mode = _read_selection()

    _select_mode(mode)


_mode_list = ["Single Player", "Multiplayer", "Online Multiplayer"]


def _print_main_menu():
    # Indents - fli = first level indent, sli = second level indent...
    fli = "\t\t"
    sli = "\t\t\t"

    # Menu
    title = f"""\n\n{fli}D R A G O N   B A L L   S U P E R
{sli}Trading Card Game
"""
    modes = f"""{sli}1: {_mode_list[0]}
{sli}2: {_mode_list[1]}
{sli}3: {_mode_list[2]}
"""
    footer = f"""{fli}This is a fan game. No profit is intended.\n\n"""
    menu = f"{title}\n\n{modes}\n\n{footer}"

    print(menu)


def _read_selection():
    valid_modes = ['1', '2', '3']

    mode = input()
    if mode not in valid_modes:
        mode_list = [s + ", " for s in valid_modes]
        print(f"Invalid mode - Supported input to select modes are {''.join(mode_list)}")
        return _ERROR_MODE

    return int(mode) - 1


def _select_mode(mode):
    if mode == 0:
        single_player_state_machine.run()
