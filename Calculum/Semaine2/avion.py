sample_input1 = """N-FBI1
9A-USKOK
I-NTERPOL
G-MI6
RF-KGB1"""


sample_input2 = """N321-CIA
F3-B12I
F-BI-12
OVO-JE-CIA
KRIJUMCAR1
"""

sample_input3 = """47-FBI
BOND-007
RF-FBI18
MARICA-13
13A-FBILL"""

def avion(sample):
    words = sample.split('\n')
    idxs = []
    for i, word in enumerate(words):
        if 'FBI' in word:
            idxs.append(str(i+1))

    if idxs:
        print(' '.join(idxs))
    else:
        print('HE GOT AWAY!')

def avion2(sample):
    pass


avion(sample_input1)
avion(sample_input2)
avion(sample_input3)



