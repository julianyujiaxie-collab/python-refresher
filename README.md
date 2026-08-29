# Python Refresher

Utilities and scripts for querying agro-food CO₂ emissions data.

## Requirements

- Python 3
- zsh
- `Agrofood_co2_emission.csv`

## Usage

From the `python-refresher` directory, run:

```sh
./run.sh
```

The script prints forest fire emissions for the United States of America.

## Utility Functions

### `get_column(file_name, query_column, query_value, result_column=1)`

Reads a comma-separated file and returns values from `result_column`
for rows whose `query_column` matches `query_value`.

Column positions use zero-based indexing. The function returns a list
of strings.

## Scripts

- `run.sh`: Runs `print_fires.py`.
- `print_fires.py`: Prints US forest fire emissions.
