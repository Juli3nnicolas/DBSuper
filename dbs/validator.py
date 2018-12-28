def validate_card_info(card: dict) -> bool:
    """
    Checks card info are sensible.
    :return: returns True if the card passes the validation, False otherwise
    """
    if card["type"] == "combat":
        return _check_combat_card_logic(card)

    if card["type"] == "extra":
        return _check_extra_card_logic(card)

    if card["type"] == "leader":
        return _check_leader_card_logic(card)

    print(f"Error : unrecognised card type '{card['type']}'")
    return False


def _check_extra_card_logic(card: dict) -> bool:
    """
    Checks an extra-card is not ill-formated.
    :return: True if well formated.
    """
    none_keys = {"atk", "combo_atk", "combo_cost"}

    return _check_card_fields(card, none_keys)


def _check_leader_card_logic(card: dict) -> bool:
    """
    Checks a leader-card is not ill-formated.
    :return: True if well formated.
    """
    none_keys = {"color", "color_cost", "total_cost", "combo_cost", "combo_atk"}

    return _check_card_fields(card, none_keys)


def _check_combat_card_logic(card: dict) -> bool:
    """
    Checks a combat-card is not ill-formated.
    :return: True if well formated.
    """
    return _check_card_fields(card, {})


def _check_card_fields(card: dict, none_keys: set) -> bool:
    """
    Returns true when all fields, not present in the none_keys set, are not None AND
    all fields present in the none_keys set have values set to None.
    """
    for key, value in card.items():
        # These fields must be empty
        if key in none_keys:
            if value is not None:
                print(f"Error: parameter '{key}' must be empty")
                return False
        else:
            # These fields are mandatory
            if value is None:
                print(f"Error: parameter '{key}' is empty")
                return False

    return True
