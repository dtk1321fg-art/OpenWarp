# Tau-Factor Scan Notes

This note records the first support-time scan for the wormhole quantum viability toy model.

## Setup

```txt
D_external = 4.0e16 m
L_throat = 1000 m
r0 = 1.62e-35 m
QI coefficient C = 3 / (32π²)
τ = tau_factor * r0 / c
```

The script compares a classical Morris-Thorne throat estimate against a rough Ford-style quantum inequality density estimate:

```txt
|ρ_QI| ≈ C ħ / (c³ τ⁴)
```

## Key Scaling

At fixed throat radius `r0`:

```txt
ρ_required = constant
ρ_QI ∝ τ^-4
τ ∝ tau_factor
QI gap = ρ_required / ρ_QI
QI gap ∝ tau_factor^4
```

So increasing `tau_factor` makes the gap worse.

## Planck-Scale Anchor Result

For `r0 = 1.62e-35 m`:

| tau_factor | tau_s | QI allowed density J/m³ | QI density gap ratio | log10 density gap | ANEC gap ratio | log10 ANEC gap |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.404e-44 | 4.360e111 | 4.208e0 | 0.62 | 8.416e0 | 0.93 |
| 10 | 5.404e-43 | 4.360e107 | 4.208e4 | 4.62 | 8.416e4 | 4.93 |
| 100 | 5.404e-42 | 4.360e103 | 4.208e8 | 8.62 | 8.416e8 | 8.93 |
| 1000 | 5.404e-41 | 4.360e99 | 4.208e12 | 12.62 | 8.416e12 | 12.93 |

## Interpretation

The tau scan does **not** rescue the throat.

It shows that the near-Planck case is only "close" under the shortest natural sampling time used by the toy model. Requiring longer-lived support rapidly makes the allowed negative-energy density smaller.

## Current Conclusion

The first serious OpenWarp wormhole target remains:

> Planck-scale or near-Planck stabilizable throat physics.

But this is not classical engineering. It requires quantum gravity, entanglement-based semiclassical mechanisms, or another framework that changes the assumptions of the toy calculation.

## Next Step

The next calculator should not only vary `tau_factor`.

It should vary the metric itself:

- redshift function Φ(r)
- shape function b(r)
- throat radius r0
- transition width
- ANEC integral path
- horizon / finite-redshift constraint
- tidal-force constraint

The correct next code target is a **metric optimizer** that searches for lower exotic-energy geometries while rejecting non-traversable metrics.
