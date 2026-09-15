# Interference / Jamming Model

## What was implemented

The retained implementation uses a third NS-3 node that transmits **high-rate UDP broadcast traffic** while the interference condition is enabled.

Representative retained configuration:

```cpp
OnOffHelper jammer(
    "ns3::UdpSocketFactory",
    InetSocketAddress(Ipv4Address("255.255.255.255"), 9)
);
jammer.SetConstantRate(DataRate("20Mbps"));
jammer.SetAttribute("PacketSize", UintegerValue(1500));
```

The experiment exposes an `--enableJamming` argument to turn the interference source on or off.

## Why this distinction matters

The report sometimes describes the experiment using broader language such as “continuous-wave / UDP flooding jamming”. The implementation excerpt retained in the report directly supports only the **UDP broadcast flooding / traffic-based interference** mechanism.

A physical continuous-wave jammer would operate differently at the RF/PHY layer and should not be claimed from this evidence.

## Interference path

```text
Legitimate STA/AP traffic
          │
          ▼
   shared 802.11 medium
          ▲
          │
20 Mbps UDP broadcast source
```

The intended interpretation is that the extra high-rate traffic increases channel occupancy/contention and reduces useful throughput available to legitimate traffic.

## Ethical boundary

This model ran inside NS-3. It is documented for defensive analysis and education; this repository does not provide instructions for disrupting real wireless systems.
