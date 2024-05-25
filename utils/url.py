from urllib.parse import urlencode, unquote

from utils.logger import logger
from utils.general import is_filename, is_identifier


def is_invalid_method(method):
    try:
        return method == "OPTIONS"
    except Exception as e:
        logger.error(f"{e} in is_valid_method")
        return False


def is_invalid_path_query(path_query):
    try:
        return (
            ("constructor" in path_query)
            or ("__proto__" in path_query)
            or ("prototypepollution" in path_query)
        )
    except Exception as e:
        logger.error(f"{e} in is_valid_path_query")


def is_invalid_path(path):
    try:
        return ("%" in path) or (is_filename(path=path))
    except Exception as e:
        logger.error(f"{e} in is_valid_path")


def get_parameterized_path_query(path_query):
    try:
        if "?" in path_query:
            path_query_parts = path_query.split("?")
            path = path_query_parts[0]
            query = path_query_parts[1]

            parameterized_path = get_parameterized_path(path=path)
            parameterized_query = get_parameterized_query(query=query)
            path_query = f"{parameterized_path}?{parameterized_query}"
        return path_query
    except Exception as e:
        logger.error(f"{e} in get_parameterized_path_query")
        return ""


def get_parameterized_query(query):
    try:
        query_key_values = query.split("&")

        parameterized_key_values = dict()
        for query_key_value in query_key_values:
            key_value_parts = query_key_value.split("=")
            key = key_value_parts[0]
            value = "{" + key.upper() + "}"
            parameterized_key_values[key] = value
        return unquote(urlencode(parameterized_key_values))
    except Exception as e:
        logger.error(f"{e} in get_parameterized_query")
        return ""


def get_parameterized_path(path):
    try:
        path_parts = path.split("/")
        for path_part in path_parts:
            part = path_part.rstrip("/")
            if is_identifier(part=part):
                path_part = "{IDENTIFIER}"
        return "/".join(path_parts)
    except Exception as e:
        logger.error(f"{e} in get_parameterized_path")
        return ""
