import math
print("--------------Part a--------------")
print("i: ", (37*3) % 23)
print("ii: ",  (19*13) % 23)
print("iii: ", (18*15) % 12)
print("iv: ", (15*29 + 11*15)%23)

print("Part b and c were done on paper, see the pdf submission")

print("\n\n--------------Part d--------------")
no_inverse = [0]
for i in range(1,216):
    if math.gcd(i,216) != 1: no_inverse.append(i)
no_inverse.remove(0)
print("Numbers with no multiplicative inverse for modulo 216: ")
print(no_inverse[0:24])
print(no_inverse[25:49])
print(no_inverse[50:74])
print(no_inverse[75:99])
print(no_inverse[100:124])
print(no_inverse[125:142])
print("Total amount of numbers with no inverse modulo 216:", len(no_inverse))