# OpenWarp Research Hypotheses

This file turns OpenWarp from a general idea into a testable research program.

A hypothesis must be written so it can be attacked, weakened, improved, or falsified.

## Notation

- `g_{\mu\nu}` = spacetime metric
- `G_{\mu\nu}` = Einstein tensor, built from curvature
- `T_{\mu\nu}` = stress-energy tensor
- `\rho` = energy density measured by an observer
- `n^\mu` = observer four-vector
- `k^\mu` = null vector, used for the null energy condition
- `v_s` = warp bubble coordinate velocity
- `f(r_s)` = warp bubble shape function
- `R` = bubble radius
- `\Delta` = approximate bubble wall thickness

Einstein's field equation:

```math
G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}
```

In geometrized units where `G = c = 1`:

```math
G_{\mu\nu} = 8\pi T_{\mu\nu}
```

The central idea:

```math
\text{geometry} \leftrightarrow \text{stress-energy}
```

If OpenWarp wants engineered spacetime geometry, it must understand engineered stress-energy.

---

# Hypothesis H1 — Alcubierre-Class Negative Energy Requirement

## Statement

Any nonzero Alcubierre-style warp bubble with a nonzero wall gradient requires negative energy density in part of the wall.

## Mathematical Form

For the Alcubierre metric:

```math
ds^2 = -dt^2 + [dx - v_s f(r_s)dt]^2 + dy^2 + dz^2
```

Energy density measured by Eulerian observers can be written:

```math
\rho = -\frac{v_s^2}{32\pi}\frac{y^2+z^2}{r_s^2}\left(\frac{df}{dr_s}\right)^2
```

Therefore:

```math
v_s \neq 0,\quad \frac{df}{dr_s}\neq 0,\quad y^2+z^2>0 \Rightarrow \rho < 0
```

## Meaning

The negative energy is not random. It appears in the wall where the bubble shape changes.

## How to Attack This Hypothesis

- Check whether alternative observer frames change the conclusion.
- Compare with energy-condition analysis.
- Compare with non-Alcubierre metrics.
- Ask whether subluminal warp metrics have the same problem.

## Current Status

Strong for the original Alcubierre metric.

---

# Hypothesis H2 — Negative Energy Alone Is Insufficient

## Statement

Proving that negative energy density exists is not enough for warp-drive relevance.

## Mathematical Form

A useful system must satisfy more than:

```math
\rho(x,t) < 0
```

It must satisfy:

```math
\rho(x,t) < 0
\quad \land \quad
\text{control}(\rho)
\quad \land \quad
\text{shape}(\rho)
\quad \land \quad
\text{stability}(\rho)
\quad \land \quad
\text{scaling}(\rho)
```

In stress-energy terms:

```math
T_{\mu\nu}^{lab}(x,t) \approx \lambda T_{\mu\nu}^{target}(x,t)
```

Where:

- `T_{\mu\nu}^{lab}` = stress-energy produced in a real system
- `T_{\mu\nu}^{target}` = stress-energy required by a target warp metric
- `\lambda` = scale factor

## Meaning

A tiny effect that cannot be controlled, shaped, or scaled is evidence for physics, not evidence for propulsion.

## How to Attack This Hypothesis

Find any negative-energy system that is:

1. reproducible
2. tunable
3. spatially shapeable
4. stable
5. scalable
6. gravitationally measurable

## Current Status

Very strong. This is one of OpenWarp's main filters against hype.

---

# Hypothesis H3 — Quantum Inequalities Are the Main Scaling Barrier

## Statement

Quantum inequalities may prevent negative energy from being large enough and long-lived enough for warp-drive-scale engineering.

## General Form

A simplified way to express the idea:

```math
\int_{-\infty}^{\infty} \rho(t) W(t) dt \geq -\frac{K}{\tau^4}
```

Where:

- `W(t)` = sampling/window function
- `\tau` = sampling time
- `K` = theory-dependent positive constant

## Meaning

The longer you want negative energy to last, the smaller its allowed magnitude may become.

Short duration can allow stronger negative energy. Long duration tends to be heavily restricted.

## OpenWarp Test

Any proposed exotic stress-energy source must answer:

```math
|\rho_{negative}| \times \Delta t \quad \text{versus quantum inequality bound}
```

## Current Status

Major theoretical barrier. Needs detailed paper summaries and mathematical checks.

---

# Hypothesis H4 — Casimir Systems Are Evidence, Not Yet Engineering

## Statement

Casimir-type systems are currently better treated as evidence for vacuum-boundary effects than as usable warp-drive stress-energy sources.

## Basic Scaling Idea

For ideal parallel plates, the Casimir pressure scales roughly as:

```math
P \propto -\frac{1}{a^4}
```

Where:

- `a` = plate separation

## Meaning

The effect becomes stronger at tiny separations, but this creates engineering problems:

- surface roughness
- material limitations
- alignment
- non-ideal conductivity
- tiny usable volume
- difficulty connecting force measurement to useful spacetime curvature

## OpenWarp Test

A Casimir-related proposal becomes more serious if it shows:

```math
\frac{\partial \rho}{\partial a} \neq 0
```

and also:

```math
\nabla \rho(x) \quad \text{can be shaped intentionally}
```

## Current Status

Promising as an experimental lane, weak as direct propulsion evidence.

---

# Hypothesis H5 — Sublight Metric Engineering Is More Plausible Than FTL First

## Statement

The first real spacetime-engineering milestone is more likely to be a tiny sublight metric effect than faster-than-light travel.

## Mathematical Target

Instead of demanding:

```math
v_s > c
```

OpenWarp should first target:

```math
\delta g_{\mu\nu} \neq 0
```

Where `\delta g_{\mu\nu}` is a small engineered change in the metric.

## Meaning

The first historic result would not be a spacecraft. It would be a controlled, measurable metric perturbation.

## Experimental Version

A possible first detection goal:

```math
\Delta \phi \neq 0
```

Where `\Delta \phi` is a phase shift in an interferometer caused by the engineered stress-energy system.

## Current Status

This should be OpenWarp's long-term experimental gate.

---

# Hypothesis H6 — A Useful Warp Program Needs Target Metrics, Not Just Effects

## Statement

OpenWarp must define target stress-energy distributions before judging whether an experiment matters.

## Mathematical Form

For a target metric:

```math
g_{\mu\nu}^{target}
```

Compute:

```math
G_{\mu\nu}^{target}
```

Then infer:

```math
T_{\mu\nu}^{target} = \frac{1}{8\pi}G_{\mu\nu}^{target}
```

Then compare with lab systems:

```math
\epsilon = ||T_{\mu\nu}^{lab} - \lambda T_{\mu\nu}^{target}||
```

A smaller `\epsilon` means the lab system is closer to the target stress-energy pattern.

## Meaning

This creates a research method:

1. Pick target metric.
2. Compute required stress-energy.
3. Find candidate lab effects.
4. Compare mathematically.
5. Reject weak matches.

## Current Status

This is the backbone of OpenWarp.

---

# Hypothesis H7 — The First Real Proof Is Not a Warp Bubble

## Statement

The first realistic proof should be a controlled stress-energy experiment, not a full warp bubble.

## Minimum Proof Target

A serious first proof might look like:

```math
\exists\, T_{\mu\nu}^{lab}(x,t):
\quad
\frac{\partial T_{\mu\nu}^{lab}}{\partial u} \neq 0
```

Where `u` is a controllable experimental parameter, such as:

- plate separation
- optical state
- cavity geometry
- material property
- temperature
- field intensity

## Meaning

The first true milestone is tunability.

If no control knob exists, there is no engineering path.

## Current Status

This becomes the main experimental direction for OpenWarp.

---

# Current Priority Ranking

| Rank | Hypothesis | Why |
|---:|---|---|
| 1 | H2 | Prevents hype and defines usable exotic stress-energy |
| 2 | H3 | Tests whether scaling is blocked by quantum inequalities |
| 3 | H4 | Most realistic early experimental lane |
| 4 | H1 | Gives the historical mathematical bottleneck |
| 5 | H5 | Keeps the project focused on plausible first wins |
| 6 | H6 | Turns the project into a math-driven research program |
| 7 | H7 | Defines the first real proof target |

## Immediate Next Work

1. Summarize Pfenning and Ford.
2. Summarize Bobrick and Martire.
3. Summarize Santiago, Schuster, and Visser.
4. Expand Casimir evidence.
5. Define a target stress-energy comparison method.
6. Draft first experiment proposal around tunable vacuum-boundary systems.
