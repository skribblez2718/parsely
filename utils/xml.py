import xml.etree.ElementTree as ET

from utils.logger import logger


def get_in_scope_items(path):
    try:
        items = get_items(path=path)

        in_scope_items = set()
        for item in items.findall("item"):
            in_scope_items.add(item)
        return tuple(in_scope_items)
    except Exception as e:
        logger.error(f"{e} in get_in_scope_items")


def get_items(path):
    try:
        tree = get_tree(path=path)
        return tree.getroot()
    except Exception as e:
        logger.error(f"{e} in get_items")


def get_tree(path):
    try:
        return ET.parse(path)
    except Exception as e:
        logger.error(f"{e} in get_tree")
