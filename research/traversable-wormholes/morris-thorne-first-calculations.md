# Morris-Thorne Wormhole — First Calculations

This file calculates what a simple traversable wormhole throat would theoretically require.

This is not a build plan. It is a GR scale check.

## Metric

Use the Morris-Thorne traversable wormhole metric:

```math
ds^2 = -e^{2\Phi(r)}c^2dt^2 + \frac{dr^2}{1-b(r)/r}+r^2d\Omega^2
```

where:

- `\Phi(r)` is the redshift function
- `b(r)` is the shape function
- `r_0` is the throat radius

## Traversability Conditions

The throat condition:

```math
b(r_0)=r_0
```

Flaring-out condition:

```math
b'(r_0)<1
```

No-horizon condition:

```math
\Phi(r) \text{ finite everywhere}
```

Shortcut condition:

```math
L_{throat} << D_{external}
```

## Simple Toy Shape Function

Use:

```math
\Phi(r)=0
```

```math
b(r)=\frac{r_0^2}{r}
```

Then:

```math
b(r_0)=r_0
```

and:

```math
b'(r)=-\frac{r_0^2}{r^2}
```

At the throat:

```math
b'(r_0)=-1<1
```

So the flaring condition is satisfied.

## Stress-Energy Requirement

For the Morris-Thorne metric, the energy density measured by a static observer is:

```math
\rho(r)=\frac{c^4}{8\pi G}\frac{b'(r)}{r^2}
```

For the toy shape function:

```math
\rho(r)=-\frac{c^4}{8\pi G}\frac{r_0^2}{r^4}
```

At the throat:

```math
\rho(r_0)=-\frac{c^4}{8\pi G r_0^2}
```

This is negative energy density.

The radial pressure for `\Phi=0` is:

```math
p_r(r)=-\frac{c^4}{8\pi G}\frac{b(r)}{r^3}
```

At the throat:

```math
p_r(r_0)=-\frac{c^4}{8\pi G r_0^2}
```

So:

```math
\rho(r_0)+p_r(r_0)=-\frac{c^4}{4\pi G r_0^2}<0
```

This violates the null energy condition, as expected.

## Local Negative Energy Density Scale

Numerical constant:

```math
\frac{c^4}{8\pi G} \approx 4.81545\times10^{42} J/m
```

So:

```math
|\rho(r_0)|\approx \frac{4.81545\times10^{42}}{r_0^2} J/m^3
```

## Integrated Negative Energy Scale

A rough throat-scale negative mass-equivalent is:

```math
M_{neg}\sim \frac{c^2 r_0}{2G}
```

and:

```math
E_{neg}\sim M_{neg}c^2 = \frac{c^4 r_0}{2G}
```

This is the same scale as the mass-energy associated with a Schwarzschild radius of order `r_0`.

## Scaling Table

| Throat radius `r0` | Local `|rho(r0)|` | Rough negative mass-equivalent `M_neg` | Rough negative energy `E_neg` |
|---:|---:|---:|---:|
| Planck length `1.62e-35 m` | `1.84e112 J/m^3` | `1.09e-8 kg` | `9.78e8 J` |
| Proton scale `1e-15 m` | `4.82e72 J/m^3` | `6.73e11 kg` | `6.05e28 J` |
| `1 nm` | `4.82e60 J/m^3` | `6.73e17 kg` | `6.05e34 J` |
| `1 um` | `4.82e54 J/m^3` | `6.73e20 kg` | `6.05e37 J` |
| `1 mm` | `4.82e48 J/m^3` | `6.73e23 kg` | `6.05e40 J` |
| `1 cm` | `4.82e46 J/m^3` | `6.73e24 kg` | `6.05e41 J` |
| `1 m` | `4.82e42 J/m^3` | `6.73e26 kg` | `6.05e43 J` |
| `1 km` | `4.82e36 J/m^3` | `6.73e29 kg` | `6.05e46 J` |

## Meaning

A human-sized throat in a simple Morris-Thorne model needs astronomical negative energy.

A `1 m` throat needs a negative mass-equivalent around:

```math
6.73\times10^{26}kg
```

That is around gas-giant mass scale.

So the simple macroscopic wormhole path is not an engineering problem; it is a fundamental stress-energy problem.

## Tidal Constraint

A rough tidal acceleration estimate is:

```math
a_{tidal}\sim \frac{c^2\xi}{r_0^2}
```

where `\xi` is body length.

For `\xi=2m` and `a_tidal<1g`:

```math
r_0 \gtrsim \sqrt{\frac{c^2\xi}{g}}\approx1.35\times10^8m
```

This means a naive human-comfortable throat must be enormous unless the metric is heavily optimized.

## The Real Theoretical Route

The simple wormhole metric tells us the brutal scale.

The real route is not:

```txt
build a 1 m Morris-Thorne wormhole directly
```

The real route is:

```txt
1. find or create a microscopic throat
2. stabilize it with negative averaged null energy
3. use quantum systems to keep it traversable
4. search for geometries with lower exotic energy
5. only then study enlargement or chaining
```

## Key Theoretical Working Condition

A wormhole becomes a true shortcut if:

```math
T_{arrival}=\frac{L_{throat}}{c} << \frac{D}{c}
```

and stays open if:

```math
\int T_{\mu\nu}k^\mu k^\nu d\lambda < 0
```

## OpenWarp Conclusion

```txt
The method that theoretically gives true interstellar shortcut travel is a traversable wormhole.
The mathematical blocker is the amount and control of negative null energy.
The first OpenWarp target is not a large wormhole, but a microscopic stabilizable throat model.
```
