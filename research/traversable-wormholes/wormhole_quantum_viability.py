import argparse
import csv
import math
from dataclasses import dataclass

# Constants
c = 299_792_458
G = 6.67430e-11
hbar = 1.054_571_817e-34
YEAR = 365.25 * 24 * 3600

# Rough Ford-style sampled energy-density coefficient.
# This is only a toy screening estimate, not a full QFT calculation.
QI_C = 3 / (32 * math.pi**2)


@dataclass
class WormholeQuantumResult:
    tau_factor: float
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
    """Magnitude of the toy Morris-Thorne throat energy-density requirement."""
    return c**4 / (8 * math.pi * G * r0**2)


def nec_violation_scale(r0: float) -> float:
    """Magnitude of rho + p_r at the throat for the toy shape function."""
    return c**4 / (4 * math.pi * G * r0**2)


def negative_mass_equivalent(r0: float) -> float:
    """Very rough negative mass-equivalent scale for a throat of radius r0."""
    return c**2 * r0 / (2 * G)


def quantum_inequality_density_bound(tau: float) -> float:
    """Toy Ford-style sampled negative-energy density magnitude.

    Scaling only:
        |rho_QI| ~ C hbar / (c^3 tau^4)

    This is a screening number. It is not a complete curved-spacetime QFT result.
    """
    return QI_C * hbar / (c**3 * tau**4)


def classify_result(log10_anec_gap: float, r0: float) -> str:
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

    label = classify_result(log10_anec_gap, r0)

    return WormholeQuantumResult(
        tau_factor=tau_factor,
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


def default_radii() -> list[float]:
    return [
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


def print_result(r: WormholeQuantumResult) -> None:
    print("\n---")
    print(f"tau_factor: {r.tau_factor:.3e}")
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


def print_summary_table(results: list[WormholeQuantumResult]) -> None:
    print("\n\n========================================================")
    print("SUMMARY TABLE")
    print("========================================================")
    print(
        f"{'tau':>8} | "
        f"{'r0(m)':>12} | "
        f"{'log rho':>8} | "
        f"{'log QI':>8} | "
        f"{'gap':>8} | "
        f"{'log M':>8} | "
        f"{'log E':>8} | "
        f"{'label':>36}"
    )
    print("-" * 122)

    for r in results:
        print(
            f"{r.tau_factor:8.1e} | "
            f"{r.r0_m:12.3e} | "
            f"{r.log10_rho_required:8.2f} | "
            f"{r.log10_qi_allowed_density:8.2f} | "
            f"{r.log10_density_gap:8.2f} | "
            f"{r.log10_negative_mass:8.2f} | "
            f"{r.log10_negative_energy:8.2f} | "
            f"{r.viability_label:>36}"
        )


def print_best_candidates(results: list[WormholeQuantumResult]) -> None:
    lowest_total_mass = min(results, key=lambda r: r.negative_mass_equiv_kg)
    lowest_density = min(results, key=lambda r: r.rho_required_J_m3)
    lowest_qi_gap = min(results, key=lambda r: r.qi_gap_density_ratio)

    print("\n\n========================================================")
    print("BEST CANDIDATES ACROSS ALL TAU FACTORS")
    print("========================================================")

    print("\nLowest total negative mass:")
    print(f"tau_factor = {lowest_total_mass.tau_factor:.3e}")
    print(f"r0 = {lowest_total_mass.r0_m:.3e} m")
    print(f"M_neg = {lowest_total_mass.negative_mass_equiv_kg:.3e} kg")
    print(f"rho = {lowest_total_mass.rho_required_J_m3:.3e} J/m^3")
    print(f"QI gap log10 = {lowest_total_mass.log10_density_gap:.2f}")

    print("\nLowest required density:")
    print(f"tau_factor = {lowest_density.tau_factor:.3e}")
    print(f"r0 = {lowest_density.r0_m:.3e} m")
    print(f"rho = {lowest_density.rho_required_J_m3:.3e} J/m^3")
    print(f"M_neg = {lowest_density.negative_mass_equiv_kg:.3e} kg")
    print(f"QI gap log10 = {lowest_density.log10_density_gap:.2f}")

    print("\nLowest QI density gap:")
    print(f"tau_factor = {lowest_qi_gap.tau_factor:.3e}")
    print(f"r0 = {lowest_qi_gap.r0_m:.3e} m")
    print(f"rho_required = {lowest_qi_gap.rho_required_J_m3:.3e} J/m^3")
    print(f"QI_allowed_density = {lowest_qi_gap.qi_allowed_density_J_m3:.3e} J/m^3")
    print(f"QI gap ratio = {lowest_qi_gap.qi_gap_density_ratio:.3e}")
    print(f"QI gap log10 = {lowest_qi_gap.log10_density_gap:.2f}")


def print_tau_factor_comparison(
    results: list[WormholeQuantumResult],
    anchor_r0: float = 1.62e-35,
) -> None:
    matches = [r for r in results if math.isclose(r.r0_m, anchor_r0, rel_tol=0, abs_tol=anchor_r0 * 1e-12)]

    if not matches:
        return

    print("\n\n========================================================")
    print(f"TAU-FACTOR COMPARISON AT r0 = {anchor_r0:.3e} m")
    print("========================================================")
    print(
        f"{'tau_factor':>12} | "
        f"{'tau_s':>12} | "
        f"{'QI_density':>12} | "
        f"{'gap_ratio':>12} | "
        f"{'log10_gap':>10} | "
        f"{'ANEC_log10':>10}"
    )
    print("-" * 86)

    for r in sorted(matches, key=lambda item: item.tau_factor):
        print(
            f"{r.tau_factor:12.1e} | "
            f"{r.tau_s:12.3e} | "
            f"{r.qi_allowed_density_J_m3:12.3e} | "
            f"{r.qi_gap_density_ratio:12.3e} | "
            f"{r.log10_density_gap:10.2f} | "
            f"{r.log10_anec_gap:10.2f}"
        )

    print("\nInterpretation:")
    print("At fixed r0, rho_required is unchanged while QI_allowed_density scales as tau^-4.")
    print("Therefore QI gap scales as tau_factor^4. Longer support time makes the gap worse.")


def save_results_csv(
    results: list[WormholeQuantumResult],
    filename: str = "wormhole_tau_factor_scan.csv",
) -> None:
    fields = list(WormholeQuantumResult.__dataclass_fields__.keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            writer.writerow(r.__dict__)
    print(f"\nSaved CSV: {filename}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Toy Morris-Thorne traversable wormhole quantum-viability scanner."
    )
    parser.add_argument("--d-external", type=float, default=4.0e16, help="External distance in meters.")
    parser.add_argument("--l-throat", type=float, default=1_000.0, help="Throat path length in meters.")
    parser.add_argument(
        "--tau-factors",
        type=float,
        nargs="+",
        default=[1.0, 10.0, 100.0, 1000.0],
        help="Support-time factors where tau = tau_factor * r0 / c.",
    )
    parser.add_argument(
        "--csv",
        default="wormhole_tau_factor_scan.csv",
        help="Output CSV filename.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print summary tables, not every individual result.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    radii = default_radii()
    results: list[WormholeQuantumResult] = []

    print("========================================================")
    print("WORMHOLE QUANTUM VIABILITY SCAN")
    print("========================================================")
    print(f"D_external = {args.d_external:.3e} m")
    print(f"L_throat = {args.l_throat:.3e} m")
    print(f"tau_factors = {args.tau_factors}")
    print("========================================================")

    for tau_factor in args.tau_factors:
        for r0 in radii:
            result = wormhole_quantum_viability(
                r0=r0,
                D_external=args.d_external,
                L_throat=args.l_throat,
                tau_factor=tau_factor,
            )
            results.append(result)

            if not args.quiet:
                print_result(result)

    print_summary_table(results)
    print_best_candidates(results)
    print_tau_factor_comparison(results)
    save_results_csv(results, args.csv)

    print("\n\n========================================================")
    print("FINAL INTERPRETATION")
    print("========================================================")
    print("This is a toy model, but it adds the first quantum-support check.")
    print("If the QI gap is huge, the throat is not supportable by known quantum negative energy.")
    print("The near-Planck throat is the only scanned region where the toy gap is not immediately absurd.")
    print("However, that region is quantum-gravity territory, not classical engineering.")
    print("Increasing tau_factor makes the gap worse because the QI bound scales as tau^-4.")
    print("Next step: build a metric optimizer and compare alternate throat shapes.")


if __name__ == "__main__":
    main()
