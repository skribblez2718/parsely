import argparse
import re

from utils.logger import logger


def get_args():
    parser = argparse.ArgumentParser(
        description="Extract asset information from Burp Proxy history XML export and convert to PlexTrac asset CSV for upload"
    )
    parser.add_argument("--input", help="Path to Burp XML file", required=True)
    parser.add_argument(
        "--output",
        help="Path to to write Plextrac CSV to",
        required=True,
    )
    return parser.parse_args()


def is_filename(path):
    try:
        filename_pattern = r"^.+\.[A-Za-z0-9]{2,5}$"
        return bool(re.match(filename_pattern, path))
    except Exception as e:
        logger.error(f"{e} in is_filename")


def is_identifier(part):
    try:
        return (
            is_uuid(part=part)
            or is_hex_identifier(part=part)
            or is_numeric_identifier(part=part)
        )
    except Exception as e:
        logger.error(f"{e} in is_identifier")
        return False


def is_uuid(part):
    try:
        uuid_pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
        return bool(re.match(uuid_pattern, part))
    except Exception as e:
        logger.error(f"{e} in is_uuid")
        return False


def is_hex_identifier(part):
    try:
        hex_pattern = r"^[A-Fa-f0-9]{16,32}$"
        return bool(re.match(hex_pattern, part))
    except Exception as e:
        logger.error(f"{e} in is_hex_identifier")
        return False


def is_numeric_identifier(part):
    try:
        numeric_pattern = r"^[0-9]{6,32}$"
        return bool(re.match(numeric_pattern, part))
    except Exception as e:
        logger.error(f"{e} in is_numeric_identifier")
        return False
