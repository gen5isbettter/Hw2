aes_input = ['0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1',
             '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '1', '1', '1', '1',
             '0', '1', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0',
             '1', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '1',
             '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1',
             '1', '1', '1']

binary_input = ''.join(aes_input)
hex_input = hex(int(binary_input, 2))
print("--------------Part a--------------")
#hex
print(hex_input)
print("--------------Part b--------------")
#write input in a state diagram
state_diagram = [['0','0','0','0'],['0','0','0','0'],
                 ['0','0','0','0'],['0','0','0','0']]

for i in range(4):
    for j in range(4):
        #fill out the 4x4 byte array that will be the input state diagram
        state_diagram[i][j] = ''.join(aes_input[(32*i + 7*j):(32*i + 7 + 7*j)])
        state_diagram[i][j] = hex(int(state_diagram[i][j], 2))

print("state diagram:")
for i in range(0,4):
    print(state_diagram[i])

print("--------------Part c--------------")

#print(sub_box)
sub_box = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
           ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
           ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
           ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
           ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
           ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
           ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
           ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
           ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
           ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
           ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
           ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
           ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
           ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
           ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
           ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

sbox_state = [['0','0','0','0'],['0','0','0','0'],
                 ['0','0','0','0'],['0','0','0','0']]

for i in range(4):
    for j in range(4):
        temp = state_diagram[i][j]
        temp = temp[2:]
        x = int(temp[0],16)
        y = int(temp[1],16)
        sbox_state[i][j] = '0x' + sub_box[x][y]
print('SubBytes applied:')
for i in range(0,4):
    print(sbox_state[i])

print('--------------Part d--------------')
shift_rows = sbox_state

for i in range(0,4):
    pop_count = i
    while pop_count != 0:
        shift_rows[i].insert(0, sbox_state[i].pop())
        pop_count += -1
print('shift rows')
for i in range(4):
    print(shift_rows[i])

print('--------------Part e--------------')
print('mix columns')
mix_columns = [['0','0','0','0'],['0','0','0','0'],
                 ['0','0','0','0'],['0','0','0','0']]

#𝑃(𝑥) = 𝑥8 + 𝑥4 + 𝑥3 + 𝑥 + 1
p_x = [1,0,0,0,1,1,0,1,1]

#create method for multiplying the columns and a matrix
#3 cases:
#multiply by one, no change
#multiply by two: bit shift rightmost bit over by one
#multiply by three: bit shift by one, and xor with original x
def multiply(x,a):
    one_b = ['0','0','0','1','1','0','1','1']
    d = ['0']*8
    if a == '01':
        x = x[2:]
        x = str(bin(int(x, 16)))[2:].zfill(8)
        return x
    else:
        x = x[2:]
        x = str(bin(int(x, 16)))[2:].zfill(8)
        x = list(x)
        x_initial = list(x)
        last_one = 0
        high_bit = 0
        for i in range(len(x)):
            if x[i] == '1':
                last_one = i
                if i != 0:
                    high_bit = i-1
        x[last_one] = '0'

        if x[high_bit] == '0':
            x[high_bit] = '1'
        else:
             #xor with 0x1B
            for j in range(8):
                d[j] = (int(one_b[j])^int(x[j]))
            x = d

        if a == '03':
            for k in range(8):
                d[k] = int(x_initial[k])^int(x[k])
            x = d
    return x

#Each index is a polynomial of degree 7 or lower
a_x = [['02','03','01','01'],['01','02','03','01'],['01','01','02','03'],['03','01','01','02']]
for i in range(4):
    for j in range(4):
        x = 4

def xor(list1, list2):
    list3 = [0]*len(list1)
    for i in range(len(list1)):
        list3[i] = int(list1[i])^int(list2[i])
    return list3
def bin_to_hex(list):
    conversion = ''.join(map(str,list))
    conversion = hex(int(conversion, 2))
    return conversion

def hex_to_bin(str1):
    result = str(bin(int(str1, 16)))[2:].zfill(8)
    return list(result)
#perform gf multiplication between mix_columns column and a_x[i]
#xor the multiplication with each result
for z in range(4):
    for column in range(4):
        temp_list = []
        for row in range(4):
            temp_list.append(multiply(shift_rows[row][z],a_x[column][row]))

        #we have our 4 values, now we xor
        result = temp_list[0]
        for i in range(1, len(temp_list)):
            result = xor(result, temp_list[i])
        # after xor, add to the mix_columns state matrix
        mix_columns[z][column] = bin_to_hex(result)
for i in range(4):
    print(mix_columns[i])

print('--------------Part f--------------')
print('Apply Round Key')
key = ['0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0',
       '0', '1', '1', '1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1',
       '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1', '1', '0', '1',
       '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '0', '1', '0']
pre_key = []
for c in range(4):
    for d in range(4):
        skibidi = hex_to_bin(mix_columns[c][d])
        for toy in skibidi:
            pre_key.append(toy)
ciphertext = xor(pre_key,key)
print(bin_to_hex(ciphertext))