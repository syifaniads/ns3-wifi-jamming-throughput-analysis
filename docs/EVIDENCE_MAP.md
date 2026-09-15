# Evidence Map

| Portfolio claim | Retained evidence | Confidence |
|---|---|---|
| Project used NS-3 3.38 | Methodology section | High |
| IEEE 802.11g fixed 6 Mbps mode | Wi-Fi configuration excerpt | High |
| Three-node AP/STA/interference topology | Topology description + NetAnim screenshot | High |
| AP at origin, STA at variable distance, interference node near midpoint | Position allocator excerpt | High |
| 1024 B UDP application packets | Client configuration excerpt | High |
| 20 Mbps / 1500 B UDP broadcast interference | `OnOffHelper` excerpt | High |
| Interference can be toggled | `--enableJamming` description | High |
| FlowMonitor used | Implementation excerpt | High |
| Throughput formula based on `rxBytes` and simulation time | Implementation excerpt | High |
| 10/30/50/80 m sweep | Bash loop excerpt | High |
| Quantitative throughput table | Results table | High |
| NetAnim used | Screenshot + text | High |
| Wireshark used for AP/STA/interference captures | Three retained screenshots + text | High |
| Exact physical continuous-wave RF jamming | Not supported by retained implementation | Not claimed |
| Exact explicit Log-Distance configuration | Narrative says so; setup excerpt does not show explicit assignment | Medium / qualified |
| Real-world over-the-air validation | Not present | Not claimed |
| Statistical repeatability across seeds | Not documented | Not claimed |

## Evidence philosophy

A portfolio statement is strongest when a reviewer can trace it to a retained artifact. Narrative interpretation is useful, but it is kept separate from implementation evidence when the two do not perfectly align.
