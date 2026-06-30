# Casimir First Calculations

This file performs OpenWarp's first numerical calculation for negative-energy research.

The goal is to estimate the ideal Casimir energy density between two perfectly conducting parallel plates and see how strongly it depends on plate separation.

## Formula

For ideal parallel conducting plates, the Casimir energy per unit area is:

```math
\frac{E}{A} = -\frac{\pi^2 \hbar c}{720a^3}
```

Dividing by the gap `a` gives the approximate energy density:

```math
\rho_{Casimir} \approx -\frac{\pi^2 \hbar c}{720a^4}
```

Where:

- `a` = plate separation
- `\hbar = 1.054571817 \times 10^{-34} J\cdot s`
- `c = 299792458 m/s`

The constant is:

```math
\frac{\pi^2 \hbar c}{720} \approx 4.33375 \times 10^{-28} J\cdot m
```

So:

```math
\rho_{Casimir} \approx -\frac{4.33375 \times 10^{-28}}{a^4} J/m^3
```

## Results

| Plate gap `a` | `a` in meters | Ideal Casimir energy density `rho` | Mass-equivalent density `rho/c^2` |
|---:|---:|---:|---:|
| 1 nm | `1.0e-9 m` | `-4.33375e8 J/m^3` | `-4.82195e-9 kg/m^3` |
| 10 nm | `1.0e-8 m` | `-4.33375e4 J/m^3` | `-4.82195e-13 kg/m^3` |
| 100 nm | `1.0e-7 m` | `-4.33375 J/m^3` | `-4.82195e-17 kg/m^3` |
| 1 micrometer | `1.0e-6 m` | `-4.33375e-4 J/m^3` | `-4.82195e-21 kg/m^3` |

## Scaling Result

The energy density scales as:

```math
\rho_{Casimir} \propto -\frac{1}{a^4}
```

So when the gap gets 10 times larger, the magnitude gets:

```math
10^4 = 10000
```

times weaker.

That means:

```math
a \rightarrow 10a \quad \Rightarrow \quad |\rho| \rightarrow \frac{|\rho|}{10000}
```

## Interpretation

The numbers show both why the Casimir effect is interesting and why it is brutal.

### Why it is interesting

At nanometer scales, the ideal negative energy density can become large compared with everyday energy densities.

At `1 nm`:

```math
\rho \approx -4.33 \times 10^8 J/m^3
```

That looks large as an energy density.

### Why it is brutal

The volume is microscopic, and the effect collapses rapidly with distance.

At `1 micrometer`:

```math
\rho \approx -4.33 \times 10^{-4} J/m^3
```

That is tiny.

So the problem is not just producing negative energy density. The real problem is producing enough of it in a useful volume and shape.

## First OpenWarp Conclusion

The Casimir effect is useful for OpenWarp as:

- evidence that quantum vacuum systems can have negative-energy-like regions
- a controllable geometry-based research lane
- a first mathematical test case for negative energy scaling

But it is not yet evidence for:

- a warp bubble
- useful propulsion
- macroscopic spacetime engineering
- scalable exotic matter

## First Hypothesis Update

The Casimir control hypothesis is:

```math
H_C: \frac{\partial \rho_{Casimir}}{\partial a} \neq 0
```

Using:

```math
\rho_{Casimir} = -\frac{K}{a^4}
```

where:

```math
K = \frac{\pi^2\hbar c}{720}
```

The derivative is:

```math
\frac{\partial \rho_{Casimir}}{\partial a} = \frac{4K}{a^5}
```

Since:

```math
K > 0
```

then:

```math
\frac{\partial \rho_{Casimir}}{\partial a} > 0
```

Meaning:

> As the plate gap increases, the negative energy density becomes less negative.

This confirms that plate separation is a real mathematical control parameter in the ideal model.

## Next Research Questions

1. How does the ideal formula change for real materials?
2. What happens with finite plate size?
3. How much do surface roughness and temperature matter?
4. Can geometry shape the negative energy region?
5. Is the stress-energy tensor pattern even close to a warp-relevant shell?
6. Could any measurable gravitational effect come from a Casimir system?
7. Do quantum inequality bounds allow scaling beyond microscopic systems?

## Next File

The next file should be:

```txt
research/casimir-real-world-limits.md
```

That file should study why ideal parallel-plate Casimir calculations are not enough for real experiments.
