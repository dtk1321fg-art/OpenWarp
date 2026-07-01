import math
import csv
from dataclasses import dataclass

# Constants
c = 299_792_458
G = 6.67430e-11
hbar = 1.054_571_817e-34
YEAR = 365.25 * 24 * 3600

# Rough Ford-style sampled energy-density coefficient.
# This is only a toy screening estimate.
QI_C = 3 / (32 * math.pi**2)


@dataclass
class WormholeQuantumResult:
    r0_m: float
    tau_s: float
    rho_required_J_m3: float
    nec_violation_scale_J_m3: float
    anec_requirement_J_m2: float
    qi_allowed_density_J_m3: float
    qi_allowed_anec_J_m2: float
    qi_gap_density_ratio: float
    qi_gap_anec_ratio: float
    negative_mass_equiv_kg: float
    negative_energy_J: float
    normal_time_years: float
    wormhole_time_seconds: float
    shortcut_ratio: float
    log10_rho_required: float
    log10_qi_allowed_density: float
    log10_density_gap: float
    log10_anec_gap: float
    log10_negative_mass: float
    log10_negative_energy: float
    log10_shortcut_ratio: float
    viability_label: str


def rho_required_at_throat(r0: float) -> float:
    return c**4 / (8 * math.pi * G * r0**2)


def nec_violation_scale(r0: float) -> float:
    return c**4 / (4 * math.pi * G * r0**2)


def negative_mass_equivalent(r0: float) -> float:
    return c**2 * r0 / (2 * G)


def quantum_inequality_density_bound(tau: float) -> float:
    return QI_C * hbar / (c**3 * tau**4)


def classify_result(log10_density_gap: float, log10_anec_gap: float, r0: float) -> str:
    if r0 <= 2e-35:
        scale = "Planck-scale"
    elif r0 < 1e-30:
        scale = "near-Planck"
    elif r0 < 1e-18:
        scale = "subnuclear"
    elif r0 < 1e-9:
        scale = "atomic/nanoscopic"
    elif r0 < 1e-3:
        scale = "microscopic"
    else:
        scale = "macroscopic"

    if log10_anec_gap < 5:
        gap = "QI gap small-ish in toy estimate"
    elif log10_anec_gap < 20:
        gap = "QI gap huge but useful for theory"
    elif log10_anec_gap < 60:
        gap = "QI gap extreme"
    else:
        gap = "QI gap absurd"

    return f"{scale}; {gap}"


def wormhole_quantum_viability(
    r0: float,
    D_external: float,
    L_throat: float,
    tau_factor: float = 1.0,
) -> WormholeQuantumResult:
    if r0 <= 0:
        raise ValueError("r0 must be positive")
    if D_external <= 0:
        raise ValueError("D_external must be positive")
    if L_throat <= 0:
        raise ValueError("L_throat must be positive")
    if tau_factor <= 0:
        raise ValueError("tau_factor must be positive")

    tau = tau_factor * r0 / c

    rho_req = rho_required_at_throat(r0)
    nec_req = nec_violation_scale(r0)
    anec_req = nec_req * r0

    qi_density = quantum_inequality_density_bound(tau)
    qi_anec = qi_density * r0

    density_gap_ratio = rho_req / qi_density
    anec_gap_ratio = anec_req / qi_anec

    m_neg = negative_mass_equivalent(r0)
    e_neg = m_neg * c**2

    normal_time_years = (D_external / c) / YEAR
    wormhole_time_seconds = L_throat / c
    shortcut_ratio = D_external / L_throat

    log10_rho_required = math.log10(rho_req)
    log10_qi_density = math.log10(qi_density)
    log10_density_gap = math.log10(density_gap_ratio)
    log10_anec_gap = math.log10(anec_gap_ratio)
    log10_m_neg = math.log10(m_neg)
    log10_e_neg = math.log10(e_neg)
    log10_shortcut = math.log10(shortcut_ratio)

    label = classify_result(log10_density_gap, log10_anec_gap, r0)

    return WormholeQuantumResult(
        r0_m=r0,
        tau_s=tau,
        rho_required_J_m3=rho_req,
        nec_violation_scale_J_m3=nec_req,
        anec_requirement_J_m2=anec_req,
        qi_allowed_density_J_m3=qi_density,
        qi_allowed_anec_J_m2=qi_anec,
        qi_gap_density_ratio=density_gap_ratio,
        qi_gap_anec_ratio=anec_gap_ratio,
        negative_mass_equiv_kg=m_neg,
        negative_energy_J=e_neg,
        normal_time_years=normal_time_years,
        wormhole_time_seconds=wormhole_time_seconds,
        shortcut_ratio=shortcut_ratio,
        log10_rho_required=log10_rho_required,
        log10_qi_allowed_density=log10_qi_density,
        log10_density_gap=log10_density_gap,
        log10_anec_gap=log10_anec_gap,
        log10_negative_mass=log10_m_neg,
        log10_negative_energy=log10_e_neg,
        log10_shortcut_ratio=log10_shortcut,
        viability_label=label,
    )


def print_result(r: WormholeQuantumResult):
    print("\n---")
    print(f"r0_m: {r.r0_m:.3e}")
    print(f"tau_s: {r.tau_s:.3e}")
    print(f"rho_required_J_m3: {r.rho_required_J_m3:.3e}")
    print(f"NEC_violation_scale_J_m3: {r.nec_violation_scale_J_m3:.3e}")
    print(f"ANEC_requirement_J_m2: {r.anec_requirement_J_m2:.3e}")
    print(f"QI_allowed_density_J_m3: {r.qi_allowed_density_J_m3:.3e}")
    print(f"QI_allowed_ANEC_J_m2: {r.qi_allowed_anec_J_m2:.3e}")
    print(f"QI_gap_density_ratio: {r.qi_gap_density_ratio:.3e}")
    print(f"QI_gap_ANEC_ratio: {r.qi_gap_anec_ratio:.3e}")
    print(f"negative_mass_equiv_kg: {r.negative_mass_equiv_kg:.3e}")
    print(f"negative_energy_J: {r.negative_energy_J:.3e}")
    print(f"normal_time_years: {r.normal_time_years:.3e}")
    print(f"wormhole_time_seconds: {r.wormhole_time_seconds:.3e}")
    print(f"shortcut_ratio: {r.shortcut_ratio:.3e}")
    print(f"log10_rho_required: {r.log10_rho_required:.2f}")
    print(f"log10_QI_allowed_density: {r.log10_qi_allowed_density:.2f}")
    print(f"log10_density_gap: {r.log10_density_gap:.2f}")
    print(f"log10_ANEC_gap: {r.log10_anec_gap:.2f}")
    print(f"log10_negative_mass: {r.log10_negative_mass:.2f}")
    print(f"log10_negative_energy: {r.log10_negative_energy:.2f}")
    print(f"log10_shortcut_ratio: {r.log10_shortcut_ratio:.2f}")
    print(f"viability_label: {r.viability_label}")


def print_summary_table(results):
    print("\n\n========================================================")
    print("SUMMARY TABLE")
    print("========================================================")
    print(
        f"{'r0(m)':>12} | "
        f"{'log rho':>8} | "
        f"{'log QI':>8} | "
        f"{'gap':>8} | "
        f"{'log M':>8} | "
        f"{'log E':>8} | "
        f"{'label':>28}"
    )
    print("-" * 100)

    for r in results:
        print(
            f"{r.r0_m:12.3e} | "
            f"{r.log10_rho_required:8.2f} | "
            f"{r.log10_qi_allowed_density:8.2f} | "
            f"{r.log10_density_gap:8.2f} | "
            f"{r.log10_negative_mass:8.2f} | "
            f"{r.log10_negative_energy:8.2f} | "
            f"{r.viability_label:>28}"
        )


def print_best_candidates(results):
    lowest_total_mass = min(results, key=lambda r: r.negative_mass_equiv_kg)
    lowest_density = min(results, key=lambda r: r.rho_required_J_m3)
    lowest_qi_gap = min(results, key=lambda r: r.qi_gap_density_ratio)

    print("\n\n========================================================")
    print("BEST CANDIDATES")
    print("========================================================")

    print("\nLowest total negative mass:")
    print(f"r0 = {lowest_total_mass.r0_m:.3e} m")
    print(f"M_neg = {lowest_total_mass.negative_mass_equiv_kg:.3e} kg")
    print(f"rho = {lowest_total_mass.rho_required_J_m3:.3e} J/m^3")
    print(f"QI gap log10 = {lowest_total_mass.log10_density_gap:.2f}")

    print("\nLowest required density:")
    print(f"r0 = {lowest_density.r0_m:.3e} m")
    print(f"rho = {lowest_density.rho_required_J_m3:.3e} J/m^3")
    print(f"M_neg = {lowest_density.negative_mass_equiv_kg:.3e} kg")
    print(f"QI gap log10 = {lowest_density.log10_density_gap:.2f}")

    print("\nLowest QI density gap:")
    print(f"r0 = {lowest_qi_gap.r0_m:.3e} m")
    print(f"rho_required = {lowest_qi_gap.rho_required_J_m3:.3e} J/m^3")
    print(f"QI_allowed_density = {lowest_qi_gap.qi_allowed_density_J_m3:.3e} J/m^3")
    print(f"QI gap ratio = {lowest_qi_gap.qi_gap_density_ratio:.3e}")
    print(f"QI gap log10 = {lowest_qi_gap.log10_density_gap:.2f}")


def save_results_csv(results, filename="wormhole_quantum_results.csv"):
    fields = list(WormholeQuantumResult.__dataclass_fields__.keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            writer.writerow(r.__dict__)
    print(f"\nSaved CSV: {filename}")


def main():
    D_external = 4.0e16
    L_throat = 1_000
    tau_factor = 1.0

    radii = [
        1.62e-35,
        1e-34,
        1e-33,
        1e-32,
        1e-31,
        1e-30,
        1e-29,
        1e-28,
        1e-27,
        1e-26,
        1e-25,
        1e-24,
        1e-23,
        1e-22,
        1e-21,
        1e-20,
        1e-19,
        1e-18,
        1e-17,
        1e-16,
        1e-15,
        1e-12,
        1e-9,
        1e-6,
        1e-3,
        1e-2,
        1,
        1e3,
    ]

    results = []

    print("========================================================")
    print("WORMHOLE QUANTUM VIABILITY SCAN")
    print("========================================================")
    print(f"D_external = {D_external:.3e} m")
    print(f"L_throat = {L_throat:.3e} m")
    print(f"tau_factor = {tau_factor:.3e}")
    print("========================================================")

    for r0 in radii:
        r = wormhole_quantum_viability(r0, D_external, L_throat, tau_factor)
        results.append(r)
        print_result(r)

    print_summary_table(results)
    print_best_candidates(results)
    save_results_csv(results)

    print("\n\n========================================================")
    print("FINAL INTERPRETATION")
    print("========================================================")
    print("This is a toy model, but it adds the first quantum-support check.")
    print("If QI gap is huge, the throat is not supportable by known quantum negative energy.")
    print("The best theoretical target is the smallest throat with the least total negative mass,")
    print("but only if quantum gravity can handle the local density.")
    print("Next step: test tau_factor = 10, 100, 1000 and compare QI gaps.")


if __name__ == "__main__":
    main()
