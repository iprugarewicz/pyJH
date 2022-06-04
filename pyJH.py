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

d=8

C=["72d5dea2df15f8677b84150ab723155781abd6904d5a87f64e9f4fc5c3d12b40","ea983ae05c45fa9c03c5d29966b2999a660296b4f2bb538ab556141a88dba231","03a35a5c9a190edb403fb20a87c144101c051980849e951d6f33ebad5ee7cddc","10ba139202bf6b41dc786515f7bb27d00a2c813937aa78503f1abfd2410091d3","422d5a0df6cc7e90dd629f9c92c097ce185ca70bc72b44acd1df65d663c6fc23","976e6c039ee0b81a2105457e446ceca8eef103bb5d8e61fafd9697b294838197","4a8e8537db03302f2a678d2dfb9f6a958afe7381f8b8696c8ac77246c07f4214","c5f4158fbdc75ec475446fa78f11bb8052de75b7aee488bc82b8001e98a6a3f4","8ef48f33a9a36315aa5f5624d5b7f989b6f1ed207c5ae0fd36cae95a06422c36","ce2935434efe983d533af974739a4ba7d0f51f596f4e81860e9dad81afd85a9f","a7050667ee34626a8b0b28be6eb9172747740726c680103fe0a07e6fc67e487b","0d550aa54af8a4c091e3e79f978ef19e8676728150608dd47e9e5a41f3e5b062","fc9f1fec4054207ae3e41a00cef4c9844fd794f59dfa95d8552e7e1124c354a5","5bdf7228bdfe6e2878f57fe20fa5c4b205897cefee49d32e447e9385eb28597f","705f6937b324314a5e8628f11dd6e465c71b770451b920e774fe43e823d4878a","7d29e8a3927694f2ddcb7a099b30d9c11d1b30fb5bdc1be0da24494ff29c82bf","a4e7ba31b470bfff0d324405def8bc483baefc3253bbd339459fc3c1e0298ba0","e5c905fdf7ae090f947034124290f134a271b701e344ed95e93b8e364f2f984a","88401d63a06cf61547c1444b8752afff7ebb4af1e20ac6304670b6c5cc6e8ce6","a4d5a456bd4fca00da9d844bc83e18ae7357ce453064d1ade8a6ce68145c2567","a3da8cf2cb0ee11633e906589a94999a1f60b220c26f847bd1ceac7fa0d18518","32595ba18ddd19d3509a1cc0aaa5b4469f3d6367e4046bbaf6ca19ab0b56ee7e","1fb179eaa9282174e9bdf7353b3651ee1d57ac5a7550d3763a46c2fea37d7001","f735c1af98a4d84278edec209e6b677941836315ea3adba8fac33b4d32832c83","a7403b1f1c2747f35940f034b72d769ae73e4e6cd2214ffdb8fd8d39dc5759ef","8d9b0c492b49ebda5ba2d74968f3700d7d3baed07a8d5584f5a5e9f0e4f88e65","a0b8a2f436103b530ca8079e753eec5a9168949256e8884f5bb05c55f8babc4c","e3bb3b99f387947b75daf4d6726b1c5d64aeac28dc34b36d6c34a550b828db71","f861e2f2108d512ae3db643359dd75fc1cacbcf143ce3fa267bbd13c02e843b0","330a5bca8829a1757f34194db416535c923b94c30e794d1e797475d7b6eeaf3f","eaa8d4f7be1a39215cf47e094c23275126a32453ba323cd244a3174a6da6d5ad","b51d3ea6aff2c90883593d98916b3c564cf87ca17286604d46e23ecc086ec7f6","2f9833b3b1bc765e2bd666a5efc4e62a06f4b6e8bec1d43674ee8215bcef2163","fdc14e0df453c969a77d5ac4065858267ec1141606e0fa167e90af3d28639d3f","d2c9f2e3009bd20c5faace30b7d40c30742a5116f2e032980deb30d8e3cef89a","4bc59e7bb5f17992ff51e66e048668d39b234d57e6966731cce6a6f3170a7505","b17681d913326cce3c175284f805a262f42bcbb378471547ff46548223936a48","38df58074e5e6565f2fc7c89fc86508e31702e44d00bca86f04009a23078474e","65a0ee39d1f73883f75ee937e42c3abd2197b2260113f86fa344edd1ef9fdee7","8ba0df15762592d93c85f7f612dc42bed8a7ec7cab27b07e538d7ddaaa3ea8de","aa25ce93bd0269d85af643fd1a7308f9c05fefda174a19a5974d66334cfd216a","35b49831db411570ea1e0fbbedcd549b9ad063a151974072f6759dbf91476fe2"]

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
        B[i]=Q[4*i]
        B[l+i]=Q[4*l+4*i]
        B[2*l+i]=Q[4*i+1]
        B[3*l+i]=Q[4*l+4*i+1]
        B[4*l+i]=Q[4*i+2]
        B[5*l+i]=Q[4*l+4*i+2]
        B[6*l+i]=Q[4*i+3]
        B[7*l+i]=Q[4*l+4*i+3]
    return B

def F(H,M):
    H=H^(M+2**(d+1)*bitarray('0'))
    H=E(H)
    H=H^(2**(d+1)*bitarray('0')+M)
    return H

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
        b.frombytes(bytes(msg,'utf-8'))
        return b
    raise TypeError

def JH224(message):
    M=msgtobits(message)
    l=len(M)
    M.append(1)
    M.extend([0]*(383+((-l)%512)))
    M+=util.int2ba(l,128)
    m=len(M)//512
    H=bitarray('0000000011100000')+1008*bitarray('0')
    H=F(H,512*bitarray('0'))
    for i in range(0,m):
        H=F(H,M[512*i:512*i+512])
    return util.ba2int(H[800:])

def JH256(message):
    M=msgtobits(message)
    l=len(M)
    M.append(1)
    M.extend([0]*(383+((-l)%512)))
    M+=util.int2ba(l,128)
    m=len(M)//512
    H=bitarray('0000000100000000')+1008*bitarray('0')
    H=F(H,512*bitarray('0'))
    for i in range(0,m):
        H=F(H,M[512*i:512*i+512])
    return util.ba2int(H[768:])

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
    return util.ba2int(H[640:])

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
    return util.ba2int(H[512:])
