from bitarray import bitarray
from random import randbytes

d = 6


def setDimension(dimension):
    if dimension<3:
        raise TypeError("Minimum dimension 3")
    global d
    d = dimension
    print("Dimension set to", d)
    return d


def bitLen(int_type):
    if type(int_type) != int:
        raise TypeError
    length = 0
    while int_type:
        int_type >>= 1
        length += 1
    return length


def intToList(int_type, expected_length):
    if type(int_type) != int:
        raise TypeError
    res = []
    for i in range(expected_length):
        res.append(int_type >> (expected_length - i - 1) & 1)
    return res


def byteToTab(byteInput):
    res = []
    for i in byteInput:
        res.extend(intToList(i, 8))
    return res


def tabToByte(tab_type):
    if type(tab_type) != list:
        raise TypeError

    return bitarray(tab_type).tobytes()


def L(byteInput):
    # Linear Transformation L
    if type(byteInput) != bytes:
        raise TypeError
    A = intToList(byteInput[0] >> 4 & 0x0F, 4)
    B = intToList(byteInput[0] & 0x0F, 4)

    D = [B[0] ^ A[1], B[1] ^ A[2], B[2] ^ A[3] ^ A[0], B[3] ^ A[0]]
    C = [A[0] ^ D[1], A[1] ^ D[2], A[2] ^ D[3] ^ D[0], A[3] ^ D[0]]

    return bitarray(C + D).tobytes()


# print(L(b'\x66'))


def pi(byteInput):
    if type(byteInput) != bytes:
        raise TypeError

    input = byteToTab(byteInput)
    res = []
    for i in range(0, int(len(input) / 4)):
        res.append(input[4 * i])
        res.append(input[4 * i + 1])
        res.append(input[4 * i + 3])
        res.append(input[4 * i + 2])
    return bitarray(res).tobytes()


def permPrim(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    input = byteToTab(byteInput)
    res = [0] * len(input)

    for i in range(int(len(input) / 2)):
        res[i] = input[2 * i]
        res[i + 2 ** (d -1)] = input[2 * i + 1]
    return bitarray(res).tobytes()


def fi(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    input = byteToTab(byteInput)
    halfLength = int(len(input) / 2)
    res = [0] * len(input)

    for i in range(0, halfLength, 2):
        res[i] = input[i]
        res[i + 1] = input[i + 1]
        res[i + halfLength] = input[i + 1 + halfLength]
        res[i + 1 + halfLength] = input[i + halfLength]
    return bitarray(res).tobytes()


def permutation(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    return fi(permPrim(pi(byteInput)))


def S(index, bits):
    if (type(index) != int and (index == 0 or index == 1)) or (type(bits) != int and -1 < bits < 16):
        raise TypeError
    return \
        [[9, 0, 4, 11, 13, 12, 3, 15, 1, 10, 2, 6, 7, 5, 8, 14],
         [3, 12, 6, 13, 5, 7, 1, 9, 15, 2, 0, 4, 11, 10, 14, 8]][index][bits]

def round(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    if len(byteInput) != 2 ** (d-3):
        raise Exception("input dimension must be " + str(d))
    input = byteToTab(byteInput)
    temp =[]
    for i in range(0,2**d,8):
        temp.append((S(0,input[i]*8+input[i+1]*4+input[i+2]*2+input[i+3])*16+S(1, input[i+4] * 8 + input[i + 5] * 4 + input[i + 6] * 2 + input[i + 7])).to_bytes(1,"big"))
    res = bytes()
    for i in temp:
        res+=L(i)
    return permutation(res)







setDimension(3)
#print(d)
x = b'\x66'#randbytes(2 ** (d - 3))
#print(x)
#print(x.hex())
print(permutation(b'\xd7').hex())
print(round(x).hex())
print(L(b'\31'))