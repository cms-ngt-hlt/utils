#!/usr/bin/env python3

import math
import argparse

MAXSHORT = 32768  # (short max) + 1, as in CMSSW


def phi2short(phi_rad: float) -> int:
    """
    C++ equivalent:
      p2i = ((short_max)+1)/pi
      return round(phi * p2i)
    """
    p2i = MAXSHORT / math.pi
    return int(round(phi_rad * p2i))


def short2phi(s: int) -> float:
    """
    C++ equivalent:
      i2p = pi/((short_max)+1)
      return float(s) * i2p
    """
    i2p = math.pi / MAXSHORT
    return float(s) * i2p


def approx_atan2s_P(x: float, degree: int) -> float:
    z = x * x

    if degree == 3:
        return x * (-10142.439453125 + z * 2002.0908203125)

    if degree == 5:
        return x * (-10381.9609375 + z * (3011.1513671875 + z * (-827.538330078125)))

    if degree == 7:
        return x * (
            -10422.177734375
            + z * (3349.97412109375 + z * (-1525.589599609375 + z * 406.64190673828125))
        )

    if degree == 9:
        return x * (
            -10428.984375
            + z
            * (
                3445.20654296875
                + z
                * (
                    -1879.137939453125
                    + z * (888.22314453125 + z * (-217.42669677734375))
                )
            )
        )

    raise ValueError("Degree must be one of {3, 5, 7, 9}")


def unsafe_atan2s(y: float, x: float, degree: int) -> int:
    """
    Mirrors CMSSW C++ unsafe_atan2s_impl().
    Returns an 'int' that fits in int16_t range for typical inputs,
    representing phi in 'short' angle units.
    """
    ax = abs(x)
    ay = abs(y)

    if ax + ay == 0.0:
        raise ValueError("unsafe_atan2s undefined for x = y = 0")

    r = (ax - ay) / (ax + ay)
    if x < 0:
        r = -r

    # These match CMSSW scheme:
    # pi/4  => MAXSHORT/4
    # 3pi/4 => 3*MAXSHORT/4
    pi4 = MAXSHORT // 4
    pi34 = 3 * MAXSHORT // 4

    angle = pi4 if x >= 0 else pi34
    angle += int(approx_atan2s_P(r, degree))

    if y < 0:
        angle = -angle

    return angle


def degrees_to_short(deg: float, degree: int) -> int:
    # Use atan2 approximation on the unit circle, as before.
    rad = math.radians(deg)
    x = math.cos(rad)
    y = math.sin(rad)
    return unsafe_atan2s(y, x, degree)


def main():
    parser = argparse.ArgumentParser(
        description="Fast atan2 short-angle approximation + phi<->short conversions"
    )
    parser.add_argument(
        "--degree",
        type=int,
        choices=[3, 5, 7, 9],
        default=9,
        help="Polynomial degree for approx_atan2s_P (default: 9)",
    )

    parser.add_argument(
        "--angles-deg",
        type=float,
        nargs="*",
        help="Input angles in degrees (forward: degrees -> short -> radians/degrees)",
    )

    parser.add_argument(
        "--phis-rad",
        type=float,
        nargs="*",
        help="Input phis in radians (convert via phi2short; does NOT use atan2 approximation)",
    )

    parser.add_argument(
        "--shorts",
        type=int,
        nargs="*",
        help="Input short values (inverse: short -> radians/degrees)",
    )

    args = parser.parse_args()

    if not (args.angles_deg or args.phis_rad or args.shorts):
        parser.error("Provide at least one of --angles-deg, --phis-rad, or --shorts")

    if args.angles_deg:
        print(f"\nForward (approx atan2): degrees -> short  (DEGREE={args.degree})")
        print(f"{'deg_in':>10} | {'short':>7} | {'phi_rad':>12} | {'phi_deg':>10}")
        print("-" * 52)
        for deg in args.angles_deg:
            s = degrees_to_short(deg, args.degree)
            phi = short2phi(s)
            print(f"{deg:10.3f} | {s:7d} | {phi:12.8f} | {math.degrees(phi):10.6f}")

    if args.phis_rad:
        print("\nForward (exact convert): phi_rad -> short (phi2short) -> back")
        print(
            f"{'phi_rad_in':>12} | {'short':>7} | {'phi_rad_out':>12} | {'phi_deg_out':>11}"
        )
        print("-" * 58)
        for phi_in in args.phis_rad:
            s = phi2short(phi_in)
            phi_out = short2phi(s)
            print(
                f"{phi_in:12.8f} | {s:7d} | {phi_out:12.8f} | {math.degrees(phi_out):11.6f}"
            )

    if args.shorts:
        print("\nInverse: short -> phi")
        print(f"{'short':>7} | {'phi_rad':>12} | {'phi_deg':>11}")
        print("-" * 38)
        for s in args.shorts:
            phi = short2phi(s)
            print(f"{s:7d} | {phi:12.8f} | {math.degrees(phi):11.6f}")


if __name__ == "__main__":
    main()
