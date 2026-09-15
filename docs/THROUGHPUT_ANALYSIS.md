# Throughput Analysis

## Retained data

```text
Distance  Normal  Interference ON
10 m      4.58    2.52 Mbps
30 m      4.58    2.25 Mbps
50 m      4.58    2.25 Mbps
80 m      0.00    0.00 Mbps
```

## Relative reduction

For the 10–50 m points, the interference condition reduces throughput substantially:

- 10 m: `(4.58 - 2.52) / 4.58 ≈ 45.0%`
- 30 m: `(4.58 - 2.25) / 4.58 ≈ 50.9%`
- 50 m: same retained values as 30 m

The report rounds the latter two as 50.8%.

## Distance effect

The normal condition remains flat in the retained table from 10 to 50 m, then reaches 0 Mbps at 80 m. The report attributes this to propagation/path-loss effects.

That interpretation is plausible within the report's experimental framing, but the public portfolio does not claim a universal 80 m cutoff.

## Why the 80 m row needs careful wording

The report labels the final row `100% (Loss)`. However:

- normal throughput = 0 Mbps,
- interference throughput = 0 Mbps.

Therefore the effect size specifically attributable to the interference source is undefined at that point. A more defensible statement is:

> The retained simulation lost measurable throughput at 80 m under both conditions.

## Future statistical improvement

A stronger experiment would run multiple seeds at every configuration and report:

- mean throughput,
- standard deviation,
- confidence interval,
- packet delivery ratio,
- delay/jitter,
- PHY/MAC retry statistics.
