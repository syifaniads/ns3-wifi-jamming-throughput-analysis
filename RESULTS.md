# Results

## Retained throughput dataset

| Distance | Normal throughput | Interference throughput | Reported reduction |
|---|---:|---:|---:|
| 10 m | 4.58 Mbps | 2.52 Mbps | 45% |
| 30 m | 4.58 Mbps | 2.25 Mbps | 50.8% |
| 50 m | 4.58 Mbps | 2.25 Mbps | 50.8% |
| 80 m | 0.00 Mbps | 0.00 Mbps | `100% (Loss)` in report |

## Interpretation

### 10 m

The interference-enabled run falls from `4.58 Mbps` to `2.52 Mbps`, a reduction of about 45%. The link remains usable, but useful throughput is substantially lower.

### 30–50 m

The retained normal runs remain at `4.58 Mbps`, while the interference-enabled runs record `2.25 Mbps`. The report describes this as approximately a 50.8% reduction.

### 80 m

Both normal and interference-enabled conditions record `0 Mbps`.

This point should **not** be interpreted as a jamming-specific 100% degradation, because the normal baseline is already zero. The safest conclusion from the retained data is that the simulated link no longer delivered measurable throughput at 80 m under either condition.

## What can be concluded

The retained runs support these observations:

- high-rate interference reduced useful throughput at 10–50 m,
- distance remained an important factor,
- the tested link collapsed by 80 m in both retained conditions,
- the interference condition did not create the 80 m failure by itself because the baseline also failed.

## What cannot be concluded

The data does not establish:

- statistical confidence intervals,
- variance across repeated random seeds,
- a universal 802.11g jamming threshold,
- real-world RF performance,
- performance of modern 802.11 standards,
- effectiveness of mitigation mechanisms.

See [docs/THROUGHPUT_ANALYSIS.md](docs/THROUGHPUT_ANALYSIS.md) and [LIMITATIONS.md](LIMITATIONS.md).
