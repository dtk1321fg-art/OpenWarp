# Quantum Viability First Results

This memo records the first OpenWarp toy scan comparing Morris-Thorne throat requirements against a rough quantum-inequality support estimate.

## Scan Setup

External distance:

```math
D_{external}=4.0\times10^{16}m
```

Internal throat path:

```math
L_{throat}=1000m
```

Shortcut factor:

```math
\frac{D}{L}=4.0\times10^{13}
```

Sampling time:

```math
\tau=\frac{r_0}{c}
```

Quantum inequality toy bound:

```math
|\rho_{QI}|\sim C\frac{\hbar}{c^3\tau^4}
```

with:

```math
C=\frac{3}{32\pi^2}
```

## Classical Requirement

Morris-Thorne toy model:

```math
\Phi(r)=0
```

```math
b(r)=\frac{r_0^2}{r}
```

Throat density magnitude:

```math
|\rho(r_0)|=\frac{c^4}{8\pi G r_0^2}
```

NEC violation scale:

```math
|\rho+p_r|=\frac{c^4}{4\pi G r_0^2}
```

Rough line-integrated ANEC requirement:

```math
|ANEC|_{req}\sim |\rho+p_r|r_0
```

## Key Results

### Best QI-gap candidate

The best toy candidate was the Planck-scale throat:

```txt
r0 = 1.62e-35 m
rho_required = 1.835e112 J/m^3
QI_allowed_density = 4.360e111 J/m^3
QI_gap_density_ratio = 4.208
QI_gap_log10 = 0.62
ANEC_gap_ratio = 8.416
M_neg = 1.091e-8 kg
E_neg = 9.803e8 J
```

Interpretation:

```txt
The Planck-scale throat is the only scanned case where the rough QI gap is not absurd.
But it sits directly in quantum-gravity territory, so classical GR and ordinary QFT are not enough.
```

### Near-Planck cases

```txt
r0 = 1e-34 m: QI gap log10 = 2.21
r0 = 1e-33 m: QI gap log10 = 4.21
r0 = 1e-32 m: QI gap log10 = 6.21
r0 = 1e-31 m: QI gap log10 = 8.21
r0 = 1e-30 m: QI gap log10 = 10.21
```

Interpretation:

```txt
Each order of magnitude increase in throat radius makes the QI density gap worse by about 2 orders of magnitude in this toy model.
```

Reason:

```math
\rho_{required}\propto r_0^{-2}
```

but:

```math
\rho_{QI}\propto \tau^{-4}\propto r_0^{-4}
```

so:

```math
\frac{\rho_{required}}{\rho_{QI}}\propto r_0^2
```

## Macroscopic Failure

For a 1 meter throat:

```txt
r0 = 1 m
rho_required = 4.815e42 J/m^3
QI_allowed_density = 3.003e-28 J/m^3
QI_gap_density_ratio = 1.603e70
M_neg = 6.733e26 kg
E_neg = 6.051e43 J
```

Interpretation:

```txt
A human-scale Morris-Thorne throat is not remotely compatible with known quantum negative-energy support in this simple model.
```

## Main Conclusion

```txt
The first theoretically serious target is not a human-scale wormhole.
The first target is a Planck-scale or near-Planck stabilizable throat.
```

The research bottleneck becomes:

```txt
Can quantum gravity or an entanglement-based semiclassical model stabilize a microscopic throat without requiring impossible macroscopic negative energy?
```

## Next Scan

Run the same calculator with:

```txt
tau_factor = 10
tau_factor = 100
tau_factor = 1000
```

This tests whether the throat must be supported over longer time windows. Larger `tau_factor` makes the QI bound stricter.

## OpenWarp Status

```txt
Current best candidate: Planck-scale stabilizable throat.
Known blocker: quantum gravity required.
Rejected path: direct macroscopic Morris-Thorne throat.
Next work: vary sampling time, compare metric families, and search for lower-exotic-energy throat geometries.
```
