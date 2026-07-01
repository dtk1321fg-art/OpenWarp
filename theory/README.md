# Theory

This folder contains the mathematical and general-relativity foundations of OpenWarp.

Main tracks:

- `metrics/` — candidate spacetime metrics
- `junction-conditions/` — thin-shell and boundary matching math
- `energy-conditions/` — WEC, NEC, DEC, SEC checks
- `stress-energy/` — stress-energy tensor models and source matching

The goal is to move from vague warp ideas to exact mathematical objects:

```math
g_{\mu\nu} \rightarrow G_{\mu\nu} \rightarrow T_{\mu\nu}
```

Every proposed concept must eventually define:

```math
T_{\mu\nu}^{source} \approx \lambda T_{\mu\nu}^{target}
```
