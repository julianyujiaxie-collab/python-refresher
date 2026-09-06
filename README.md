# Python Refresher

A small Python project for querying columns from an agro-food CO₂ emissions dataset.

## Requirements

- Python 3
- zsh
- `Agrofood_co2_emission.csv`

The CSV file must be located in the `python-refresher` directory when using the included examples.

## Usage

Run `print_fires.py` with the required command-line arguments:

```sh
python3 print_fires.py \
    --country "United States of America" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "Agrofood_co2_emission.csv"
```

Column positions use zero-based indexing. For example, the first column has index `0`.

## Command-Line Arguments

| Argument | Type | Description |
| --- | --- | --- |
| `--country` | string | Country or query value to match. |
| `--country-column` | integer | Zero-based index of the column containing the country. |
| `--fires-column` | integer | Zero-based index of the column containing fire emissions. |
| `--file-name` | string | Path to the CSV file. |

Underscore variants such as `--country_column`, `--fires_column`, and
`--file_name` are also supported.

All four command-line arguments are required.

## Examples

### Successful query

```sh
python3 print_fires.py \
    --country "United States of America" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "Agrofood_co2_emission.csv"
```

This prints a list of forest fire emission values for the United States
of America.

### File-opening error

```sh
python3 print_fires.py \
    --country "United States of America" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "missing.csv"
```

Because `missing.csv` does not exist, the program reports a file-opening
error and returns an empty list.

### Integer-conversion error

```sh
python3 print_fires.py \
    --country "Area" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "Agrofood_co2_emission.csv"
```

This matches the CSV header and attempts to convert `Forest fires` to an
integer. The program reports the conversion error and skips that value.

## Running All Examples

The `run.sh` script runs all three examples:

```sh
./run.sh
```

The script changes to its own directory before running the examples, so
it can also be invoked from another working directory.

## Utility Function

### `get_column(file_name, query_column, query_value, result_column=1)`

`get_column()` reads a comma-separated file line by line. For every row
where `query_column` matches `query_value`, it converts the value in
`result_column` to an integer and adds it to the returned list.

The `result_column` argument defaults to column index `1`.

Decimal values are converted to `float` before being converted to
`int`. This truncates the decimal portion toward zero.

The function handles:

- File-opening errors, including missing files and permission errors.
- Values that cannot be converted to integers.
- Rows that do not contain the requested columns.

Invalid values are skipped, while successfully converted values remain
in the returned list. Error messages are written to standard error.

## Project Files

- `my_utils.py`: Contains the reusable `get_column()` function.
- `print_fires.py`: Parses command-line arguments and runs a column query.
- `run.sh`: Demonstrates one successful query and two handled errors.
- `Agrofood_co2_emission.csv`: Local emissions dataset used by the examples.
