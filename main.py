from bitarray import bitarray

d = 4


def setDimension(dimension):
    d = dimension


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


print(L(b'\x66'))


def pi(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    if len(byteInput) * 8 != 2 ** d:
        raise Exception("input dimension must be " + str(d))
    input = byteToTab(byteInput)
    res = []
    for i in range(0, int(len(input) / 4)):
        res.append(input[4 * i])
        res.append(input[4 * i + 1])
        res.append(input[4 * i + 3])
        res.append(input[4 * i + 2])
    return bitarray(res).tobytes()


print(pi(b'\xab\x12'))


def permPrim(byteInput):
    if type(byteInput) != bytes:
        raise TypeError
    if len(byteInput) * 8 != 2 ** d:
        raise Exception("input dimension must be " + str(d))
    input = byteToTab(byteInput)
    res = [0]*len(input)

    for i in range(int(len(input)/2)):
        res[i]=input[2*i]
        res[i+2**(d-1)]=input[2 * i + 1]
    return bitarray(res).tobytes()

print(byteToTab(b'\xab\x12'))
print(byteToTab(permPrim(b'\xab\x12')))

