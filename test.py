from bitarray import bitarray, util
import pyJH

for a in ["224", "256", "384", "512"]:
    f = open(f'LongMsgKAT_{a}.txt', 'r')
    for i in range(4):
        f.readline()
    for i in range(512):
        length = int(f.readline().split(' = ')[1])
        msg = util.hex2ba((f.readline().split(' = ')[1]).replace('\n', ""))
        digest = f.readline().split(' = ')[1]
        l = len(msg)
        if length != l:
            msg = msg[:(length - l)]
        print(length, len(msg))
        exec(f"print(pyJH.JH{a}(msg).lower().strip()==digest.lower().strip())")
