from helpers.math_helpers import (
    gauss_lemma,
    rationalize_float,
    rationalize_float_list,
    ruffinis_rule,
    solve_low_degree,
)
from helpers.array_helpers import unique
from helpers.string_helpers import build_polynomial
import sympy as sp


def request_input():
    polyDegree = int(input("Enter the degree of the polynomial: "))

    if polyDegree < 0:
        print("Degree must be a positive integer. Exiting")
        exit(1)

    poly: list[dict] = []
    for i in reversed(range(polyDegree + 1)):
        coef = input(f"degree {i} coefficient: ")
        poly.append({"degree": i, "coef": int(coef)})
    print(f"Polynomial: {build_polynomial(poly)}")
    return (poly, polyDegree)


def get_roots(poly: list[dict], polyDegree: int):
    ind_doef: int = poly[-1]["coef"]
    main_coef: int = poly[0]["coef"]

    if polyDegree < 3:
        return solve_low_degree(poly, polyDegree)

    # Find roots via gauss (will get only rational roots. See ())
    p_roots = unique(gauss_lemma(ind_doef, main_coef))
    p_root_pretty = rationalize_float_list(p_roots)

    print(f"Potential roots: {[sp.pretty(p_root) for p_root in p_root_pretty]}")

    roots: list[str] = []
    for p_root in p_roots:

        quotient, remainder = ruffinis_rule(poly, p_root)
        quotient_degree = max(map(lambda q_term: q_term["degree"], quotient))

        while remainder == 0:
            roots.append(rationalize_float(p_root))
            quotient_degree = max(map(lambda q_term: q_term["degree"], quotient))

            if len(roots) == polyDegree:
                return roots

            if quotient_degree < 3:
                roots.extend(solve_low_degree(quotient, quotient_degree))
                return roots

            quotient, remainder = ruffinis_rule(quotient, p_root)
            if remainder != 0:
                break

    return roots


def exec():
    poly, polyDegree = request_input()
    roots = get_roots(poly, polyDegree)

    print(f"Found roots: {[sp.pretty(root) for root in roots]}")


exec()
