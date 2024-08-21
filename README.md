# InterCalc

## Introduction

Scientific calculations often involve uncertainty intervals. Such calculations difficult and tedious to perform correctly with a conventional calculator. This module is like a calculator created specifically to deal with uncertainty intervals.

For example, if you have a battery with a voltage of 12 ± 1 V (that is, \[11, 13\] V) and a circuit with a resistance of 3 ± 1 Ω (that is, \[2, 4\] Ω), then the current is \[11/4, 13/2\] Ω. This module is meant for performing such calculations. You would perform the calculation as follows:
```
>>> from intercalc import *
>>> i = interval # Typing interval every time you want to construct a new interval is rather tedious.
>>> v = i(11, 13)
>>> r = i(2, 4)
>>> c = v / r
>>> print(c)
[2.75, 6.5]
```
I have used dunder methods to enable the use of familiar operations.

## One significant limitation

If you perform a calculation where the same variable appears in multiple places, it will be treated as if each occurrence were a different variable. For example:
```
>>> a = i(1, 2)
>>> print(a - a)
[-1.0, 1.0]
```
Obviously `a - a` should yield exactly 0, but implementing such behaviour would require significantly more work, and in my experience, most formulae one comes across do not feature repeated variables.

## How to use

### Constructing intervals

Interval objects are constructed with `i()`. For example, `i(5, 6)` to construct the interval \[5, 6\].

### Arithmetic and powers

Use `+`, `-`, `*`, and `/` operators as you would with floats.

### Powers and logarithms

Use the `**` operator for powers. Note that the exponent should be a number, not an interval.

Use `intercalc.log(a, b)` to obtain the base `b` logarithm of `a`, where `a` is an intrval and `b` is a number.

I have chosen to restrict exponents and bases to numbers because in practice, these are usually constants, not variables.

### Trigonometry

The sine, cosine, and tangent of `a` can all be found with `intercalc.sin(a)`, `intercalc.cos(a)`, and `intercalc.tan(a)` respectively.

### Miscellaneous

Unary operators `+` and `-` have been implemented.

`abs(a)` is the absolute value of `a`.

The constructor automatically puts the arguments in order so you don't have to worry about putting them in order every time you construct an interval, so `interval(4, 3)` is the same as `interval(3, 4)`.
