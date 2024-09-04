def denary_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n>0: 
        binary = str(n % 2) + binary
        # same as floor division
        n = n >> 1

def binary_to_denary(n: str) -> int:
    den = 0
    for i in range(len(n)): 
        # 1010
        # 1*2^3 + 0*2^2 + 1*2^1 + 0
        den = den + int(n[i]) * 2**(len(n)-1-i)
    return den


def denary_to_hex(n):
    if n == 0:
        return "0"
    hex = ""
    while n>0:
        rem = n % 16
        if rem < 10:
            hex = str(rem) + hex
        else:
            hex = chr(rem + 55) + hex
        n = n >> 4
    return hex

def hex_to_denary(n: str) -> int:
    den = 0
    for i in range(len(n)):
        if n[i].isdigit():
            den = den + int(n[i]) * 16**(len(n)-1-i)
    return den

