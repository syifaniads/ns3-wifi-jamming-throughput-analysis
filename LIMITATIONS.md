# Limitations

This portfolio intentionally separates verified experiment evidence from broader conclusions.

## Retained-artifact limitations

- The complete original `wifi-jamming-project.cc` source file is not currently preserved in this public repository.
- The original raw `results.csv`, PCAP files, NetAnim XML, and simulation logs are not currently available here.
- The public examples are sanitized reconstructions of snippets retained in the report, not a claim of byte-for-byte source recovery.

## Experimental limitations

- The report preserves one summarized throughput value per retained condition; repeated random seeds and confidence intervals are not documented.
- The evaluated standard is IEEE 802.11g at a fixed 6 Mbps data/control mode.
- Only four distances are retained: 10, 30, 50, and 80 m.
- The interference implementation shown in the retained code is high-rate UDP broadcast traffic, not a physical continuous-wave RF jammer.
- The report does not evaluate defensive mechanisms such as channel switching, adaptive rate control, or frequency hopping.
- No physical hardware experiment is retained to validate simulation-to-reality correspondence.

## Interpretation limitations

- At 80 m, both normal and interference-enabled throughput are zero, so the effect cannot be attributed uniquely to the interference source.
- The report discusses Log-Distance propagation, but the retained setup excerpt does not explicitly show a configured `LogDistancePropagationLossModel`.
- Different report sections describe application direction differently; the retained implementation excerpt implies STA/client → AP/server.

## Generalization

The results apply to this specific NS-3 configuration. They should not be generalized to all Wi-Fi deployments, all jammer types, or modern 802.11 standards without additional experiments.
