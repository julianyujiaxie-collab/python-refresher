def get_column(file_name, query_column, query_value, result_column):
    column_values = []

    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split(",")

            if values[query_column] == query_value:
                column_values.append(values[result_column])

    return column_values
