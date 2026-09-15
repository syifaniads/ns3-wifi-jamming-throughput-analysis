# Experiment Design

## Research question

How do **distance** and a **high-rate interfering transmitter** affect throughput in a controlled IEEE 802.11g NS-3 topology?

## Experimental variables

### Independent variables

1. **AP–STA distance:** 10 m, 30 m, 50 m, 80 m.
2. **Interference state:** OFF / ON.

### Controlled parameters retained in the report

- NS-3 3.38.
- IEEE 802.11g.
- Constant data/control mode: `ErpOfdmRate6Mbps`.
- Three nodes: AP, STA, and interference node.
- STA/client packet size: 1024 B.
- STA/client interval: 1000 µs.
- Interference source: 20 Mbps UDP broadcast.
- Interference packet size: 1500 B.

### Primary output

Throughput in Mbps, derived from received bytes over simulation time.

The report also states that FlowMonitor captured transmitted, received, and lost packets.

## Topology

The retained design places:

- AP at `(0, 0, 0)`,
- STA at `(distance, 0, 0)`,
- interference node near the communication path at `(distance/2, 5, 0)`.

This means the interference source moves relative to the AP/STA geometry as the tested distance changes.

## Experimental sweep

Eight logical combinations are produced:

| Distance | Normal | Interference ON |
|---:|---|---|
| 10 m | run | run |
| 30 m | run | run |
| 50 m | run | run |
| 80 m | run | run |

The Bash automation runs both conditions at every distance and appends `RESULT` output to a CSV.

## Validation layers

The project uses several evidence channels rather than relying on one metric:

1. **FlowMonitor** — quantitative packet/throughput metrics.
2. **NetAnim** — spatial/topological visualization.
3. **PCAP + Wireshark** — packet-level inspection of AP, STA, and interference-node traffic.
4. **CSV + Matplotlib** — comparative throughput visualization.

## Scope boundary

The project is a **simulation study**. It does not establish real-world RF range, hardware susceptibility, or production WLAN behavior. See [LIMITATIONS.md](LIMITATIONS.md).
