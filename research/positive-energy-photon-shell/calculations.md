# Positive-Energy Photon-Shell Calculations

This file calculates the first numbers for the positive-energy photon-shell idea.

This is outside the Casimir path.

## Model

Use a spherical shell at radius `R`.

Interior:

```math
ds_-^2 = -c^2dT^2 + dr^2 + r^2d\Omega^2
```

Exterior:

```math
ds_+^2 = -\left(1-\frac{2GM}{c^2r}\right)c^2dt^2
+\left(1-\frac{2GM}{c^2r}\right)^{-1}dr^2
+r^2d\Omega^2
```

Compactness:

```math
u = \frac{GM}{c^2R}
```

Metric perturbation scale:

```math
h \sim 2u = \frac{2GM}{c^2R}
```

## Mass Needed For A Target Metric Perturbation

Solve:

```math
h = \frac{2GM}{c^2R}
```

for mass:

```math
M = \frac{hc^2R}{2G}
```

For `R = 1m`:

| Target metric perturbation `h` | Required mass `M` |
|---:|---:|
| `1e-30` | `6.73e-4 kg` |
| `1e-24` | `6.73e2 kg` |
| `1e-21` | `6.73e5 kg` |
| `1e-18` | `6.73e8 kg` |
| `1e-15` | `6.73e11 kg` |

## Shell Stress-Energy From Junction Conditions

For static flat-interior / Schwarzschild-exterior shell:

```math
\sigma = \frac{c^4}{4\pi G R}\left(1-\sqrt{1-2u}\right)
```

```math
p = \frac{c^4}{8\pi G R}\left(\frac{1-u}{\sqrt{1-2u}}-1\right)
```

Weak-field approximation:

```math
\sigma \approx \frac{Mc^2}{4\pi R^2}
```

```math
p \approx \frac{GM^2}{16\pi R^3}
```

## Example Shell Values

| Shell mass `M` | Radius `R` | Compactness `u` | Metric scale `h≈2u` | Surface energy density `sigma` | Surface pressure `p` |
|---:|---:|---:|---:|---:|---:|
| `1 kg` | `1 m` | `7.43e-28` | `1.49e-27` | `7.15e15 J/m^2` | `1.33e-12 N/m` |
| `1000 kg` | `1 m` | `7.43e-25` | `1.49e-24` | `7.15e18 J/m^2` | `1.33e-6 N/m` |
| `1e6 kg` | `1 m` | `7.43e-22` | `1.49e-21` | `7.15e21 J/m^2` | `1.33 N/m` |
| `6.73e5 kg` | `1 m` | `5.00e-22` | `1.00e-21` | `4.81e21 J/m^2` | `0.60 N/m` |
| `1e6 kg` | `10 m` | `7.43e-23` | `1.49e-22` | `7.15e19 J/m^2` | `1.33e-3 N/m` |
| `1e9 kg` | `1000 m` | `7.43e-22` | `1.49e-21` | `7.15e18 J/m^2` | `1.33e-3 N/m` |

## Photon Steering Power

A crude photon-thrust estimate:

```math
P \approx Mac
```

This assumes ideal collimated photon exhaust. Real systems are worse by an efficiency factor.

| Shell mass `M` | Acceleration `a` | Photon power `P≈Mac` |
|---:|---:|---:|
| `1 kg` | `1e-6 m/s^2` | `3.00e2 W` |
| `1 kg` | `1e-3 m/s^2` | `3.00e5 W` |
| `1 kg` | `1 m/s^2` | `3.00e8 W` |
| `1000 kg` | `1e-6 m/s^2` | `3.00e5 W` |
| `1000 kg` | `1e-3 m/s^2` | `3.00e8 W` |
| `1000 kg` | `1 m/s^2` | `3.00e11 W` |
| `1e6 kg` | `1e-6 m/s^2` | `3.00e8 W` |
| `1e6 kg` | `1e-3 m/s^2` | `3.00e11 W` |
| `1e6 kg` | `1 m/s^2` | `3.00e14 W` |

## Interpretation

This path is extremely energy-costly, but it is not like Casimir's negative-energy dead end.

It uses positive energy and classical GR.

The honest version is:

```txt
Can we design a positive-energy shell whose interior/exterior geometry and steering obey GR?
```

not:

```txt
Can we make FTL warp now?
```

## Why This Is A Better Future-Compatible Track

This testbed gives OpenWarp something real to optimize:

```math
S_{ab} \rightarrow T_{\mu\nu} \rightarrow g_{\mu\nu}
```

Then the metric optimizer can search for lower-energy shell geometries.

## Main Verdict

```txt
Positive-energy photon shells are GR-compatible.
They avoid exotic negative energy as the main source.
They are sublight and energy-costly.
They are better than Casimir for future-compatible warp research.
```
