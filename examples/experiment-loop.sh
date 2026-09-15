#!/usr/bin/env bash
set -euo pipefail

OUTPUT="results.csv"
: > "$OUTPUT"

for distance in 10 30 50 80; do
  ./ns3 run "scratch/wifi-jamming-project --distance=${distance} --enableJamming=false" \
    | grep '^RESULT' >> "$OUTPUT"

  ./ns3 run "scratch/wifi-jamming-project --distance=${distance} --enableJamming=true" \
    | grep '^RESULT' >> "$OUTPUT"
done

echo "Saved experiment output to $OUTPUT"
