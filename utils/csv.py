from utils.logger import logger


def write_csv_file(assets, output_path):
    try:
        column_names = get_column_names()
        column_names_str = get_string_from_tuple(tup=column_names)

        rows_str = get_rows(assets=assets)
        csv_data = column_names_str + rows_str

        with open(output_path, mode="w") as f:
            f.write(csv_data)

    except Exception as e:
        logger.error(f"{e} in write_csv_file")


def get_column_names():
    name = tuple(["name"])
    ip_address = tuple(["ip addresses"])
    criticality = tuple(["criticality"])
    data_owner = tuple(["data owner"])
    physical_location = tuple(["physical location"])
    system_owner = tuple(["system owner"])
    ports = tuple(["ports"])
    tags = tuple(["tags"])
    description = tuple(["description"])
    parent = tuple(["parent"])
    asset_type = tuple(["type"])
    host_fqdn = tuple(["host fqdn"])
    hostname = tuple(["hostname"])
    host_dns = tuple(["host rdns"])
    dns_name = tuple(["dns name"])
    mac_address = tuple(["mac address"])
    netbios_name = tuple(["netbios name"])
    total_cves = tuple(["total cves"])
    pci_status = tuple(["pci status"])
    operating_system = tuple(["operating system"])
    return tuple(
        name
        + ip_address
        + criticality
        + data_owner
        + physical_location
        + system_owner
        + ports
        + tags
        + description
        + parent
        + asset_type
        + host_fqdn
        + hostname
        + host_dns
        + dns_name
        + mac_address
        + netbios_name
        + total_cves
        + pci_status
        + operating_system
    )


def get_string_from_tuple(tup):
    return ",".join(tup) + "\n"


def get_rows(assets):
    rows = ""
    for asset in assets:
        rows += get_string_from_tuple(tup=asset)
    return rows
