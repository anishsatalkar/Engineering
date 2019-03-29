#Encryption done. Decryption under progress

key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

P8 = [6, 3, 7, 4, 8, 5, 10, 9]

EP8 = [4, 1, 2, 3, 2, 3, 4, 1]

S_Box_0 = [['01', '00', '11', '10'],
           ['11', '10', '01', '00'],
           ['00', '10', '01', '11'],
           ['11', '01', '10', '10']]

S_Box_1 = [['00', '01', '10', '11'],
           ['10', '00', '01', '11'],
           ['11', '00', '01', '11'],
           ['10', '01', '00', '11']]

P4 = [2, 4, 3, 1]


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


def xor(b1, b2):
    xor_val = []
    for i in range(len(b1)):
        xor_val.append(b1[i] ^ b2[i])

    return xor_val


def encrypt_round(plain_t, key_in):
    P8_box = [2, 6, 3, 1, 4, 8, 5, 7]
    plain_t = permute(P8_box, plain_t)

    print('permuted encrypt : ', plain_t)

    hf1 = plain_t[:len(plain_t) // 2]
    copy_hf1 = [x for x in hf1]
    hf2 = plain_t[len(plain_t) // 2:]
    copy_hf2 = [x for x in hf2]

    print('hf1 : {}, hf2 : {}'.format(hf1, hf2))

    hf2 = expand_and_permute(EP8, hf2)
    print('expanded hf2 = ', hf2)

    # XOR hf2 with Key_1

    xor_val = xor(hf2, key_in)
    print('xor_val : ', xor_val)

    hf1 = xor_val[:len(xor_val) // 2]
    hf2 = xor_val[len(xor_val) // 2:]

    print('xor stuff : ', hf1, ' ', hf2)

    row_hf1 = str(hf1[0]) + str(hf1[3])
    col_hf1 = str(hf1[1]) + str(hf1[2])
    S0 = (int(row_hf1, 2), int(col_hf1, 2))

    row_hf2 = str(hf2[0]) + str(hf2[3])
    col_hf2 = str(hf2[1]) + str(hf2[2])
    S1 = (int(row_hf2, 2), int(col_hf2, 2))

    print('S0 : {} -- S1 : {}'.format(S0, S1))

    S0S1 = S_Box_0[S0[0]][S0[1]] + S_Box_1[S1[0]][S1[1]]
    S0S1 = [int(x) for x in S0S1]
    print('S0S1 : ',S0S1)

    permute_S0S1 = permute(P4, S0S1)
    print('permuted S0S1 with P4 : ',permute_S0S1)

    xor_permute_S0S1 = xor(permute_S0S1, copy_hf1)
    print('XOR Permute P4 S0S1',xor_permute_S0S1)

    final_out = copy_hf2 + [x for x in xor_permute_S0S1]
    print('combine 2nd half part with prev result : ',final_out)
    return final_out


def decrypt(cipher_text, key_2):
    P8_box = [2, 6, 3, 1, 4, 8, 5, 7]
    plain_t = permute(P8_box, cipher_text)

    print('permuted decrypt  : ', plain_t)

    hf1 = plain_t[:len(plain_t) // 2]
    copy_hf1 = [x for x in hf1]
    hf2 = plain_t[len(plain_t) // 2:]
    copy_hf2 = [x for x in hf2]

    print('hf1 : {}, hf2 : {}'.format(hf1, hf2))

    hf2 = expand_and_permute(EP8, hf2)
    print('expanded hf2 = ', hf2)

    # XOR hf2 with Key_2

    xor_val = xor(hf2, key_2)
    print('xor_val : ', xor_val)

    hf1 = xor_val[:len(xor_val) // 2]
    hf2 = xor_val[len(xor_val) // 2:]

    print('xor stuff : ', hf1, ' ', hf2)

    row_hf1 = str(hf1[0]) + str(hf1[3])
    col_hf1 = str(hf1[1]) + str(hf1[2])
    S0 = (int(row_hf1, 2), int(col_hf1, 2))

    row_hf2 = str(hf2[0]) + str(hf2[3])
    col_hf2 = str(hf2[1]) + str(hf2[2])
    S1 = (int(row_hf2, 2), int(col_hf2, 2))

    print(S0, S1)

    S0S1 = S_Box_0[S0[0]][S0[1]] + S_Box_1[S1[0]][S1[1]]
    S0S1 = [int(x) for x in S0S1]
    print('decrypt S0S1: ', S0S1)

    permute_S0S1 = permute(P4, S0S1)
    #
    xor_permute_S0S1 = xor(permute_S0S1, copy_hf1)
    print('P4 S0S1 XOR : ', xor_permute_S0S1)
    #
    # final_out = copy_hf2 + [x for x in xor_permute_S0S1]
    # print(final_out)
    #
    # return final_out


if __name__ == '__main__':
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
    # print('Key 2 : ', key_2)

    # ------Encryption starts------
    # plain_text = [0, 1, 1, 1, 0, 0, 1, 0]
    plain_text = [0, 1, 1, 0, 1, 1, 0, 1]

    round_1_output = encrypt_round(plain_text, key_in=[1, 0, 1, 0, 0, 1, 0, 0])
    #
    round_2_output = encrypt_round(round_1_output, key_in=[0, 1, 0, 0, 0, 0, 1, 1])
    #
    print('Final cipher_text : ', round_2_output)

    # decrypt([0, 1, 0, 0, 0, 1, 1, 0], key_2)
