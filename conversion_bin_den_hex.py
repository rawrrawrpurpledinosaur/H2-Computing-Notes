def denary_to_binary(n: int) -> str: # This notation means that function accepts int and returns str
    if n == 0:
        return "0"

    binary = ""
    while n>0: 
        binary = str(n % 2) + binary # adds the result of n modulo 2 to the left of result
        n = n // 2 # floor division
    return binary

def binary_to_denary(n: str) -> int:
    # Reverse the string to perform conversion more easily
    n = n[::-1]
    den = 0
    for i in range(0, len(n)-1): 
        # 2^i to convert the i_th digit and add to result
        den = den + int(n[i]) * 2**i
    return den


def denary_to_hex(n):
    if n == 0:
        return "0"
    hex = ""
    while n>0:
        rem = n % 16 # find remainder  
        if rem < 10:
            hex = str(rem) + hex 
        else:
            # Convert to ASCII character (A-F)
            hex = chr(rem + 55) + hex
        n//=16
    return hex

def hex_to_denary(n: str) -> int:
    den = 0
    # reverse the string to make conversion easier
    n = n[::-1]
    for i in range(0, len(n)-1):
        # Convert to ASCII character (A-F)
        if n[i].isalpha():
            den = den + (ord(n[i])-55) * 16**i
        else:
            den = den + int(n[i]) * 16**i
    return den

