# Metrics

This folder stores candidate spacetime metrics for OpenWarp.

Metrics are not ideas. They are mathematical objects.

For every candidate metric, OpenWarp should compute:

```math
g_{\mu\nu}
```

```math
G_{\mu\nu}
```

```math
T_{\mu\nu} = \frac{c^4}{8\pi G}G_{\mu\nu}
```

Then check:

```math
\rho = T_{\mu\nu}u^\mu u^\nu
```

and energy conditions.

## Candidate Metric Families

1. Alcubierre-style shift metrics
2. Natario-style zero-expansion metrics
3. Bobrick-Martire positive-energy sublight shell metrics
4. Positive-energy photon-shell / Kinnersley-exterior metrics
5. Linearized weak-field shell metrics
6. Analogue-gravity metrics for simulation only

## Rule

A candidate metric is not serious until it has:

```txt
metric -> Einstein tensor -> stress-energy tensor -> energy-condition check -> source comparison
```
