# Representative Simulation Snippets

These snippets are reconstructed from code excerpts retained in the final report. They are not presented as a byte-for-byte copy of the original source file.

## Nodes and positions

```cpp
NodeContainer wifiNodes;
wifiNodes.Create(3); // 0=AP, 1=STA, 2=interference node

pos->Add(Vector(0.0, 0.0, 0.0));
pos->Add(Vector(distance, 0.0, 0.0));
pos->Add(Vector(distance / 2, 5.0, 0.0));
```

## IEEE 802.11g fixed-rate configuration

```cpp
wifi.SetStandard(WIFI_STANDARD_80211g);
wifi.SetRemoteStationManager(
    "ns3::ConstantRateWifiManager",
    "DataMode", StringValue("ErpOfdmRate6Mbps"),
    "ControlMode", StringValue("ErpOfdmRate6Mbps")
);
```

## UDP server and client settings

```cpp
UdpServerHelper server(4000);
server.Install(apNode.Get(0));

client.SetAttribute("PacketSize", UintegerValue(1024));
client.SetAttribute("Interval", TimeValue(MicroSeconds(1000)));
client.SetAttribute("MaxPackets", UintegerValue(1000000));
```

## Traffic-based interference source

```cpp
OnOffHelper jammer(
    "ns3::UdpSocketFactory",
    InetSocketAddress(Ipv4Address("255.255.255.255"), 9)
);
jammer.SetConstantRate(DataRate("20Mbps"));
jammer.SetAttribute("PacketSize", UintegerValue(1500));
```

## FlowMonitor throughput calculation

```cpp
double throughput = (flow.second.rxBytes * 8.0 / 1e6) / simTime;
```

## Evidence note

The full original source is not currently retained in this public portfolio. See [../SOURCE_EVIDENCE.md](../SOURCE_EVIDENCE.md) and [../LIMITATIONS.md](../LIMITATIONS.md).
