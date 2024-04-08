import sympy as sp


def get_divisors(n: int):
    divisors = []
    for i in range(1, abs(n) + 1):
        # If i divides n evenly, it's a divisor
        if n % i == 0:
            divisors.append(i)
            divisors.append(-i)

    return divisors


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


def rationalize_float_list(float_list: list[float]) -> list[str]:
    rationals = []
    for i in range(len(float_list)):
        fraction = rationalize_float(float_list[i])
        rationals.append(fraction)
    return rationals


def baskara(poly: list[dict]):
    a = poly[2]["coef"]
    b = poly[1]["coef"]
    c = poly[0]["coef"]

    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        x1 = rationalize_float((-b + sp.sqrt(discriminant)) / (2 * a))
        x2 = rationalize_float((-b - sp.sqrt(discriminant)) / (2 * a))
    else:
        real_part = rationalize_float(-b / (2 * a))
        imag_part = rationalize_float(sp.sqrt(-discriminant) / (2 * a))
        x1 = f"{sp.simplify(real_part)}+{sp.simplify(imag_part)}i"
        x2 = f"{sp.simplify(real_part)}-{sp.simplify(imag_part)}i"

    return x1, x2


def evaluate(terms: list[dict], x: float) -> float:
    result = 0
    for term in terms:
        coefficient = term["coef"]
        grade = term["grade"]

        result += coefficient * (x**grade)
    return result
