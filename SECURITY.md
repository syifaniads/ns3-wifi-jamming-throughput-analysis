# Security & Ethical Use

## Scope

This repository documents a **simulated** wireless-network experiment performed in NS-3. It is intended for defensive analysis, education, and portfolio review.

## No real-world disruption claim

The project does not claim that the team:

- transmitted interference over real RF spectrum,
- attacked third-party wireless infrastructure,
- bypassed wireless authentication,
- disrupted any live network.

The retained implementation emulates interference through high-rate UDP broadcast traffic inside the simulator.

## Public-artifact policy

Do not commit:

- private keys or certificates,
- cloud credentials,
- real wireless credentials,
- student IDs,
- private PCAPs containing unrelated user traffic,
- machine-specific secrets or tokens.

## Safe reproduction

Reproduce experiments only inside isolated simulators or authorized test environments. Any physical wireless-security testing must comply with applicable law, spectrum regulation, and explicit authorization.
