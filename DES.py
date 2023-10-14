
def mixer(Left_side, Right_side, Round_key):
    #expand right side
    Expand = [32, 1, 2, 3, 4, 5,
               4, 5, 6, 7, 8, 9,
               8, 9, 10, 11, 12, 13,
               12, 13, 14, 15, 16, 17,
               16, 17, 18, 19, 20, 21,
               20, 21, 22, 23, 24, 25,
               24, 25, 26, 27, 28, 29,
               28, 29, 30, 31, 32, 1]
    #fix indices
    for i in range(0, 48):
        Expand[i] = Expand[i] - 1

    #Expand the right side to xor
    Right_expansion = [0]*48
    for i in range(0,48):
        Right_expansion[i] = Right_side[Expand[i]]

    #xor with round key
    xor_1 = [0] * 48
    for i in range(0,48):
        xor_1[i] = Right_expansion[i] ^ Round_key[i]
    #s_boxes
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    output = [0] * 64
    sbox_output = [0] * 32
    #use the sub boxes to reduce the input size back down to 32
    for i in range(0,8):
        sub = sbox[i]
        compress = Right_expansion[i*6: (i+1)*6]
        row_no = str(compress[0]) + str(compress[5])
        col_no = str(compress[1]) + str(compress[2]) + str(compress[3]) + str(compress[4])
        row_no = int(row_no,2)
        col_no = int(col_no, 2)
        substitution = sub[row_no][col_no]
        substitution = bin(substitution).replace("0b","")
        while len(substitution) < 4:
            substitution = '0' + substitution
        sub_list = [k for k in substitution]
        sub_list = list(map(int, sub_list))
        for j in range (0,4):
            sbox_output[i*4 + j] = sub_list[j]
    #permutation
    P = [16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]
    #Fix permutation indices and permute the sbox output while we're at it
    for i in range(0,32):
        P[i] = P[i] - 1
        sbox_output[i] = sbox_output[P[i]]

    #xor s_box output with the Left side, this is the new right side
    R_prime = [0] * 32
    for i in range(0,32):
        R_prime[i] = sbox_output[i] ^ Left_side[i]

    #Right side becomes the new left
    L_prime = Right_side
    output = L_prime + R_prime

    return(output)

plaintext = [0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,1,
             0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,0]

key = [1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,
       1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1]

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
plaintext_perm = [0] * 64

#change initial perm so that they will reflect the array indices
for i in range(0,64):
    initial_perm[i] = initial_perm[i] - 1

#complete the initial permutation
for i in range(0,64):
    plaintext_perm[i] = plaintext[initial_perm[i]]

#Create keys for the 2 rounds
#First, add in parity bits, this will help us create round keys
parity_key = key
for i in range(1,9):
    parity_key.insert(i*8 -1, 0)
#Create arrays for Permuted choice 1 and 2, change their values to reflect array indices
PC1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
for i in range(0,56):
    PC1[i] = PC1[i] - 1

PC2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]
for i in range(0,48):
    PC2[i] = PC2[i] - 1

#Now that the form of PC1 and PC2 are set up, we can attain our C's, D's and get out 2 keys

Permuted_choice_1 = [0] * 56
for i in range(0,56):
    Permuted_choice_1[i] = parity_key[PC1[i]]

C0 = Permuted_choice_1[0:28]
D0 = Permuted_choice_1[28:56]

#shift the bits to the left to get C1 & D1
C1 = [0] * 28
D1 = [0] * 28
for i in range(0,28):
        if i == 27:
            C1[i] = C0[0]
        else: C1[i] = C0[i+1]

for i in range(0,28):
        if i == 27:
            D1[i] = D0[0]
        else: D1[i] = D0[i+1]

Round_key_1 = [0]*48
C1D1 = C1 + D1

#Create the first round key
for i in range(0,48):
    Round_key_1[i] = C1D1[PC2[i]]

#Create the second round key
C2 = [0] * 28
D2 = [0] * 28
for i in range(0,28):
        if i == 27:
            C2[i] = C1[0]
        else: C2[i] = C1[i+1]

for i in range(0,28):
        if i == 27:
            D2[i] = D1[0]
        else: D2[i] = D1[i+1]

Round_key_2 = [0]*48
C2D2 = C2 + D2
for i in range(0,48):
    Round_key_2[i] = C2D2[PC2[i]]

#Feistel round 1
print("Before feistel round one: ", plaintext_perm)
round1_ciphertext = mixer(plaintext_perm[0:32], plaintext_perm[32:64], Round_key_1)
print("After feistel round one: ", round1_ciphertext)
#Feistel round 2
round2_ciphertext = mixer(round1_ciphertext[0:32], round1_ciphertext[32:64], Round_key_2)
print("After feistel round two: ", round2_ciphertext)
#INVERSE INITIAL PERM

IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]
#fix the array indices
for i in range(0,64):
    IP_inverse[i] = IP_inverse[i] - 1
ciphertext = [0]*64
#Rearrange the ciphertext with the Inverse permutation from the beginning
for i in range(0,64):
    ciphertext[i] = round2_ciphertext[IP_inverse[i]]

print("Final ciphertext: ", ciphertext)