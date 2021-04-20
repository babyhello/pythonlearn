from decimal import Decimal as Dec

x1 = Dec(2.968)
print(x1)
x2 = Dec(0.5)
print(x2)
x3 = Dec('2.968')
print(x3)

print(Dec(2968)*Dec(0.001)-Dec(2.968))
print(Dec(2968)*Dec('0.001')-Dec(2.968))
print(Dec(2968)*Dec('0.001')-Dec('2.968'))