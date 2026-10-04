print("Parity - last bit = 0 even, last bit = 1 odd. Press Enter ")
for i in [2, 3, 4, 5, 8, 9]:
    if i & 1:
        print("  ", i, "-> odd")
    else:
        print("  ", i, "-> even")

print("Count the 1s - watch")
temp = 5
while temp > 0:
    print("  binary:", bin(temp)[2:], "  last bit:", temp & 1)
    temp >>= 1
    print("  total is in", 5, "=", bin(5).count("1"))