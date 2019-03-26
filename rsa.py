def phi(a_num, b_num):
    return (a_num - 1) * (b_num - 1)


def gcd(a_num, b_num):
    if b_num == 0:
        return a_num
    return int(gcd(b_num, a_num % b_num))


def is_int(num):
    if num - int(num) == 0:
        return True
    else:
        return False


def calculate_d_values(p, e_num, iter):
    return ((p * iter) + 1) / e_num


def encrypt(plain_t, n_num):
    return (plain_t ** public_key['e']) % n_num


def decrypt(cipher_t, n_num):
    return (cipher_t ** private_key['d']) % n_num


a = 13
b = 11

n = a * b

phi_n = phi(a, b)

e = 2
while gcd(e, phi_n) != 1 and e < phi_n:
    e += 1

i = 1

d = calculate_d_values(phi_n, e, i)
while not is_int(d):
    i += 1
    d = calculate_d_values(phi_n, e, i)

public_key = {
    'e': int(e),
    'n': n
}

private_key = {
    'd': int(d),
    'n': n
}

plain_text = 13

cipher_text = encrypt(plain_text, n)
print(cipher_text)

print(decrypt(cipher_text, n))
