# Israel Thin-Shell Junction Conditions

This note defines the mathematical tool OpenWarp will use for positive-energy shell models.

## Purpose

If we want a flat interior and curved exterior, we must match two spacetime regions across a shell.

This is exactly what junction conditions are for.

## Setup

Interior metric:

```math
g^-_{\mu\nu}
```

Exterior metric:

```math
g^+_{\mu\nu}
```

Shell hypersurface:

```math
\Sigma
```

Induced shell metric:

```math
h_{ab}
```

Extrinsic curvatures on each side:

```math
K^-_{ab}, \quad K^+_{ab}
```

Jump across the shell:

```math
[K_{ab}] = K^+_{ab} - K^-_{ab}
```

Trace jump:

```math
[K] = h^{ab}[K_{ab}]
```

## Israel Junction Formula

```math
S_{ab} = -\frac{c^4}{8\pi G}\left([K_{ab}] - h_{ab}[K]\right)
```

where `S_ab` is the surface stress-energy tensor of the shell.

This tells us what material shell is required to stitch the inside and outside geometries together.

## Static Flat-Interior / Schwarzschild-Exterior Shell

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

Define compactness:

```math
u = \frac{GM}{c^2R}
```

Surface energy density:

```math
\sigma = \frac{c^4}{4\pi G R}\left(1-\sqrt{1-2u}\right)
```

Surface pressure/tension scale:

```math
p = \frac{c^4}{8\pi G R}\left(\frac{1-u}{\sqrt{1-2u}}-1\right)
```

Weak-field approximations:

```math
\sigma \approx \frac{Mc^2}{4\pi R^2}
```

```math
p \approx \frac{GM^2}{16\pi R^3}
```

## Energy Condition Check

A basic shell-energy sanity check is:

```math
\sigma \geq 0
```

Dominant-energy shell condition:

```math
\sigma \geq |p_i|
```

for each principal surface pressure `p_i`.

## OpenWarp Use

This folder is for checking whether a candidate shell is physically allowed.

Pipeline:

```txt
choose interior metric
choose exterior metric
choose shell radius and motion
compute K_ab jumps
compute S_ab
check energy conditions
compare with realistic materials/energy sources
```
