import json
from sys import exit
import argparse
from pathlib import Path
from validator import validate_card_info
"""
This scripts adds one card to the card database. The card is formatted in json.
:name str: Card's name
:type str: Card's type. It must be one of 'leader', 'combat', 'extra'
:color str: Card's color. It must be one of 'red', 'green', 'blue', 'yellow', 'black' or ''
:color_cost str: Card's color cost to be summoned in combat zone. It must be lower than or equal to its 'total_cost'
:total_cost str: Card's total cost to be summoned in combat zone.
:combo_cost str: Card's cost to be summoned in combo zone.
:atk str: Card's attack when summoned in action zone.
:combo_atk: Card's attack when summoned in combo zone.
"""

# Parse command line arguments

parser = argparse.ArgumentParser(description=globals().__doc__)
parser.add_argument("--name", help="card's name. This parameter is mandatory")
parser.add_argument("--type", help="card's type. This parameter is mandatory")
parser.add_argument("--color", help="card's color. This parameter is mandatory")
parser.add_argument(
    "--color_cost",
    help="Card's color cost to be summoned in combat zone. It must be lower than or equal to its 'total_cost'")
parser.add_argument("--total_cost", help="Card's total cost to be summoned in combat zone.")
parser.add_argument("--combo_cost", help="Card's cost to be summoned in combo zone.")
parser.add_argument("--atk", help="Card's attack when summoned in action zone.")
parser.add_argument("--combo_atk", help="Card's attack when summoned in combo zone.")

args = parser.parse_args()
raw_card = args.__dict__

if not validate_card_info(raw_card):
    exit(-1)

# Check the card doesn't already exist
file_path = f"./card_database/{raw_card['name']}"

if Path(file_path).is_file():
    print(f"Error : file '{file_path}' already exists. Please delete it to overwrite changes.")
    exit(-1)

# Add the card to the database
card = json.dumps(raw_card)
with open(f"./card_database/{raw_card['name']}", "w") as f:
    f.writelines(card)

print(f"Success : file '{file_path}' has been written to disk with the following content : \n{card}")
