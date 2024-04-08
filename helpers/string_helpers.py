def build_polynomial(terms: list[dict]):
    polynomial = []

    for term in sorted(terms, key=lambda x: x["grade"], reverse=True):
        coefficient = term["coef"]
        grade = term["grade"]
        if coefficient != 0:
            if grade == 0:
                polynomial.append(str(coefficient))
            elif grade == 1:
                polynomial.append(f"{coefficient}x")
            else:
                polynomial.append(f"{coefficient}(x^{grade})")
    return " + ".join(polynomial)
