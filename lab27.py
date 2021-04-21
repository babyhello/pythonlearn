import lab26_demo_module

print(lab26_demo_module.foo(3, 4))
print(lab26_demo_module.bar(5, 6))
import lab26_demo_module as l26

print(l26.foo(7, 8))
print(l26.bar(9, 10))

from lab26_demo_module import foo, bar

print(foo(11, 12))
print(bar(13, 14))
from lab26_demo_module import foo as fo, bar as ba

print(fo(15, 16))
print(ba(17, 18))