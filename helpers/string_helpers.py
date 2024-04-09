def build_polynomial(terms: list[dict]):
    polynomial = []

    determine_sign = lambda coef: f"{coef if coef < 0 else f'+{coef}'}"

    for term in terms:
        coefficient = term["coef"]
        grade = term["grade"]
        if coefficient != 0:
            if grade == 0:
                polynomial.append(determine_sign(coefficient))
            elif grade == 1:
                polynomial.append(f"{determine_sign(coefficient)}x")
            else:
                polynomial.append(f"{determine_sign(coefficient)}(x^{grade})")
    return " ".join(polynomial)
