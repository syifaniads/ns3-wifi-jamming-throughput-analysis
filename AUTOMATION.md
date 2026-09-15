# Experiment Automation

## Goal

The project automated the distance/interference sweep so that every tested condition followed the same execution pattern and produced machine-readable output.

## Retained workflow

```text
NS-3 scenario
   │
   ├── --distance=<value>
   └── --enableJamming=<true|false>
            │
            ▼
      RESULT output
            │
      grep RESULT
            │
            ▼
       results.csv
            │
            ▼
      pandas / matplotlib
```

## Bash sweep

The report retains the core loop:

```bash
for d in 10 30 50 80
do
  ./ns3 run "scratch/wifi-jamming-project --distance=$d --enableJamming=false" \
    | grep RESULT >> results.csv

  ./ns3 run "scratch/wifi-jamming-project --distance=$d --enableJamming=true" \
    | grep RESULT >> results.csv
done
```

A cleaned reconstruction is provided in [`examples/experiment-loop.sh`](examples/experiment-loop.sh).

## Output contract

The retained report states the simulation emitted:

```text
RESULT,distance,jamming,tx,rx,lost,throughput
```

This is a useful engineering pattern because it decouples simulation execution from later visualization.

## Visualization

The CSV was separated into interference OFF/ON datasets and plotted with Matplotlib as throughput versus distance.

See [`examples/plotting-example.py`](examples/plotting-example.py).

## Reproducibility limitation

The original complete source tree, PCAP set, XML animation file, and raw CSV are not currently retained in this public portfolio. The examples here reconstruct only the workflow that is directly evidenced in the report.
