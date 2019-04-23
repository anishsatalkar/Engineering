def phi(a, b):
    return (a - 1) * (b - 1)


def gcd(a, b):
    if b == 0:
        return a
    return int(gcd(b, a % b))


def is_int(num):
    if num - int(num) == 0:
        return True
    else:
        return False


def calculate_d_value(phi_n, e, i):
    return ((phi_n * i) + 1) / e


def encrypt(plain_t, n):
    return (plain_t ** public_key['e']) % n


def decrypt(cipher_t, n):
    return (cipher_t ** private_key['d']) % n


a = 11
b = 13

n = a * b

phi_n = phi(a, b)

e = 2
while gcd(e, phi_n) != 1 and e < phi_n:
    e += 1

print('e: ', e)
i = 1

d = calculate_d_value(phi_n, e, i)
while not is_int(d):
    i += 1
    d = calculate_d_value(phi_n, e, i)

public_key = {
    'e': int(e),
    'n': n
}

private_key = {
    'd': int(d),
    'n': n
}

plain_text = 13
print('Plaintext : ',plain_text)
cipher_text = encrypt(plain_text, n)
print('After encryption, cipertext : ', cipher_text)

print('After decryption, plaintext : ', decrypt(cipher_text, n))
