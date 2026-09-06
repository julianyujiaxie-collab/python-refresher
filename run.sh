#!/usr/bin/env zsh

set -e
cd -- "${0:A:h}"

print -r -- "1. Valid query"
python3 print_fires.py \
    --country "United States of America" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "Agrofood_co2_emission.csv"

print
print -r -- "2. File-opening error"
python3 print_fires.py \
    --country "United States of America" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "missing.csv"

print
print -r -- "3. Integer-conversion error"
python3 print_fires.py \
    --country "Area" \
    --country-column 0 \
    --fires-column 3 \
    --file-name "Agrofood_co2_emission.csv"
