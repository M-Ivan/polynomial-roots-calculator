def build_polynomial(terms: list[dict]):
    polynomial = []

    determine_sign = lambda coef: f"{coef if coef < 0 else f'+{coef}'}"

    for term in terms:
        coefficient = term["coef"]
        degree = term["degree"]
        if coefficient != 0:
            if degree == 0:
                polynomial.append(determine_sign(coefficient))
            elif degree == 1:
                polynomial.append(f"{determine_sign(coefficient)}x")
            else:
                polynomial.append(f"{determine_sign(coefficient)}(x^{degree})")
    return " ".join(polynomial)
