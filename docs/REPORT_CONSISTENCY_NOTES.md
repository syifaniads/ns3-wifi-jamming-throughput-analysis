# Report Consistency Notes

This file documents places where the retained report's narrative and implementation excerpts are not perfectly aligned.

## 1. Application traffic direction

One narrative section describes the AP as transmitting application/video traffic toward the client.

The retained implementation excerpt instead shows:

- `UdpServerHelper server(4000)` installed on the AP,
- a client application configured on the STA.

That implies the retained application flow is **STA/client → AP/server**.

Portfolio wording therefore avoids claiming AP → STA application direction as a verified fact.

## 2. “Continuous-wave” versus UDP-flooding interference

The report discusses both continuous-wave and UDP-flooding jamming terminology.

The retained code directly shows:

- `OnOffHelper`,
- UDP socket factory,
- broadcast destination `255.255.255.255`,
- 20 Mbps rate,
- 1500-byte packets.

Therefore the implementation is described here as **traffic-based high-rate UDP broadcast interference**.

## 3. Propagation model wording

The methodology discusses the Log-Distance propagation-loss model.

The retained setup excerpt shows:

```cpp
YansWifiChannelHelper channel = YansWifiChannelHelper::Default();
```

but does not include an explicit `AddPropagationLoss(...)` call. Because the exact full source is not retained here, the portfolio treats explicit Log-Distance configuration as **report-described rather than independently source-verified**.

## 4. 80 m “100% loss” row

The report table labels the 80 m condition as `100% (Loss)`.

However, both:

- normal throughput = 0 Mbps,
- interference throughput = 0 Mbps.

Thus the row verifies connectivity collapse at 80 m in the retained runs, but not a 100% *additional* degradation caused by the interference source.

## 5. “Video traffic” terminology

The retained application snippets show generic UDP server/client behavior and packet-size/interval configuration. No retained codec, video application, or media stream is independently evidenced.

Portfolio wording therefore uses **UDP application traffic**, not “video streaming implementation”.
