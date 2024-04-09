from helpers.math_helpers import (
    baskara,
    evaluate,
    gauss_teorem,
    rationalize_float,
    rationalize_float_list,
    ruffinis_rule,
    resolve_low_grade,
)
from helpers.array_helpers import unique
from helpers.string_helpers import build_polynomial
import sympy as sp


def request_input():
    polyGrade = int(input("Enter the grade of the polynomial: "))
    poly: list[dict] = []
    for i in reversed(range(polyGrade + 1)):
        coef = input(f"Grade {i} coefficient: ")
        poly.append({"grade": i, "coef": int(coef)})
    print(f"Polynomial: {build_polynomial(poly)}")
    return (poly, polyGrade)


def get_roots(poly: list[dict], polyGrade: int):
    ind_doef: int = poly[-1]["coef"]
    main_coef: int = poly[0]["coef"]

    if polyGrade < 3:
        return resolve_low_grade(poly, polyGrade)

    # Find roots via gauss (will get only rational roots. See ())
    p_roots = unique(gauss_teorem(ind_doef, main_coef))
    p_root_pretty = rationalize_float_list(p_roots)

    print(f"Potential roots: {[sp.pretty(p_root) for p_root in p_root_pretty]}")

    roots: list[str] = []
    for p_root in p_roots:

        quotient, remainder = ruffinis_rule(poly, p_root)
        quotient_grade = max(map(lambda q_term: q_term["grade"], quotient))

        while remainder == 0:
            roots.append(rationalize_float(p_root))
            quotient_grade = max(map(lambda q_term: q_term["grade"], quotient))

            if quotient_grade < 3:
                roots.extend(resolve_low_grade(quotient, quotient_grade))
                return roots

            quotient, remainder = ruffinis_rule(quotient, p_root)

            if remainder != 0:
                break

    return roots


def exec():
    poly, polyGrade = request_input()
    roots = get_roots(poly, polyGrade)

    print(f"Found roots: {[sp.pretty(root) for root in roots]}")


exec()
