# Metric Optimizer

This folder will contain code and notes for searching candidate metrics.

The goal is to stop guessing.

Instead of asking:

```txt
Can this one warp metric work?
```

ask:

```txt
What metric minimizes impossible stress-energy requirements?
```

## Objective Function

A first objective function:

```math
J[g] =
w_1\int |\rho_-(g)|dV
+w_2\int |NEC_-(g)|dV
+w_3\int \|T_{\mu\nu}^{source}-\lambda T_{\mu\nu}^{target}\|^2dV
+w_4\mathcal{C}_{causal}
+w_5\mathcal{C}_{stability}
```

Low `J` means the metric is more physically interesting.

## Candidate Search Parameters

- shell radius `R`
- wall thickness `Delta R`
- shift-vector profile
- lapse profile
- shell compactness
- source tensor family
- allowed positive/negative energy constraints

## Output

Every run should output:

```txt
metric parameters
maximum energy density
integrated exotic energy
energy-condition violations
source-match score
stability flags
```

## First Target

Start with positive-energy sublight shell metrics and compare them against:

- Casimir stress-energy
- positive mass shell stress-energy
- photon-radiation stress-energy
- dynamic vacuum systems
