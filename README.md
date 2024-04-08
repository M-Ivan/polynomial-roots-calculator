# root-calculator

A simple polynomial roots calculator script written in python.

## Requirements

- python >=3.6 [download here](https://www.python.org/downloads/)
- pyenv [install it now](https://pypi.org/project/pipenv/#installation)

## Instalation

```bash
$ pipenv install
```

## Features

- Rational display of periodic floats
- Square root display of irrational floats (`sqrt(2)` = √2)
- Support for any grade polynomial

## Usage

To perform a run, prompt:

```bash
$ python3 roots.calculator.py
```

## Known issues

- Pending support complex roots for polynomials of greater grade than 2.
- Pending support for complex coefficient polynomial
- Pending support for irrational / rational coefficients (you can multiply your poly coefs by an scalar in the meantime to get rid of denominators)
