# Traversable Wormholes Research Track

This folder contains OpenWarp's active wormhole-network research.

## Core Idea

Do not make a ship locally move faster than light.

Make the path shorter.

```txt
Normal travel:
T_normal = D / c

Wormhole travel:
T_wormhole = L_throat / c
```

If `L_throat << D_external`, then travel can be effectively faster-than-light without locally violating the speed of light.

## Current Research Target

The first serious target is **not** a human-scale traversable wormhole.

A direct 1-meter Morris-Thorne-style throat has an astrophysical negative-energy requirement. The current target is therefore:

> Planck-scale or near-Planck throat viability.

This is not an engineering design. It is a bottleneck search.

## Starting Metric

```txt
ds² = -e^(2Φ(r)) c²dt² + dr²/(1 - b(r)/r) + r²dΩ²
```

Traversability conditions:

```txt
b(r0) = r0
b′(r0) < 1
Φ(r) finite everywhere
```

Toy model:

```txt
Φ(r) = 0
b(r) = r0² / r
```

At the throat:

```txt
b′(r0) = -1 < 1
```

## Current Calculator

`wormhole_quantum_viability.py`

The script compares:

1. classical throat energy requirements
2. negative mass-equivalent
3. NEC / ANEC violation scale
4. a rough Ford-style quantum inequality density bound
5. shortcut ratio for `D_external / L_throat`
6. tau-factor support-time scaling

The QI estimate used is:

```txt
|ρ_QI| ≈ C ħ / (c³ τ⁴)

C = 3 / (32π²)
τ = tau_factor * r0 / c
```

## Key Result So Far

For `r0 = 1.62e-35 m`, `D_external = 4.0e16 m`, `L_throat = 1000 m`, and `tau_factor = 1`:

```txt
rho_required ≈ 1.835e112 J/m³
QI_allowed_density ≈ 4.360e111 J/m³
QI_gap_density_ratio ≈ 4.208
ANEC_gap_ratio ≈ 8.416
M_neg ≈ 1.091e-8 kg
E_neg ≈ 9.803e8 J
```

This is the only scanned region where the toy QI gap is not absurd, but it is directly in quantum-gravity territory.

## Tau-Factor Warning

Increasing `tau_factor` makes the QI gap worse.

Reason:

```txt
ρ_required ∝ r0^-2
ρ_QI ∝ τ^-4
τ = tau_factor * r0 / c
```

So at fixed `r0`:

```txt
QI gap ∝ tau_factor^4
```

This means longer support time is not a simple solution. It tightens the allowed negative-energy bound.

## Research Sequence

1. Create or obtain a microscopic connected wormhole-mouth pair.
2. Stabilize the throat using negative averaged null energy or a quantum-gravity equivalent.
3. Keep the redshift function finite so there is no horizon.
4. Enlarge or chain throats only if negative-energy scaling can be solved.
5. Move one mouth to a destination using ordinary sublight transport.
6. Use the throat as an interstellar shortcut.

## Next Work

1. Run `tau_factor = 1, 10, 100, 1000`.
2. Compare QI gaps under longer support times.
3. Add alternate metric families to see if exotic energy can be reduced.
4. Study Gao-Jafferis-Wall traversable wormholes.
5. Study Maldacena-Milekhin-Popov four-dimensional traversable wormholes.
6. Build a metric optimizer that searches for lower negative-energy throat shapes.
7. Track all assumptions and failure modes.
