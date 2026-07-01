# Sublight Shell — First Calculations

This file runs OpenWarp's first calculation for a future-compatible sublight shell target.

The purpose is to compare a rough warp-like shell stress-energy demand against the strongest ideal Casimir density we calculated earlier.

This is **not** an exact general-relativity solution. It is an order-of-magnitude stress-energy scale check.

## Core Question

Can a known negative-energy source, such as an ideal 1 nm Casimir cavity, reach the local energy-density scale needed for even a very weak sublight warp-like shell?

## Approximate Target Density

For an Alcubierre-like shell, a rough local energy-density scale is:

```math
|\rho_{target}| \sim \frac{c^4}{32\pi G}\frac{\beta^2}{\Delta R^2}
```

where:

- `\beta = v/c`
- `\Delta R` is wall thickness
- `c` is the speed of light
- `G` is Newton's gravitational constant

The constant is:

```math
\frac{c^4}{32\pi G} \approx 1.20386 \times 10^{42} \frac{J}{m}
```

So:

```math
|\rho_{target}| \sim 1.20386 \times 10^{42}\frac{\beta^2}{\Delta R^2} J/m^3
```

## Comparison Source: Best Ideal Casimir Case

For a 1 nm ideal Casimir gap:

```math
|\rho_{Casimir,1nm}| \approx 4.33375 \times 10^8 J/m^3
```

This is the best aggressive ideal case used so far.

## Target Density Table

| Wall thickness `Delta R` | Speed `beta = v/c` | Target density `|rho_target|` | Ratio vs 1 nm Casimir |
|---:|---:|---:|---:|
| `1 um` | `1` | `1.20386e54 J/m^3` | `2.78e45 x` |
| `1 um` | `1e-3` | `1.20386e48 J/m^3` | `2.78e39 x` |
| `1 um` | `1e-6` | `1.20386e42 J/m^3` | `2.78e33 x` |
| `1 um` | `1e-9` | `1.20386e36 J/m^3` | `2.78e27 x` |
| `1 mm` | `1` | `1.20386e48 J/m^3` | `2.78e39 x` |
| `1 mm` | `1e-3` | `1.20386e42 J/m^3` | `2.78e33 x` |
| `1 mm` | `1e-6` | `1.20386e36 J/m^3` | `2.78e27 x` |
| `1 mm` | `1e-9` | `1.20386e30 J/m^3` | `2.78e21 x` |
| `1 m` | `1` | `1.20386e42 J/m^3` | `2.78e33 x` |
| `1 m` | `1e-3` | `1.20386e36 J/m^3` | `2.78e27 x` |
| `1 m` | `1e-6` | `1.20386e30 J/m^3` | `2.78e21 x` |
| `1 m` | `1e-9` | `1.20386e24 J/m^3` | `2.78e15 x` |
| `1 km` | `1` | `1.20386e36 J/m^3` | `2.78e27 x` |
| `1 km` | `1e-3` | `1.20386e30 J/m^3` | `2.78e21 x` |
| `1 km` | `1e-6` | `1.20386e24 J/m^3` | `2.78e15 x` |
| `1 km` | `1e-9` | `1.20386e18 J/m^3` | `2.78e9 x` |

## Meaning Of The Table

Even extremely slow shell motion is far beyond ideal Casimir density if the wall thickness is laboratory sized.

For example, with:

```math
\Delta R = 1m
```

and:

```math
\beta = 10^{-9}
```

which is only:

```math
v \approx 0.3m/s
```

we still need:

```math
|\rho_{target}| \sim 10^{24} J/m^3
```

That is still about:

```math
2.78 \times 10^{15}
```

or **quadrillions of times stronger** than the ideal 1 nm Casimir density.

## What Speed Would Casimir Match?

Solve:

```math
|\rho_{target}| = |\rho_{Casimir,1nm}|
```

for `\beta`:

```math
\beta_{match}=\sqrt{\frac{|\rho_{Casimir}|\Delta R^2}{c^4/(32\pi G)}}
```

Results:

| Wall thickness `Delta R` | `beta_match` | speed `v_match` |
|---:|---:|---:|
| `1 um` | `1.90e-23` | `5.69e-15 m/s` |
| `1 mm` | `1.90e-20` | `5.69e-12 m/s` |
| `1 m` | `1.90e-17` | `5.69e-9 m/s` |
| `1 km` | `1.90e-14` | `5.69e-6 m/s` |
| `1000 km` | `1.90e-11` | `5.69e-3 m/s` |
| `1 billion m` | `1.90e-8` | `5.69 m/s` |

## Wall Thickness Needed To Match Casimir

Solve for wall thickness:

```math
\Delta R_{needed}=\beta\sqrt{\frac{c^4/(32\pi G)}{|\rho_{Casimir}|}}
```

Results:

| Speed `beta` | Speed approx | Needed wall thickness to match 1 nm Casimir |
|---:|---:|---:|
| `1` | speed of light | `5.27e16 m` |
| `1e-3` | `300,000 m/s` | `5.27e13 m` |
| `1e-6` | `300 m/s` | `5.27e10 m` |
| `1e-9` | `0.3 m/s` | `5.27e7 m` |
| `1e-12` | `0.0003 m/s` | `5.27e4 m` |

This is the killer result.

Even for walking-speed or slower shell motion, Casimir-strength density only matches the toy target if the wall thickness becomes planetary or astronomical.

## Gravitational Signal From The 1 mm Toy Casimir Shell

Earlier we estimated a 1 mm radius, 1 micrometer thick, 1 nm-gap ideal stacked Casimir shell:

```math
E_{stack} \approx -5.45 \times 10^{-3}J
```

Mass-equivalent:

```math
m = \frac{E}{c^2} \approx -6.06 \times 10^{-20}kg
```

Equivalent Schwarzschild-radius scale:

```math
r_s = \frac{2G|E|}{c^4} \approx 9.0 \times 10^{-47}m
```

Dimensionless metric perturbation near `R = 1mm`:

```math
h \sim \frac{r_s}{R} \approx 9.0 \times 10^{-44}
```

This is effectively impossible to detect gravitationally with any current or near-term instrument.

## Main Result

Casimir shells are useful for stress-energy shaping research.

They are not useful as direct metric-motion engines.

The honest testbed goal must be:

```txt
Measure and shape renormalized vacuum stress-energy.
```

not:

```txt
Move a spacetime bubble.
```

## Future-Compatible Direction

The future-compatible OpenWarp route is:

1. Use Casimir systems to test shell-shaped negative renormalized energy.
2. Use dynamic Casimir systems to test time-dependent vacuum-state control.
3. Build a metric optimizer to search for targets far below Alcubierre demands.
4. Use source matching to compare real systems against target stress-energy tensors.
5. Avoid claiming propulsion until metric perturbations become measurable.

## Updated Verdict

```txt
Casimir can support the mathematics of a negative-energy shell testbed.
Casimir cannot directly support a sublight warp-motion shell at useful scale.
The next breakthrough must come from metric optimization, a new stress-energy source, or new physics.
```
