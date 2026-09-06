import argparse

import my_utils


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Print fire emissions for a selected country."
    )

    parser.add_argument(
        "--country",
        required=True,
        help="Country to query.",
    )
    parser.add_argument(
        "--country-column",
        "--country_column",
        dest="country_column",
        type=int,
        required=True,
        help="Zero-based index of the country column.",
    )
    parser.add_argument(
        "--fires-column",
        "--fires_column",
        dest="fires_column",
        type=int,
        required=True,
        help="Zero-based index of the fire emissions column.",
    )
    parser.add_argument(
        "--file-name",
        "--file_name",
        dest="file_name",
        required=True,
        help="Path to the CSV file.",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    fires = my_utils.get_column(
        args.file_name,
        args.country_column,
        args.country,
        result_column=args.fires_column,
    )

    print(fires)


if __name__ == "__main__":
    main()
