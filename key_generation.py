import numpy as np
import random

# acccepting user credentials
string1 = raw_input("enter roll number \n")
roll = list(string1)
matrix1 = [roll[i:i + 4] for i in xrange(0, len(string1), 4)]
string2 = raw_input("enter aadhar number\n")
aadhar = list(string2)
matrix2 = [aadhar[i:i + 3] for i in xrange(0, len(string2), 3)]
# printing user credentials
roll_matrix = [[0 for i in range(4)] for j in range(3)]
for i in range(3):
    for j in range(4):
        roll_matrix[i][j] = int(matrix1[i][j]);
# print("Roll Number Matrix")
# for p in roll_matrix:
#    print(p)
aadhar_matrix = [[0 for i in range(3)] for j in range(4)]
for i in range(4):
    for j in range(3):
        aadhar_matrix[i][j] = int(matrix2[i][j]);
# print("Aadhar Number Matrix")
# for q in aadhar_matrix:
#    print(q)
# printing result matrix
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(roll_matrix)):
    for j in range(len(aadhar_matrix[0])):
        for k in range(len(aadhar_matrix)):
            result[i][j] += roll_matrix[i][k] * aadhar_matrix[k][j]
# print("Result Matrix (roll*aadhar)")
# print(result)
# generating matrix of random numbers
ran = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        ran[i][j] = random.randint(0, 25)
# print("Matrix Generated by random numbers")
# print(ran)
# generating key matrix by multiplying random and result matrices
key_matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
for i in range(len(result)):
    for j in range(len(ran[0])):
        for k in range(len(ran)):
            key_matrix[i][j] += result[i][k] * ran[k][j]
key_matrix_modified = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        key_matrix_modified[i][j] = key_matrix[i][j] % 25
print ("Your KEY is")
print (key_matrix_modified)
a = np.array(key_matrix)
# accepting a 9 letter code to encrypt
text = raw_input("Enter a 9 letter text to be Encrypted \n ")
pt = []
for x in text:
    pt.append(int(ord(x)))
# print(pt)
# code for encryption
temp = []
for i in range(3):
    for j in range(3):
        temp.append(int(key_matrix_modified[i][j]))
# print(temp)
pri_ct = np.add(temp, pt)
pri_ct = list(pri_ct)
# print(pri_ct)
act_ct = []
for each in pri_ct:
    if each > 126:
        act_ct.append(np.mod(each, 94))
    else:
        act_ct.append(each)
# print(act_ct)
cipher_text = []
for each in act_ct:
    cipher_text.append(chr(each))
# printing the encrypted data as cipher text
print("CIPHER TEXT for the data is")
print(cipher_text)
# decryption
ch = raw_input("do you want to decrypt the text? (y/n) : ")
pri_pt = []
# decryption process
if ch == 'y':
    for each in cipher_text:
        pri_pt.append(ord(each))
        # print(pri_pt)
    quotient = []
    for each in pri_pt:
        if each < 65:
            multi = (np.divide(each + 94, 94))
            quotient.append((multi * 94) + each)
        else:
            quotient.append(each)

    # print(quotient)
    act_pt = (np.subtract(quotient, temp))
    # print(act_pt)
    plain_text = []
    for each in act_pt:
        plain_text.append(chr(each))
    print("The Decrypted data is ")
    print(plain_text)
else:
    print("you choosed not to encrypt the data Thanks! ")
# the end !!
