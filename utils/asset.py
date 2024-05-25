from utils.logger import logger
from utils.url import (
    is_invalid_method,
    is_invalid_path_query,
    is_invalid_path,
    get_parameterized_path_query,
)


def get_parent_assets(in_scope_items):
    try:
        parent_assets = set()
        for in_scope_item in in_scope_items:
            for child in in_scope_item:
                if child.tag == "host":
                    parent_asset = get_parent_asset(child=child)
                    parent_assets.add(parent_asset)
        return tuple(parent_assets)
    except Exception as e:
        logger.error(f"{e} in get_parent_assets")
        return tuple()


def get_parent_asset(child):
    try:
        host = child.text
        ip = child.attrib["ip"]
        return tuple([host, ip] + ([""] * 18))
    except Exception as e:
        logger.error(f"{e} in get_parent_asset")
        return tuple()


def get_child_assets(in_scope_items):
    try:
        child_assets = set()
        for in_scope_item in in_scope_items:
            method = parent = path_query = ""
            for child in in_scope_item:
                parent = get_host(child=child, host=parent)
                method = get_method(child=child, method=method)
                path_query = get_path_query(child=child, path_query=path_query)

                if parent and method and path_query:
                    child_asset = tuple(
                        [f"{method} {path_query}"] + ([""] * 8) + [parent] + ([""] * 10)
                    )
                    child_assets.add(child_asset)
        return tuple(child_assets)
    except Exception as e:
        logger.error(f"{e} in get_child_assets")
        return tuple()


def get_host(child, host):
    try:
        if child.tag == "host":
            host = child.text
        return host
    except Exception as e:
        logger.error(f"{e} in get_host")
        return ""


def get_method(child, method):
    try:
        if child.tag == "method":
            method = child.text
            if is_invalid_method(method=method):
                method = ""
        return method
    except Exception as e:
        logger.error(f"{e} in get_method")
        return ""


def get_path_query(child, path_query):
    try:
        if child.tag == "path":
            path_query = child.text
            path = path_query.split("?")[0]
            if (is_invalid_path_query(path_query=path_query)) or (
                is_invalid_path(path=path)
            ):
                path_query = ""
            else:
                path_query = get_parameterized_path_query(path_query=path_query)
            return path_query
    except Exception as e:
        logger.error(f"{e} in get_path_query")
        return ""
