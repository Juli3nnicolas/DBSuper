from dbs import validator


def test__check_leader_card_logic_returns_true_when_given_valid_input():
    card = {
        "name": "bob",
        "type": "leader",
        "color": None,
        "color_cost": None,
        "total_cost": None,
        "combo_cost": None,
        "atk": "10000",
        "combo_atk": None
    }

    assert validator._check_leader_card_logic(card)


def test__check_leader_card_logic_returns_false_when_given_exceeding_parameter_values():
    card = {
        "name": "bob",
        "type": "leader",
        "color": "blue",
        "color_cost": "2",
        "total_cost": "4",
        "combo_cost": "1",
        "atk": "10000",
        "combo_atk": "1000"
    }
    assert not validator._check_leader_card_logic(card)

    card["color"] = None
    assert not validator._check_leader_card_logic(card)

    card["color_cost"] = None
    assert not validator._check_leader_card_logic(card)

    card["total_cost"] = None
    assert not validator._check_leader_card_logic(card)

    card["combo_cost"] = None
    assert not validator._check_leader_card_logic(card)

    card["combo_atk"] = None
    assert validator._check_leader_card_logic(card)


def test__check_leader_card_logic_returns_false_when_given_empty_mandatory_values_values():
    card = {
        "name": None,
        "type": None,
        "color": None,
        "color_cost": None,
        "total_cost": None,
        "combo_cost": None,
        "atk": None,
        "combo_atk": None
    }
    assert not validator._check_leader_card_logic(card)


def test__check_extra_card_logic_returns_true_when_given_valid_input():
    card = {
        "name": "bob",
        "type": "extra",
        "color": "blue",
        "color_cost": "1",
        "total_cost": "1",
        "combo_cost": None,
        "atk": None,
        "combo_atk": None
    }

    assert validator._check_extra_card_logic(card)


def test__check_extra_card_logic_returns_false_when_given_exceeding_parameter_values():
    card = {
        "name": "bob",
        "type": "leader",
        "color": "blue",
        "color_cost": "2",
        "total_cost": "4",
        "combo_cost": "1",
        "atk": "10000",
        "combo_atk": "1000"
    }
    assert not validator._check_leader_card_logic(card)

    card["combo_cost"] = None
    assert not validator._check_leader_card_logic(card)

    card["atk"] = None
    assert not validator._check_leader_card_logic(card)

    card["combo_atk"] = None
    assert validator._check_extra_card_logic(card)


def test__check_extra_card_logic_returns_false_when_given_empty_mandatory_values_values():
    card = {
        "name": None,
        "type": None,
        "color": None,
        "color_cost": None,
        "total_cost": None,
        "combo_cost": None,
        "atk": None,
        "combo_atk": None
    }
    assert not validator._check_extra_card_logic(card)


def test__check_combat_card_logic_returns_true_when_given_valid_input():
    card = {
        "name": "bob",
        "type": "extra",
        "color": "blue",
        "color_cost": "1",
        "total_cost": "1",
        "combo_cost": "2",
        "atk": "35000",
        "combo_atk": "15000"
    }

    assert validator._check_combat_card_logic(card)


def test__check_combat_card_logic_returns_true_when_given_empty_values():
    card = {
        "name": None,
        "type": "extra",
        "color": "blue",
        "color_cost": "1",
        "total_cost": "1",
        "combo_cost": "2",
        "atk": "35000",
        "combo_atk": "15000"
    }

    for key, value in card.items():
        assert not validator._check_combat_card_logic(card)
        card[key] = None


def test__check_card_fields_returns_true_when_fields_are_not_none():
    content = {"a": "1", "b": "2"}

    assert validator._check_card_fields(content, {})

    content["a"] = None
    assert validator._check_card_fields(content, {"a"})
