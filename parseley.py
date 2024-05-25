from utils.general import get_args
from utils.logger import logger
from utils.xml import get_in_scope_items
from utils.asset import get_parent_assets, get_child_assets
from utils.csv import write_csv_file


def main():
    try:
        args = get_args()
        logger.info("Getting in scope items..")
        in_scope_items = get_in_scope_items(path=args.input)

        logger.info("Getting assets..")
        parent_assets = get_parent_assets(in_scope_items=in_scope_items)
        child_assets = get_child_assets(in_scope_items=in_scope_items)
        assets = parent_assets + child_assets
        logger.info(f"Writing results to {args.output}")
        write_csv_file(assets=assets, output_path=args.output)
    except Exception as e:
        logger.error(f"{e} in main")


if __name__ == "__main__":
    main()
