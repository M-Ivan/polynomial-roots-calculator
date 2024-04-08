from helpers.math_helpers import (
    baskara,
    evaluate,
    gauss_teorem,
    rationalize_float,
    rationalize_float_list,
)
from helpers.array_helpers import unique
from helpers.string_helpers import build_polynomial
import sympy as sp


def request_input():
    polyGrade = int(input("Enter the grade of the polynomial: "))
    poly: list[dict] = []
    for i in range(polyGrade + 1):
        coef = input(f"Grade {i} coefficient: ")
        poly.append({"grade": i, "coef": int(coef)})
    print(f"Polynomial: {build_polynomial(poly)}")
    return (poly, polyGrade)


def get_roots(poly: list[dict], polyGrade: int):
    ind_doef: int = poly[0]["coef"]
    main_coef: int = poly[polyGrade]["coef"]

    if polyGrade == 2:
        print("Polynomial is quadratic ecuation, resolving using Baskara")
        return baskara(poly)

    # Find roots via gauss (complex roots are not supported yet)
    p_roots = unique(gauss_teorem(ind_doef, main_coef))

    p_root_pretty = rationalize_float_list(p_roots)

    print(f"Potential roots: {[sp.pretty(p_root) for p_root in p_root_pretty]}")

    roots: list[str] = []
    for p_root in p_roots:

        result = evaluate(poly, p_root)

        print(f"Result({rationalize_float(p_root)}): {result}")

        if result == 0:
            rationalized_root = rationalize_float(p_root)
            roots.append(rationalized_root)
    return roots


def exec():
    poly, polyGrade = request_input()
    roots = get_roots(poly, polyGrade)

    print(f"Found roots: {[sp.pretty(root) for root in roots]}")


exec()
