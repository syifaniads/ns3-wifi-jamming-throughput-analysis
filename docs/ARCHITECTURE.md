# Architecture

## Simulation architecture

```mermaid
flowchart TB
    subgraph Wireless[NS-3 IEEE 802.11g simulation]
      AP[Node 0\nAP / UDP server]
      STA[Node 1\nSTA / UDP client]
      JAM[Node 2\n20 Mbps UDP broadcast source]
      MEDIUM((Shared wireless medium))
      AP --- MEDIUM
      STA --- MEDIUM
      JAM --> MEDIUM
    end

    CFG[CLI parameters\ndistance + enableJamming] --> Wireless
    Wireless --> FM[FlowMonitor]
    Wireless --> XML[NetAnim XML]
    Wireless --> PCAP[PCAP captures]
    FM --> CSV[results.csv]
    CSV --> PLOT[Python / Matplotlib]
    PCAP --> WS[Wireshark]
```

## Node roles

### Node 0 — Access Point

Configured using `ApWifiMac` and shown in the retained implementation as hosting a UDP server.

### Node 1 — Station

Configured using `StaWifiMac`. Its x-coordinate is varied according to the requested distance.

### Node 2 — Interference node

Configured using `AdhocWifiMac` in the retained excerpt and placed approximately halfway between AP and STA with a 5 m y-offset. It emits high-rate UDP broadcast traffic while the interference condition is enabled.

## Data plane vs analysis plane

The project deliberately separates simulation behavior from later analysis:

- **simulation plane:** Wi-Fi, UDP application traffic, interfering traffic,
- **measurement plane:** FlowMonitor and PCAP,
- **analysis plane:** CSV, pandas/Matplotlib, Wireshark, NetAnim.

This separation makes the experiment easier to automate and reason about.
