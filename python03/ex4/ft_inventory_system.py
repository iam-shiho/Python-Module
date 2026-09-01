#!/usr/bin/env python3

import sys
class None_value(Exception):
    pass

class Redundant_item(Exception):
    pass

class Invalid_parameter(Exception):
    pass

def import_dict() -> dict[str, int]:
    program_name, *args = sys.argv
    inventory = {}
    if not args:
        raise None_value("No item provided. Usage: python3 ft_inventory_system.py <item_name>:<quantity> ...")
    for arg in args:
        try:
            if ':' in arg:
                key, value = arg.split(':')
            else:
                raise Invalid_parameter(f"Error - invalid parameter '{arg}'")
            if inventory.get(key) == None:
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
        raise None_value("No valid item provided. Usage: python3 ft_inventory_system.py <item_name>:<quantity> ...")
    return(inventory)

def print_dict(inventory: dict[str,int]) -> None:
    try:
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        values = inventory.values()
        sum_values = sum(values)
        print(f"Total quantity of the {len(values)} items: {sum_values}")
        for key, value in inventory.items():
            print(f"Item {key} represents {round((value / sum_values) * 100,1)}%")
        max_value = max(inventory, key=inventory.get)
        min_value = min(inventory, key=inventory.get)
        print(f"Item most abundant: {max_value} with quantity {inventory[max_value]}") #最大値
        print(f"Item least abundant: {min_value} with quantity {inventory[min_value]}") #最小値
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

#引数を受取り、各変数に入れていく
    #quanityはint ValueErrorで落とす
    #書式が違うものはerror
    #かぶりがある場合もerror文を出力する
        #一回keyとvalueを各々リストに格納して重複がないかチェック？
        #最初にkeyがあるか確認してから入れる？　<- こっちのほうがわかりやすい
#指定されたものをプリントしていく
    #dictのを取り出してリスト型にして、出力する
    #総数を数える＋その割合を出力する
    #一番多いものを出力
    #一番少ないものを出力
    #try except 文の後にfinallyを追加してマジックアイテムを追加する
#raiseをmainで感知しているのはいいのか悩み
