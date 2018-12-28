def validate_card_info(card: dict) -> bool:
    """
    Checks card info are sensible.
    :return: returns True if the card passes the validation, False otherwise
    """
    if card["type"] == "combat":
        return check_combat_card_logic(card)

    if card["type"] == "extra":
        return check_extra_card_logic(card)

    if card["type"] == "leader":
        return check_leader_card_logic(card)

    print(f"Error : unrecognised card type '{card['type']}'")
    return False


def check_extra_card_logic(card: dict) -> bool:
    for key, value in card.items():
        # Most of the fields mustn't be empty
        if value is None:
            if key == "atk" or key == "combo_atk":
                continue
            else:
                print(f"Error: parameter '{key}' is empty")
                return False

    return True


def check_leader_card_logic(card: dict) -> bool:
    for key, value in card.items():
        # Most of the fields mustn't be empty
        if value is None:
            if key == "color_cost" or key == "total_cost" or key == "combo_cost" or key == "combo_atk":
                continue
            else:
                print(f"Error: parameter '{key}' is empty")
                return False

    return True


def check_combat_card_logic(card: dict) -> bool:
    for key, value in card.items():
        # Most of the fields mustn't be empty
        if value is None:
            print(f"Error: parameter '{key}' is empty")
            return False

    return True
