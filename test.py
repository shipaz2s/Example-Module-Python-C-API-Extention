import custom

class Derived(custom.Custom): pass

n = Derived()

# n.some_attribute = n
# n.number = 1
# n.n = -1

# n.first = str(1)
# n.second = "2dasd"

n.first = "john"
n.last = "mate"

print(n)
print(n.name())
print(n.number)
print(n.first)
print(n.last)

print(f'n = {n}')
n2 = Derived()
print(f'n2 = {n2}')
n3 = n
print(f'n3 = {n3}')