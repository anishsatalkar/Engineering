key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

P8 = [6, 3, 7, 4, 8, 5, 10, 9]

EP8 = [4, 1, 2, 3, 2, 3, 4, 1]


def shift_left_round(bin_list, k):
    shifted_num = []
    for idx, val in enumerate(bin_list):
        shifted_num.append(bin_list[(idx + k) % len(bin_list)])

    return shifted_num


def permute(p_box, in_key):
    len_pbox = len(p_box)
    permuted = []
    for i in range(0, len_pbox):
        permuted.append(in_key[p_box[i] - 1])
    return permuted

def expand_and_permute(ep_box, in_key):
    len_ep_box = len(ep_box)
    expanded = []
    for i in range(0, len_ep_box):
        expanded.append(in_key[ep_box[i] - 1])

    return expanded

def encrypt(plain_t, key1, key2):
    P8_box = [2, 6, 3, 1, 4, 8, 5, 7]
    plain_t = permute(P8_box, plain_t)

    print('permuted encrypt : ', plain_t)

    hf1 = plain_t[:len(plain_t) // 2]
    hf2 = plain_t[len(plain_t) // 2:]

    print('hf1 : {}, hf2 : {}'.format(hf1, hf2))

    hf2 = expand_and_permute(EP8 , [1,0,0,0])
    print('expanded hf1 = ' , hf2)


# Initial permutation using P10 box
key_permuted = permute(P10, key)

# Splitting the permuted key into two halves
h1 = key_permuted[:len(key_permuted) // 2]
h2 = key_permuted[len(key_permuted) // 2:]

# Shifting (in a circular manner) the halves 1 bit to the left
h1 = shift_left_round(h1, 1)
h2 = shift_left_round(h2, 1)

# Combining the shifted halves into a single key
key_shifted_1 = h1 + h2

# Applying permutation on this combined key using P8 box to get the first key
key_1 = permute(P8, key_shifted_1)

# ------Generating the second key:------

# Left shift the 2 halves from one of the above steps
h1 = shift_left_round(h1, 2)
h2 = shift_left_round(h2, 2)

# Combine the 2 halves
key_shifted_2 = h1 + h2

# Applying permutation on this combined key using P8 box to get the second key
key_2 = permute(P8, key_shifted_2)

# ------Encryption starts------
plain_text = [0, 1, 1, 1, 0, 0, 1, 0]

cipher_text = encrypt(plain_text, key_1, key_2)
