import math

r = 5
a = r * r * math.pi

s1 = "radius=%f,area=%f\n"
s2 = "radius=%.1f, area=%.2f\n"
s3 = "radius=%(radius).1f, area=%(area).2f\n"
s4 = "radius={}, area={}\n"
s5 = "radius={:.1f}, area={:.2f}\n"
s6 = "radius={0:.1f}, area={1:.2f}\n"
print(s1 % (r, a))
print(s2 % (r, a))
print(s3 % {'radius': r, 'area': a})
print(s3 % {'area': a, 'radius': r})
print(s4.format(r, a))
print(s5.format(r, a))
print(s6.format(r, a))
print(f"radius={r:.1f}, area={a:.2f}\n")