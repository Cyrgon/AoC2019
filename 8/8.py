
rows = 6
cols = 25

with open('input.txt') as f:
    for line in f:

        #Part 2
        line = line.strip()
        for i in range(0, rows * cols):
            if i % cols == 0:
                print("")
            pos = i
            while pos < len(line):
                if line[pos] != '2':
                    if line[pos] == '1':
                        print 'O',
                    else:
                        print ' ',
                    break
                pos += rows * cols

        #Part 1
        minZ = 10000
        res = 0
        count = 0
        sums = {}
        for p in line:
            if p not in sums:
                sums[p] = 0
            sums[p] += 1
            count += 1

            if count > rows * cols:
                count = 0
                if sums['0'] < minZ:
                    minZ = sums['0']
                    res = sums['1'] * sums['2']
                sums = {}
                count = 0

        print("\n\n1: " + str(res))
