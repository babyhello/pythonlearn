class Car:
    vendor = "lexus"
    valid = True


c1 = Car()
c2 = Car()
c3 = Car()
print(Car.vendor, c1.vendor, c2.vendor, c3.vendor)
print(Car.valid, c1.valid, c2.valid, c3.valid)
Car.valid = False
print(Car.valid, c1.valid, c2.valid, c3.valid)
Car.quality = "Best"
print(Car.quality, c1.quality, c2.quality, c3.quality)
c1.color = 'red'
c2.driver = "Mark"
c3.passenger = 6
print(c1.color, c1.vendor, c1.valid, c1.quality)
print(Car.valid, c1.valid, c2.valid, c3.valid)
c1.valid = True
print(Car.valid, c1.valid, c2.valid, c3.valid)