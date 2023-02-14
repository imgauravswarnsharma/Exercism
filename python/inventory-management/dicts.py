"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    dict_x = {}
    for i in items:
        count_x = items.count(i)
        dict_x[i] = count_x
    return dict_x

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for i in items:
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] +=1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for i in items:
        if inventory[i]==0:
            continue
        else:
            inventory[i] -=1
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    for keys in inventory:
        if keys == item:
            inventory.pop(keys)
            return inventory
    return inventory

def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_x = []
    for item in inventory.items():
        if item[1]>0:
            list_x.append(item)
    return list_x
