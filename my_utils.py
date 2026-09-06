import sys


def get_column(file_name, query_column, query_value, result_column=1):
    column_values = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                values = line.strip().split(",")

                if query_column >= len(values) or result_column >= len(values):
                    print(
                        f"Skipping line {line_number}: missing column.",
                        file=sys.stderr,
                    )
                    continue

                if values[query_column] == query_value:
                    try:
                        result = int(float(values[result_column]))
                    except (ValueError, OverflowError):
                        print(
                            f"Skipping line {line_number}: "
                            f"cannot convert {values[result_column]!r} "
                            "to an integer.",
                            file=sys.stderr,
                        )
                        continue

                    column_values.append(result)

    except OSError as error:
        print(
            f"Unable to open {file_name!r}: {error}",
            file=sys.stderr,
        )

    return column_values
