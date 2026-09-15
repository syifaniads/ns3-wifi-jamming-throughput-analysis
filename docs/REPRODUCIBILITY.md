# Reproducibility Notes

## Retained software stack

- NS-3 3.38
- C++ simulation scenario
- Bash experiment runner
- Python with pandas/Matplotlib
- NetAnim
- Wireshark

## Minimal reproduction plan

1. Install NS-3 3.38 in an isolated lab environment.
2. Recreate the three-node AP/STA/interference topology.
3. Configure 802.11g with constant `ErpOfdmRate6Mbps` data/control mode.
4. Parameterize distance and interference state.
5. Install the UDP server/client applications and the high-rate broadcast source.
6. Add FlowMonitor and PCAP output.
7. Run every distance with interference OFF and ON.
8. Export results to CSV.
9. Plot throughput against distance.
10. Inspect PCAPs in Wireshark and topology in NetAnim.

## Missing original artifacts

The public portfolio currently does not contain the original complete:

- `wifi-jamming-project.cc`,
- `run-jamming.sh`,
- `results.csv`,
- `.pcap` files,
- NetAnim `.xml`,
- raw terminal logs.

Therefore the repository provides **sanitized reconstructions**, not a claim of exact source recovery.

## Recommended stronger reproduction

For research-grade repeatability, future runs should also preserve:

- NS-3 commit/version metadata,
- random seed/run identifiers,
- exact propagation-model configuration,
- full CLI parameters,
- raw FlowMonitor XML,
- PCAP files,
- generated CSV,
- plotting environment/requirements,
- checksums for artifacts.
