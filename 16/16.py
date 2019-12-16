import sys

#Part 1
with open(sys.argv[1]) as f:
    sig = f.readline().strip()

sig = [int(x) for x in sig]
pattern = [0, 1, 0, -1]

def getPattern(length, offset):
    res = []
    skippedOnce = False
    while len(res) < length:
        for i in pattern:
            for j in range(0, offset + 1):
                if not skippedOnce:
                    skippedOnce = True
                    continue
                res.append(i)
    return res[:length]


def getFactor(position, offset):
    k = (position + 1) % (4 * (offset + 1))
    k = k // (offset + 1)
    return pattern[k]

def fft(signal):
    res = []
    for i in range(0, len(signal)):
        val = 0
        pat = getPattern(len(signal), i)
        for j in range(0, len(pat)):
            val += pat[j] * signal[j]
        res.append(abs(val) % 10)
    return res

for i in range(0, 100):
   sig = fft(sig)
print("".join([str(x) for x in sig[:8]]))

# Part 2
with open(sys.argv[1]) as f:
    sig = f.readline().strip()

signalMultipel = 10000

sig = [int(x) for x in sig] * signalMultipel

def part2(signal):
    res = []
    s = sum(signal)
    for i in range(0, len(signal)):
        res.append(s % 10)
        s -= signal[i]
    return res

offset = int("".join([str(x) for x in sig[:7]]))
newSig = sig[offset:]

for i in range(0, 100):
    newSig = part2(newSig)
print("".join([str(x) for x in newSig[:8]]))
