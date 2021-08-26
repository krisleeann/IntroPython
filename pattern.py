# Not overly elegant, but it works
for i in range(1):
    if (32 % 2 == 0):
        print(16 * "/" + 16 * "\\")
    if (32 % 3 == 2):
        print(12 * '/' + 8 * '*' + 12 * '\\')
    if (32 / 4 == 8):
        print(4 * '/' + 24 * '*' + 4 * '\\')
    if (32 % 1 == 0):
        print(32 * '*')