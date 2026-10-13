


import sys
print(f"Python {sys.version}")

a = 1000
b = int("1000")
print(f"a == b: {a == b}")   # True
print(f"a is b: {a is b}")   # False

name = "world"
s1 = f"hello {name}!"
s2 = f"hello {name}!"
print(f"s1 == s2: {s1 == s2}")  # True
print(f"s1 is s2: {s1 is s2}")  # False

x = None
print(f"x is None: {x is None}")  # True


x = 10
y = x
x = x + 5
print(f"x = {x}, y = {y}") 
print(f"id(x) = {id(x)}, id(y) = {id(y)}") 
s = "abc"
s2 = s
s = s + "def"
print(f"s = {s}, s2 = {s2}")  
print(f"id(s) = {id(s)}, id(s2) = {id(s2)}") 



s = "Hello World"
s_stripped = s.strip()
s_lower = s.lower()
s_replaced = s.replace("World", "Python")

print(f"Исходная: '{s}'")
print(f"strip: '{s_stripped}'")
print(f"lower: '{s_lower}'")
print(f"replace: '{s_replaced}'")
print(f"s не изменилась: {s == 'Hello World'}")


import sys

numbers = [0, 1, 255, 256, 1000, 10**10, 10**100]
for n in numbers:
    print(f"{n!r:>15} - {sys.getsizeof(n)} байт")

strings = ["", "a", "ab", "abc", "a"*100]
for s in strings:
    print(f"len={len(s):>3} - {sys.getsizeof(s)} байт")




import timeit

setup_code = """
a, b, c, d, e, f, g, h, i, j = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
"""

code_concat = "a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f + ' ' + g + ' ' + h + ' ' + i + ' ' + j"

code_format = "'{} {} {} {} {} {} {} {} {} {}'.format(a, b, c, d, e, f, g, h, i, j)"

code_fstring = "f'{a} {b} {c} {d} {e} {f} {g} {h} {i} {j}'"

t_concat = timeit.timeit(code_concat, setup=setup_code, number=1000000)
t_format = timeit.timeit(code_format, setup=setup_code, number=1000000)
t_fstring = timeit.timeit(code_fstring, setup=setup_code, number=1000000)

print(f"Конкатенация: {t_concat:.4f} с")
print(f"format():     {t_format:.4f} с")
print(f"f-строка:     {t_fstring:.4f} с")
