# Polynomial roots calculator

A simple polynomial roots calculator script written in python.

It uses the Gaus Theorem behind the scenes to find the potential roots of the polynomial. Then it evaluates each potential root in the polynomial to get the result.

## Requirements

- python >=3.6 [download here](https://www.python.org/downloads/)
- pyenv [install it now](https://pypi.org/project/pipenv/#installation)

## Instalation

```bash
$ pipenv install
```

## Limitations

- Meant to be used for real coefficients polynomials (complex polynomials are not supported by design)
- It uses the [Gauss Lemma](https://www.reddit.com/r/learnmath/comments/fursna/comment/fmefqtc/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) for finding the polynomials roots, so you need to input integer coefficients. If your polynomial has rational / irrationals coefficients try multiplying the whole polynomial by an number that gets rid of the denominators. The resulting polynomial will share roots with the original one. Example:

```
P(x) = (3/2)(x^4) + (5/2)(x^3) - 2(x^2) + (3/2)x + (9/2)
2xP(x) = 3(x^4) + 5(x^3) - 2(x^2) + 3x + 9   <-- Shares roots with P(x)

```

## Features

- Rational display of floats
- Square root display of irrational floats (`sqrt(2)` = √2)
- Support for any degree polynomial
- Support for nth (double, triple, etc) roots (will be displayed n number of times)
- Support for complex roots (conjugate ones)

## Usage

To perform a run, prompt:

```bash
$ python3 roots.calculator.py
```
