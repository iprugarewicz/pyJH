from bitarray import bitarray
from random import randbytes

d = 6


def setDimension(dimension):
    if dimension < 2:
        raise TypeError("Minimum dimension 2")
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
def bytesToHexTab(byteInput):

    res = []
    for i in byteInput:
        res.extend([i>>4 & 0x0F,i & 0x0F])
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

    inputTab = byteToTab(byteInput)
    res = []
    for i in range(0, int(len(inputTab) / 4)):
        res.append(inputTab[4 * i])
        res.append(inputTab[4 * i + 1])
        res.append(inputTab[4 * i + 3])
        res.append(inputTab[4 * i + 2])
    return bitarray(res).tobytes()


def permPrim(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    inputTab = bytesToHexTab(byteInput)
    res = [0] * 2 ** (d)

    for i in range(2 ** (d-1)):
        res[i] = inputTab[2 * i]
        res[i + 2 ** (d - 1)] = inputTab[2 * i + 1]
    temp = bytes()
    for i in range(0,2**(d),2):
        temp+=((res[i] <<4) + (res[i + 1])).to_bytes(1, "big")
    return temp


def fi(byteInput):
    res =[]
    if type(byteInput) != bytes:
        raise TypeError
    inputTab = bytesToHexTab(byteInput)
    halfLength = 2**(d-1)
    res = bytes()

    for i in range(0, 2**(d-1),2):
        res+=((inputTab[i]<<4) + inputTab[i + 1]).to_bytes(1,"big")

    for i in range(0, 2**(d-1),2):
        res += (inputTab[i+halfLength]  + (inputTab[i + 1+halfLength]<<4)).to_bytes(1, "big")

    return res


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


def round(byteInput,
          constant):  # tu w instrukcji jest wejscie  2^(d-2) -1 , ale mi sie wydaje ze to literówka bo potem jest uzywane normalne 2^d -1
    if type(byteInput) != bytes:
        raise TypeError
    if len(byteInput) != 2 ** (d-1):
        raise Exception("input dimension must be " + str(d))
    if len(constant) != 2 ** (d - 3):
        raise Exception("constant dimension must be " + str(d - 2))

    inputTab = byteToTab(byteInput)
    constant = byteToTab(constant)
    temp = []
    for i in range(0, 2 ** (d)):
        if constant[i] == 0:
            temp.append((S(0, inputTab[i] * 8 + inputTab[i + 1] * 4 + inputTab[i + 2] * 2 + inputTab[i + 3]) * 16 +
                         S(0,
                           inputTab[i + 4] * 8 + inputTab[i + 5] * 4 + inputTab[i + 6] * 2 + inputTab[i + 7])).to_bytes(
                1, "big"))
        elif constant[i] == 1:
            temp.append((S(1, inputTab[i] * 8 + inputTab[i + 1] * 4 + inputTab[i + 2] * 2 + inputTab[i + 3]) * 16 +
                         S(1,
                           inputTab[i + 4] * 8 + inputTab[i + 5] * 4 + inputTab[i + 6] * 2 + inputTab[i + 7])).to_bytes(
                1, "big"))

    res = bytes()
    for i in temp:
        res += L(i)
    return permutation(res)


setDimension(4)
x = b'\x19\xf1\xc1\x8e\x1a\xbc\x81\x08' #randbytes(2 ** (d-1))
c = randbytes(2 ** (d - 3))


print("x =", x.hex())
#print(permPrim(x).hex())
print("c =", c.hex())
print("R =", round(x, c).hex())
#print(fi(x))
#print(permPrim(x))
