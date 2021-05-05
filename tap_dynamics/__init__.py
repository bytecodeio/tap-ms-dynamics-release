import singer
from singer import utils

from tap_dynamics.discover import discover
from tap_dynamics.sync import sync

REQUIRED_CONFIG_KEYS = [
    "start_date",
    "organization_uri",
    "user_agent",
    "client_id",
    "client_secret",
    "tenant_id",
    "redirect_uri"
]
LOGGER = singer.get_logger()


@utils.handle_top_exception(LOGGER)
def main():
    # Parse command line arguments
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)

    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        catalog = discover(args.config)
        catalog.dump()
    # Otherwise run in sync mode
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = discover(args.config)
        sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
