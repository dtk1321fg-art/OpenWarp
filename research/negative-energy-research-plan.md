# Negative Energy Research Plan

This file defines OpenWarp's first serious research lane: negative energy and exotic stress-energy.

The goal is not to claim that warp drive is solved. The goal is to investigate whether known quantum systems can produce local negative energy density that is measurable, controllable, shapeable, stable, scalable, and relevant to stress-energy engineering.

## Core Research Question

> Can Casimir-type or squeezed-state quantum systems produce local negative energy density that is measurable, tunable, and relevant to stress-energy engineering?

## Why This Is the First Lane

Alcubierre-style warp metrics appear to require negative energy density in the bubble wall. But proving a mathematical requirement is not the same as proving a physical source.

OpenWarp's first job is to separate:

1. mathematically required negative energy
2. quantum-field-theory negative energy
3. experimentally measured vacuum effects
4. controllable lab stress-energy
5. warp-relevant stress-energy engineering

## Definition

Energy density measured by an observer is:

```math
\rho = T_{\mu\nu}u^\mu u^\nu
```

Where:

- `T_{\mu\nu}` is the stress-energy tensor
- `u^\mu` is the observer four-velocity
- `\rho` is the measured energy density

Negative energy means:

```math
\rho < 0
```

But OpenWarp needs more than this.

The actual target is:

```math
\rho(x,t) < 0
\quad + \quad
\text{control}
\quad + \quad
\text{shape}
\quad + \quad
\text{stability}
\quad + \quad
\text{scaling}
```

## Important Source Papers

### 1. Negative Energy Densities in Quantum Field Theory

**Author:** L. H. Ford  
**Link:** https://arxiv.org/abs/0911.3597

Why it matters:

- Reviews local negative energy density in quantum field theory.
- Explains sub-vacuum effects.
- Introduces quantum inequalities that limit magnitude and duration.

Use this paper to answer:

- What types of negative energy are allowed?
- What makes them limited?
- What experiments might detect sub-vacuum effects?

### 2. The Energy Density in the Casimir Effect

**Authors:** V. Sopova and L. H. Ford  
**Link:** https://arxiv.org/abs/quant-ph/0204125

Why it matters:

- Investigates energy density in Casimir-like systems.
- Finds that under some physically realizable conditions the negative Casimir term can dominate in a region between half-spaces.

Use this paper to answer:

- When is Casimir energy density negative?
- Is the negative region spatially meaningful?
- How does geometry affect the result?

### 3. The Quantum Interest Conjecture

**Authors:** L. H. Ford and Thomas A. Roman  
**Link:** https://arxiv.org/abs/gr-qc/9901074

Why it matters:

- Explains that negative energy pulses are constrained by positive-energy compensation.
- Suggests positive pulses must overcompensate negative pulses as separation grows.

Use this paper to answer:

- Can negative energy be isolated?
- Can negative energy be stored?
- What time restrictions appear?

## Lane A — Casimir Systems

### Basic Formula

For ideal parallel conducting plates, the Casimir energy per unit area is:

```math
\frac{E}{A} = -\frac{\pi^2\hbar c}{720a^3}
```

Approximate energy density:

```math
\rho_{Casimir} \approx -\frac{\pi^2\hbar c}{720a^4}
```

Where:

- `a` is the plate separation
- `\hbar` is reduced Planck's constant
- `c` is the speed of light

### Control Hypothesis

```math
H_C: \frac{\partial \rho_{Casimir}}{\partial a} \neq 0
```

Meaning:

> Changing plate separation changes the negative-energy-like density.

### Why This Matters

Casimir systems give a possible control knob: geometry.

### Weaknesses

- Effects are tiny.
- Real plates are not ideal.
- Surface roughness matters.
- Material properties matter.
- The region is microscopic.
- The stress-energy pattern is not automatically warp-like.
- Force measurement is not the same as useful spacetime curvature.

### Research Tasks

1. Compute `\rho_{Casimir}` for different plate separations.
2. Compare ideal vs real-material assumptions.
3. Study whether geometry can shape the energy density.
4. Identify measurement methods.
5. Ask whether the effect couples gravitationally in any measurable way.

## Lane B — Squeezed States

### Hypothesis

```math
H_S: \langle T_{00} \rangle_{squeezed} < \langle T_{00} \rangle_{vacuum}
```

Meaning:

> A squeezed quantum state may locally reduce energy density or fluctuations below the ordinary vacuum reference.

### Why This Matters

Squeezed states are real tools in quantum optics and precision measurement. They may be relevant to sub-vacuum phenomena.

### Weaknesses

- Effects are temporary.
- Effects are constrained.
- Shape control may be difficult.
- Scaling may be extremely limited.
- Translating optical sub-vacuum effects into gravitational stress-energy is hard.

### Research Tasks

1. Define which stress-energy component is affected.
2. Identify experiments using squeezed light.
3. Determine whether the effect is energy density, field variance, or measurement noise suppression.
4. Compare with quantum inequality limits.
5. Ask if spatial shaping is possible.

## Lane C — Quantum Inequalities

### Simplified Form

```math
\int_{-\infty}^{\infty}\rho(t)W(t)dt \geq -\frac{K}{\tau^4}
```

Where:

- `W(t)` is a sampling/window function
- `\tau` is the sampling time
- `K` is a positive constant depending on the field and theory

### Meaning

Quantum theory may allow local negative energy, but it does not allow unlimited negative energy.

Usually:

> The longer negative energy lasts, the weaker it must be.

### Research Hypothesis

```math
H_QI: |\rho_-|\Delta t \text{ is bounded by quantum inequalities}
```

### Research Tasks

1. Summarize Ford's negative energy review.
2. Summarize Ford and Roman's quantum interest paper.
3. Identify the strongest bound relevant to Casimir-like systems.
4. Identify the strongest bound relevant to squeezed states.
5. Compare any proposed negative-energy source against the bound.

## Evidence Ranking Table

| Effect | Equation | Evidence status | Control knob | Main weakness | OpenWarp relevance |
|---|---|---|---|---|---|
| Casimir effect | `rho ~ -pi^2 hbar c / (720a^4)` | experimentally connected to real force measurements; energy-density interpretation requires care | plate separation, geometry, material | tiny, microscopic, real-material limits | best first experimental lane |
| Squeezed states | `<T00>_squeezed < <T00>_vacuum` | real quantum optics field; exact energy-density claim must be checked | optical state, squeezing parameter | temporary, constrained, hard to scale | possible sub-vacuum lane |
| Quantum inequalities | `int rho W dt >= -K/tau^4` | strong theoretical constraint | not a control knob; a limit | may kill scaling | main wall |
| Quantum interest | positive pulse must compensate negative pulse | theoretical constraint in QFT | not a control knob; a limit | blocks isolation/storage | important for feasibility |
| Alcubierre requirement | `rho < 0` in wall | mathematical requirement of original metric | shape function and velocity in metric | no known physical source | target comparison |

## Five-Day Starter Plan

### Day 1 — Define the Question

Write the exact question:

> Can known quantum systems produce local negative energy density that is measurable, tunable, and relevant to stress-energy engineering?

Output:

- one paragraph definition
- list of candidate systems
- list of what would count as proof

### Day 2 — Casimir Math

Use:

```math
\rho_{Casimir} \approx -\frac{\pi^2\hbar c}{720a^4}
```

Calculate for:

```math
a = 1nm, 10nm, 100nm, 1\mu m
```

Output:

- table of energy densities
- comment on scaling
- note real-material limitations

### Day 3 — Quantum Inequality Wall

Read Ford's review and Ford-Roman quantum interest.

Output:

- one-page explanation of quantum inequalities
- one-page explanation of quantum interest
- list of limits any proposal must pass

### Day 4 — Squeezed States

Define what squeezed states actually lower:

- energy density?
- field variance?
- measurement noise?
- local stress-energy expectation?

Output:

- one-page squeezed-state summary
- list of possible experiments
- list of uncertainties

### Day 5 — OpenWarp Mini-Report

Title:

**Can the Casimir Effect Count as Negative Energy Evidence for OpenWarp?**

Expected conclusion:

> Yes, as evidence for local negative-energy-like quantum-vacuum effects. No, as direct evidence for warp propulsion. Maybe, as a tunable experimental lane for stress-energy engineering.

## What Would Count as Progress?

A result becomes more important if it shows:

```math
\frac{\partial T_{\mu\nu}^{lab}}{\partial u} \neq 0
```

Meaning stress-energy changes when we control parameter `u`.

A stronger result would show shaping:

```math
\nabla T_{\mu\nu}^{lab}(x,t) \neq 0
```

A much stronger result would show target similarity:

```math
T_{\mu\nu}^{lab}(x,t) \approx \lambda T_{\mu\nu}^{warp}(x,t)
```

The strongest early result would show measurable spacetime coupling:

```math
T_{\mu\nu}^{lab} \rightarrow \delta g_{\mu\nu}^{measurable}
```

## What Would Count as Failure?

A negative-energy lane is weak if:

- it cannot define `T_{\mu\nu}`
- it cannot be measured
- it cannot be tuned
- it cannot be shaped
- it violates quantum inequality limits
- it cannot scale
- it only creates an analogue effect, not real stress-energy
- it confuses force, field variance, and energy density

## Immediate Next File To Create

After this plan, create:

```txt
research/casimir-first-calculations.md
```

That file should calculate the Casimir energy density for several plate gaps and explain why scaling is both promising and brutal.
