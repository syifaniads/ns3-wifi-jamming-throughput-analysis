# Wireshark Validation

## Purpose

PCAP inspection provides an independent view of what packet classes were present during the simulation.

## Station capture

The report screenshot for the Station shows received application traffic together with 802.11 management frames such as Beacons.

## Access Point capture

The AP capture shows periodic Beacon transmission and application data traffic associated with the simulated WLAN.

## Interference-node capture

The report's interference-node capture shows repeated UDP broadcast packets while the interfering condition is active.

This packet-level evidence is consistent with the retained `OnOffHelper` implementation that targets `255.255.255.255` at 20 Mbps.

## What Wireshark does not prove

Packet capture does not directly measure:

- RF energy level,
- SNR,
- channel busy ratio,
- physical continuous-wave interference,
- spectrum occupancy outside the simulation.

Those require PHY counters or RF instrumentation beyond the retained evidence.
