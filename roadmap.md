# OpenWarp Roadmap

This roadmap is organized as a sequence of scientific gates. Each gate must be treated skeptically. The project should only advance when the evidence, math, and assumptions are strong enough.

OpenWarp's current active route is **engineered traversable wormhole networks**: effective faster-than-light travel by shortening the path, not by locally moving a ship faster than light.

```txt
Normal travel:
T_normal = D / c

Wormhole travel:
T_wormhole = L_throat / c

If L_throat << D_external, the trip is effectively faster-than-light
without locally exceeding c.
```

## Phase 0 — Research Foundation

**Status:** active

Goal: build the public research map and calculate first-order viability limits.

Deliverables:

- Define the project mission
- Track known no-go theorems
- Track possible loopholes
- Build the traversable-wormhole literature path
- Run simple classical throat scaling estimates
- Run toy quantum-inequality viability scans
- Define what would count as proof

## Phase 1 — Classical Wormhole Geometry

Goal: understand the Morris-Thorne traversable wormhole framework and identify which metric choices control throat size, redshift, tidal forces, and exotic stress-energy.

Core questions:

- What does the redshift function Φ(r) control?
- What does the shape function b(r) control?
- What does the throat condition b(r0) = r0 require?
- Which metric families minimize NEC violation?
- Which choices create horizons or tidal forces that make traversal impossible?

Deliverables:

- Morris-Thorne geometry notes
- Metric family comparison table
- First metric optimizer scaffold

## Phase 2 — Negative Energy and Quantum Inequality Screening

Goal: compare classical exotic stress-energy requirements against quantum field theory limits.

Core questions:

- How much negative energy density is required at the throat?
- How does required density scale with r0?
- How does total negative mass-equivalent scale with r0?
- How do Ford-style quantum inequalities restrict support duration?
- Does increasing support time help or hurt?

Deliverables:

- `wormhole_quantum_viability.py`
- Tau-factor scan results
- Scaling-laws note

Current result:

- A 1-meter throat is astrophysical in negative-energy scale.
- The only scanned region with a non-absurd toy QI gap is near the Planck length.
- Increasing `tau_factor` makes the QI gap worse because the bound scales like τ^-4.

## Phase 3 — Semiclassical and Entanglement-Based Traversability

Goal: study whether traversability can emerge from quantum information structure rather than classical exotic matter shells.

Key literature:

- Gao-Jafferis-Wall traversable wormholes via double-trace deformation
- Maldacena-Milekhin-Popov four-dimensional traversable wormholes
- Later work on information transfer, scattering, and traversability limits

Core questions:

- What actually supplies negative averaged null energy?
- Is the throat physically traversable or only information-traversable?
- What assumptions depend on AdS/CFT, near-extremal black holes, special fermions, or extra dimensions?
- Can any mechanism survive in an approximately realistic universe?

Deliverables:

- GJW paper summary
- MMP paper summary
- Semiclassical mechanism comparison table

## Phase 4 — Metric Optimization

Goal: search across allowed metric families to reduce the exotic-energy requirement while avoiding horizons and non-traversable geometries.

Core constraints:

- `b(r0) = r0`
- `b′(r0) < 1`
- Φ(r) finite everywhere
- no horizon
- finite tidal forces
- explicit NEC / ANEC accounting

Deliverables:

- Metric optimizer prototype
- Candidate metric table
- Failure-mode catalog

## Phase 5 — Microscopic Throat Stabilization

Goal: identify whether a microscopic throat could be stabilized in a regime where classical GR is no longer enough.

Core questions:

- Does quantum gravity allow Planck-scale connected throats?
- Can entanglement maintain connectivity?
- Can topology change occur without contradiction?
- Are there constraints from causality, chronology protection, or quantum focusing?

Deliverables:

- Quantum-gravity bottleneck memo
- Candidate model comparison
- Minimum assumptions list

## Phase 6 — Chaining and Network Concepts

Goal: investigate whether many microscopic or near-microscopic throats could form a useful network without requiring one large human-scale throat.

Core questions:

- Can tiny throats be chained?
- Does chaining amplify or destroy the exotic-energy requirement?
- Does information transfer differ from matter transfer?
- Are there stability or synchronization problems?

Deliverables:

- Wormhole network architecture note
- Chaining failure analysis
- Information-vs-matter traversal memo

## Phase 7 — Mouth Transport

Goal: study the non-FTL deployment problem: one mouth is transported to a destination using ordinary sublight motion.

Core questions:

- Can moving a mouth destabilize the throat?
- What happens under acceleration?
- What causality problems appear when mouths move relativistically?
- Can a network remain synchronized?

Deliverables:

- Mouth transport constraints memo
- Causality-risk checklist

## Phase 8 — Experimental and Observational Relevance

Goal: identify any testable signatures related to microscopic wormholes, analogue systems, or semiclassical negative energy.

Possible signals:

- Quantum-channel behavior
- Analogue traversability signatures
- Precision phase shifts
- Unusual scattering / resonance behavior
- Indirect constraints from high-energy or gravitational observations

Deliverables:

- First testability memo
- Analogue-system candidate list
- Detection-before-control plan

## Rule for Advancement

OpenWarp should only move to the next gate if the previous gate produces a result that survives:

1. dimensional analysis
2. energy-condition checks
3. quantum inequality checks
4. causality review
5. stability review
6. clear statement of assumptions
