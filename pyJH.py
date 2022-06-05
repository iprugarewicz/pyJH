# pyJH by ndywm&szaleniec1231
#
#      █████
#   █████
#        ███
#   █████
#        ███
#   █████
#        ███
#   █████
#        ███
#   █████
#        ███  ██  ██
#   █████  ██  ██ ██
#    ████  ██  ██


from bitarray import bitarray, util
from copy import deepcopy

d=8

C=["6a09e667f3bcc908b2fb1366ea957d3e3adec17512775099da2f590b0667322a","bb896bf05955abcd5281828d66e7d99ac4203494f89bf12817deb43288712231","1836e76b12d79c55118a1139d2417df52a2021225ff6350063d88e5f1f91631c","263085a7000fa9c3317c6ca8ab65f7a7713cf4201060ce886af855a90d6a4eed","1cebafd51a156aeb62a11fb3be2e14f60b7e48de85814270fd62e97614d7b441","e5564cb574f7e09c75e2e244929e9549279ab224a28e445d57185e7d7a09fdc1","5820f0f0d764cff3a5552a5e41a82b9eff6ee0aa615773bb07e8603424c3cf8a","b126fb741733c5bfcef6f43a62e8e5706a26656028aa897ec1ea4616ce8fd510","dbf0de32bca77254bb4f562581a3bc991cf94f225652c27f14eae958ae6aa616","e6113be617f45f3de53cff03919a94c32c927b093ac8f23b47f7189aadb9bc67","80d0d26052ca45d593ab5fb3102506390083afb5ffe107dacfcba7dbe601a12b","43af1c76126714dfa950c368787c81ae3beecf956c85c962086ae16e40ebb0b4","9aee8994d2d74a5cdb7b1ef294eed5c1520724dd8ed58c92d3f0e174b0c32045","0b2aa58ceb3bdb9e1eef66b376e0c565d5d8fe7bacb8da866f859ac521f3d571","7a1523ef3d970a3a9b0b4d610e02749d37b8d57c1885fe4206a7f338e8356866","2c2db8f7876685f2cd9a2e0ddb64c9d5bf13905371fc39e0fa86e1477234a297","9df085eb2544ebf62b50686a71e6e828dfed9dbe0b106c9452ceddff3d138990","e6e5c42cb2d460c9d6e4791a1681bb2e222e54558eb78d5244e217d1bfcf5058","8f1f57e44e126210f00763ff57da208a5093b8ff7947534a4c260a17642f72b2","ae4ef4792ea148608cf116cb2bff66e8fc74811266cd641112cd17801ed38b59","91a744efbf68b192d0549b608bdb3191fc12a0e83543cec5f882250b244f78e4","4b5d27d3368f9c17d4b2a2b216c7e74e7714d2cc03e1e44588cd9936de74357c","0ea17cafb8286131bda9e3757b3610aa3f77a6d0575053fc926eea7e237df289","848af9f57eb1a616e2c342c8cea528b8a95a5d16d9d87be9bb3784d0c351c32b","c0435cc3654fb85dd9335ba91ac3dbde1f85d567d7ad16f9de6e009bca3f95b5","927547fe5e5e45e2fe99f1651ea1cbf097dc3a3d40ddd21cee260543c288ec6b","c117a3770d3a34469d50dfa7db020300d306a365374fa828c8b780ee1b9d7a34","8ff2178ae2dbe5e872fac789a34bc228debf54a882743caad14f3a550fdbe68f","abd06c52ed58ff091205d0f627574c8cbc1fe7cf79210f5a2286f6e23a27efa0","631f4acb8d3ca4253e301849f157571d3211b6c1045347befb7c77df3c6ca7bd","ae88f2342c23344590be2014fab4f179fd4bf7c90db14fa4018fcce689d2127b","93b89385546d71379fe41c39bc602e8b7c8b2f78ee914d1f0af0d437a189a8a4","1d1e036abeef3f44848cd76ef6baa889fcec56cd7967eb909a464bfc23c72435","a8e4ede4c5fe5e88d4fb192e0a0821e935ba145bbfc59c2508282755a5df53a5","8e4e37a3b970f079ae9d22a499a714c875760273f74a9398995d32c05027d810","61cfa42792f93b9fde36eb163e978709fafa7616ec3c7dad0135806c3d91a21b","f037c5d91623288b7d0302c1b941b72676a943b372659dcd7d6ef408a11b40c0","2a306354ca3ea90b0e97eaebcea0a6d7c6522399e885c613de824922c892c490","3ca6cdd788a5bdc5ef2dceeb16bca31e0a0d2c7e9921b6f71d33e25dd2f3cf53","f72578721db56bf8f49538b0ae6ea470c2fb1339dd26333f135f7def45376ec0","e449a03eab359e34095f8b4b55cd7ac7c0ec6510f2c4cc79fa6b1fee6b18c59e","73bd6978c59f2b219449b36770fb313fbe2da28f6b04275f071a1b193dde2072"]

H0_224=util.hex2ba('2dfedd62f99a98acae7cacd619d634e7a4831005bc301216b86038c6c966149466d9899f2580706fce9ea31b1d9b1adc11e8325f7b366e10f994857f02fa06c11b4f1b5cd8c840b397f6a17f6e738099dcdf93a5adeaa3d3a431e8dec9539a6822b4a98aec86a1e4d574ac959ce56cf015960deab5ab2bbf9611dcf0dd64ea6e')
H0_256=util.hex2ba('eb98a3412c20d3eb92cdbe7b9cb245c11c93519160d4c7fa260082d67e508a03a4239e267726b945e0fb1a48d41a9477cdb5ab26026b177a56f024420fff2fa871a396897f2e4d751d144908f77de262277695f776248f9487d5b6574780296c5c5e272dac8e0d6c518450c657057a0f7be4d367702412ea89e3ab13d31cd76')
H0_384=util.hex2ba('481e3bc6d813398a6d3b5e894ade879b63faea68d480ad2e332ccb21480f826798aec84d9082b928d455ea304111424936f555b2924847ecc7250a93baf43ce1569b7f8a27db454c9efcbd496397af0e589fc27d26aa80cd80c08b8c9deb2eda8a7981e8f8d5373af43967adddd17a71a9b4d3bda475d394976c3fba9842737f')
H0_512=util.hex2ba('6fd14b963e00aa17636a2e057a15d5438a225e8d0c97ef0be9341259f2b3c361891da0c1536f801e2aa9056bea2b6d80588eccdb2075baa6a90f3a76baf83bf70169e60541e34a6946b58a8e2e6fe65a1047a7d0c1843c243b6e71b12d5ac199cf57f6ec9db1f856a706887c5716b156e3c2fcdfe68517fb545a4678cc8cdd4b')


for i in range(0,42):
    C[i]=util.hex2ba(C[i])

S=[[9, 0, 4, 11, 13, 12, 3, 15, 1, 10, 2, 6, 7, 5, 8, 14],[3, 12, 6, 13, 5, 7, 1, 9, 15, 2, 0, 4, 11, 10, 14, 8]]

def L(A,B):
    D=bitarray([B[0] ^ A[1], B[1] ^ A[2], B[2] ^ A[3] ^ A[0], B[3] ^ A[0]])
    C=bitarray([A[0] ^ D[1], A[1] ^ D[2], A[2] ^ D[3] ^ D[0], A[3] ^ D[0]])
    return (C,D)

def pi(arr):
    res=[None]*len(arr)
    for i in range(0,len(arr),4):
        res[i]=arr[i]
        res[i+1]=arr[i+1]
        res[i+2]=arr[i+3]
        res[i+3]=arr[i+2]
    return res

def pp(arr):
    res=[None]*len(arr)
    l=len(arr)//2
    for i in range(0,l):
        res[i]=arr[2*i]
    for i in range(0,l):
        res[i+l]=arr[2*i+1]
    return res

def fi(arr):
    res=[None]*len(arr)
    for i in range(0,len(arr)//2):
        res[i]=arr[i]
    for i in range(len(arr)//2,len(arr),2):
        res[i+1]=arr[i]
        res[i]=arr[i+1]
    return res

def p(arr):
    return fi(pp(pi(arr)))


def R(bits, c):
    v=[]
    for i in range(0,len(bits)//4):
        v.append(util.int2ba(S[c[i]][util.ba2int(bits[4*i:4*i+4])],4))

    for i in range(0,len(v),2):
        outl=L(v[i],v[i+1])
        v[i]=outl[0]
        v[i+1]=outl[1]
    res=bitarray()
    v=p(v)
    for i in v:
        res+=i
    return res

def E(A):
    l=len(A)//8
    Q=bitarray()
    for i in range(0,l):
        Q.append(A[i])
        Q.append(A[2*l+i])
        Q.append(A[4*l+i])
        Q.append(A[6*l+i])
        Q.append(A[l+i])
        Q.append(A[3*l+i])
        Q.append(A[5*l+i])
        Q.append(A[7*l+i])
    for i in range(0,6*(d-1)):
        Q=R(Q,C[i])
    B=len(A)*bitarray('0')
    for i in range (0,l):
        B[i]=Q[8*i]
        B[l+i]=Q[8*i+4]
        B[2*l+i]=Q[8*i+1]
        B[3*l+i]=Q[8*i+5]
        B[4*l+i]=Q[8*i+2]
        B[5*l+i]=Q[8*i+6]
        B[6*l+i]=Q[8*i+3]
        B[7*l+i]=Q[8*i+7]
    return B

def F(H,M):
    A=H^(M+2**(d+1)*bitarray('0'))
    B=E(A)
    out=B^(2**(d+1)*bitarray('0')+M)
    return out

def msgtobits(msg):
    if(type(msg)==int):
        return util.int2ba(msg)
    if(type(msg)==bitarray):
        return msg
    if(type(msg)==bytes):
        b=bitarray()
        b.frombytes(msg)
        return b
    if(type(msg)==str):
        b=bitarray()
        b.frombytes(bytes(msg,'ascii'))
        return b
    raise TypeError

def JH224(message):
    M=msgtobits(message)
    l=len(M)
    M.append(1)
    M.extend([0]*(383+((-l)%512)))
    M+=util.int2ba(l,128)
    m=len(M)//512
    H=deepcopy(H0_224)
    for i in range(0,m):
        H=F(H,M[512*i:512*i+512])
    return util.ba2hex(H[800:])

def JH256(message):
    M=msgtobits(message)
    l=len(M)
    M.append(1)
    M.extend([0]*(383+((-l)%512)))
    M+=util.int2ba(l,128)
    m=len(M)//512
    H=deepcopy(H0_256)
    for i in range(0,m):
        H=F(H,M[512*i:512*i+512])
    return util.ba2hex(H[768:])

def JH384(message):
    M=msgtobits(message)
    l=len(M)
    M.append(1)
    M.extend([0]*(383+((-l)%512)))
    M+=util.int2ba(l,128)
    m=len(M)//512
    H=bitarray('0000000110000000')+1008*bitarray('0')
    H=F(H,512*bitarray('0'))
    for i in range(0,m):
        H=F(H,M[512*i:512*i+512])
    return util.ba2hex(H[640:])

def JH512(message):
    M=msgtobits(message)
    l=len(M)
    M.append(1)
    M.extend([0]*(383+((-l)%512)))
    M+=util.int2ba(l,128)
    m=len(M)//512
    H=bitarray('0000001000000000')+1008*bitarray('0')
    H=F(H,512*bitarray('0'))
    for i in range(0,m):
        H=F(H,M[512*i:512*i+512])
    return util.ba2hex(H[512:])
