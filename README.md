# OpenWarp

OpenWarp is an open-source research project exploring spacetime engineering and effective faster-than-light travel through theoretically serious path-shortening mechanisms.

The current active route is **engineered traversable wormhole networks**.

The goal is not to make a ship locally outrun light. The goal is to investigate whether spacetime can contain, create, stabilize, or connect shortcuts such that the path length through a throat is much shorter than the ordinary external distance.

```txt
Normal travel:
T_normal = D / c

Wormhole travel:
T_wormhole = L_throat / c

If L_throat << D_external, travel is effectively faster-than-light
without locally exceeding c.
```

This project does **not** claim that warp drive, traversable wormholes, or effective FTL currently exist. The goal is to map the real scientific path from known physics, semiclassical gravity, quantum inequalities, and quantum-gravity candidates toward testable statements.

## Mission

To investigate whether a stabilizable traversable shortcut through spacetime is theoretically possible, what stress-energy or quantum information structure it would require, and which assumptions block or permit such a route.

## Core Question

> Can a microscopic traversable throat be created, stabilized, and eventually networked into a spacetime shortcut without requiring impossible macroscopic negative energy?

## Active Hypothesis

The first serious target is **not** a human-scale wormhole.

A direct human-scale Morris-Thorne-style throat appears to require astrophysical negative energy. The first theoretically interesting target is instead:

> A Planck-scale or near-Planck stabilizable throat whose existence depends on quantum gravity, entanglement, or a semiclassical mechanism beyond ordinary classical general relativity.

## Why Wormholes Instead of Warp Bubbles?

Warp bubbles try to move a region through external space in an FTL-like way. That runs directly into extreme stress-energy, quantum inequality, horizon, stability, and causality problems.

A traversable wormhole network changes the target:

- Do not locally exceed the speed of light.
- Shorten the path.
- Move one mouth by ordinary sublight transport.
- Use the connected throat as the shortcut.

This does not remove the hard physics. It changes which hard physics matters most.

## Main Metric Under Study

The starting classical model is the Morris-Thorne traversable wormhole metric:

```txt
ds² = -e^(2Φ(r)) c²dt² + dr²/(1 - b(r)/r) + r²dΩ²
```

Traversability conditions:

```txt
b(r0) = r0
b′(r0) < 1
Φ(r) finite everywhere
```

Toy shape function:

```txt
Φ(r) = 0
b(r) = r0² / r
```

At the throat:

```txt
b′(r0) = -1 < 1
```

This is a toy model, not a buildable engineering design.

## Current Bottleneck

The key bottleneck is no longer simply "can negative energy exist?"

It is now:

> Can quantum gravity or an entanglement-based semiclassical model stabilize a microscopic connected throat without requiring impossible macroscopic negative energy?

## Current Status

**Phase 0: Research foundation and viability screening.**

Current active work:

- Classical Morris-Thorne throat scaling
- Negative mass-equivalent estimates
- NEC / ANEC violation estimates
- Ford-style quantum inequality toy screening
- Tau-factor support-time scan
- Literature path through Gao-Jafferis-Wall and Maldacena-Milekhin-Popov-style traversable wormholes

## Repository Structure

```txt
OpenWarp/
  README.md
  roadmap.md
  questions.md
  CONTRIBUTING.md
  literature/
    papers-to-read.md
  research/
    evidence-map.md
    no-go-theorems.md
    possible-loopholes.md
    traversable-wormholes/
      README.md
      wormhole_quantum_viability.py
      tau_factor_scan_notes.md
  experiments/
    README.md
```

## First Milestone

Create a serious public memo:

> What Actually Blocks Traversable Wormhole Engineering: Energy Conditions, Quantum Inequalities, and Quantum Gravity

## Project Rules

- Do not claim effective FTL is solved.
- Do not present toy models as engineering designs.
- Keep speculative ideas clearly labeled.
- Track no-go theorems honestly.
- Prefer falsifiable calculations over hype.
- Keep the project peaceful and scientific.

## License

This project should eventually use an open-source license. Suggested: MIT for code, CC BY 4.0 for research notes.
