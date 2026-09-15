# Portfolio Summary

## One-line summary

Led a four-person NS-3 wireless-network project that evaluated IEEE 802.11g throughput under distance variation and simulated high-rate interference, automated repeated experiments, and validated behavior with FlowMonitor, NetAnim, Wireshark, and Python analysis.

## Role

**Syifani Adillah Salsabila — Group Lead / Ketua Kelompok & Wireless Network Simulation Contributor**

This was collaborative coursework. The leadership role is based on the project owner's confirmation; member names are verifiable from the retained report.

## CV-ready bullets

- Led a four-person wireless-network simulation project using **NS-3 3.38**, IEEE 802.11g, UDP traffic, FlowMonitor, NetAnim, and Wireshark.
- Automated interference ON/OFF experiments across **10, 30, 50, and 80 m** with Bash and generated CSV-backed throughput analysis using Python/Matplotlib.
- Measured a throughput drop from **4.58 Mbps to 2.52 Mbps at 10 m** and from **4.58 Mbps to 2.25 Mbps at 30–50 m** under the retained high-rate UDP-broadcast interference scenario.
- Performed packet-level validation using PCAP captures and documented the distinction between traffic-based interference emulation and physical RF jamming.
- Audited retained experiment evidence and documented inconsistencies around traffic direction, propagation-model wording, and the 80 m zero-throughput case instead of overclaiming results.

## Interview talking points

A reviewer can ask about:

- why a fixed `ErpOfdmRate6Mbps` baseline was useful,
- how shared-medium contention affects Wi-Fi throughput,
- why high-rate broadcast traffic can degrade legitimate traffic,
- how FlowMonitor throughput was calculated,
- why automation improves repeatability,
- what NetAnim validates versus what Wireshark validates,
- why 0 Mbps in both baseline and interference conditions at 80 m cannot be attributed solely to the interference source,
- limitations of using one retained result per condition,
- difference between simulated UDP flooding and physical-layer continuous-wave jamming.

## Relevant roles

This project is especially useful evidence for:

- Network Engineer / NOC
- Network Security Engineer
- Infrastructure Engineer
- Wireless / Telecom Engineering internship
- Security Analyst roles involving network traffic analysis
- Research / simulation-oriented networking roles

## Technologies

`NS-3` · `C++` · `IEEE 802.11g` · `UDP` · `FlowMonitor` · `Wireshark` · `NetAnim` · `Bash` · `Python` · `pandas` · `Matplotlib` · `PCAP` · `Network Security`
