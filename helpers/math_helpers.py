import sympy as sp


def get_divisors(n: int):
    divisors = []
    for i in range(1, abs(n) + 1):
        # If i divides n evenly, it's a divisor
        if n % i == 0:
            divisors.append(i)
            divisors.append(-i)

    return divisors


def ruffinis_rule(poly: list[dict], divisor: float) -> tuple[list[dict], float]:
    quotient = []
    remainder = 0

    # Iterate through the terms
    for term in poly:
        quotient_coef = term["coef"] + remainder
        quotient.append({"grade": term["grade"] - 1, "coef": quotient_coef})
        remainder = quotient_coef * divisor

    # Remove leading zeros from the quotient
    while len(quotient) > 0 and (
        quotient[-1]["coef"] == 0 or quotient[-1]["grade"] < 0
    ):
        quotient.pop()

    return list(quotient), remainder


def resolve_low_grade(poly: list[dict], polyGrade: int) -> tuple[float]:
    if polyGrade == 0:
        return []

    if polyGrade == 1:
        return [resolve_linear(poly)]

    if polyGrade == 2:
        return baskara(poly)


def gauss_teorem(ind: int, main: int) -> list[float]:
    ind_divisors = get_divisors(ind)
    main_divisors = get_divisors(main)

    potentialRoots: float = []
    for indDivisor in ind_divisors:
        for mainDivisor in main_divisors:
            potentialRoot = sp.Rational(indDivisor, mainDivisor)
            potentialRoots.append(potentialRoot)

    return potentialRoots


def rationalize_float(number: float) -> str:
    return sp.nsimplify(number)


def resolve_linear(poly: list[dict]) -> float:
    a = poly[0]["coef"]
    b = poly[1]["coef"]

    return rationalize_float(-b / a)


def rationalize_float_list(float_list: list[float]) -> list[str]:
    rationals = []
    for i in range(len(float_list)):
        fraction = rationalize_float(float_list[i])
        rationals.append(fraction)
    return rationals


def baskara(poly: list[dict]):
    a = poly[0]["coef"]
    b = poly[1]["coef"]
    c = poly[2]["coef"]

    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        x1 = rationalize_float((-b + sp.sqrt(discriminant)) / (2 * a))
        x2 = rationalize_float((-b - sp.sqrt(discriminant)) / (2 * a))
    else:
        real_part = rationalize_float(-b / (2 * a))
        imag_part = rationalize_float(sp.sqrt(-discriminant) / (2 * a))
        x1 = f"{sp.simplify(real_part)}+{sp.simplify(imag_part)}i"
        x2 = f"{sp.simplify(real_part)}-{sp.simplify(imag_part)}i"

    return [x1, x2]


def evaluate(terms: list[dict], x: float) -> float:
    result = 0
    for term in terms:
        coefficient = term["coef"]
        grade = term["grade"]

        result += coefficient * (x**grade)
    return result
