from fractions import Fraction

x1 = Fraction(250, 72)
print(type(x1), dir(x1))
print(x1.numerator, x1.denominator)
x2 = Fraction(150, 33)
print(x1 + x2, x1 - x2)