#!/usr/bin/env python3

import sys


class None_value(Exception):
    pass


class Redundant_item(Exception):
    pass


class Invalid_parameter(Exception):
    pass


def get_value(inventory: tuple[str, int]) -> int:
    key, value = inventory
    return value


def import_dict() -> dict[str, int]:
    program_name, *args = sys.argv
    inventory: dict[str, int] = {}
    if not args:
        raise None_value("No item provided. Usage: python3 "
                         "ft_inventory_system.py <item_name>:<quantity> ...")
    for arg in args:
        try:
            if ':' in arg:
                key, value = arg.split(':')
            else:
                raise Invalid_parameter(f"Error - invalid parameter '{arg}'")
            if not inventory.get(key):
                inventory[key] = int(value)
            else:
                raise Redundant_item(f"Redundant item '{key}' - discarding")
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
        except Redundant_item as e:
            print(e)
        except Invalid_parameter as e:
            print(e)
    if not inventory:
        raise None_value("No valid item provided. Usage: python3 "
                         "ft_inventory_system.py <item_name>:<quantity> ...")
    return inventory


def print_dict(inventory: dict[str, int]) -> None:
    try:
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        values = inventory.values()
        sum_values = sum(values)
        print(f"Total quantity of the {len(values)} items: {sum_values}")
        for key, value in inventory.items():
            print(f"Item {key} represents "
                  f"{round((value / sum_values) * 100,1)}%")
        max_key, max_value = max(inventory.items(), key=get_value)
        min_key, min_value = min(inventory.items(), key=get_value)
        print(f"Item most abundant: {max_key} with quantity {max_value}")
        print(f"Item least abundant: {min_key} with quantity {min_value}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = import_dict()
    print_dict(inventory)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
