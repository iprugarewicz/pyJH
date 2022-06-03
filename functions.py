d = 4


def setD(dimension):
    d = dimension


def bitLen(int_type):
    length = 0
    while int_type:
        int_type >>= 1
        length += 1
    return length


def getBit(binary, bit_id):
    return (binary >> bit_id) % 2;


def L(A, B):
    D = getBit(B, 0) ^ getBit(A, 1)  # D_0
    D += 2 * (getBit(B, 1) ^ getBit(A, 2))  # D_1
    D += 4 * (getBit(B, 2) ^ getBit(A, 3) ^ getBit(A, 0))  # D_2
    D += 8 * (getBit(B, 3) ^ getBit(A, 0))  # D_3

    C = getBit(A, 0) ^ getBit(D, 1)  # C_0
    C += 2 * (getBit(A, 1) ^ getBit(D, 2))  # C_1
    C += 4 * (getBit(A, 2) ^ getBit(D, 3) ^ getBit(D, 0))  # C_2
    C += 8 * (getBit(A, 3) ^ getBit(D, 0))  # C_3

    return [C, D]
def pi(A):
    B = 0
    print(bin(A),bitLen(A))
    for i in range(int((bitLen(A)+1)/4)):
        B += (2 ** (i+0)) * getBit(A, (4 * i))
        print(i*4,getBit(A,4*i))
        B += (2 ** (i+1)) * getBit(A, (4 * i)+1)
        print(getBit(A, (4 * i)+1))
        B += (2 ** (i+2)) * getBit(A, (4 * i)+3)
        print(getBit(A, (4 * i)+2))
        B += (2 ** (i+3)) * getBit(A, (4 * i)+2)
        print(getBit(A, (4 * i)+3))
        representation = bin(B)
    return B
