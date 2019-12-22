import sys
import intcode as ic

orgProg = ic.programFromFile(sys.argv[1])

nl = chr(10)

#Part 1
springscript = "NOT C J" + nl + "AND D J" + nl + "NOT A T" + nl + "OR T J" + nl + "WALK" + nl

springscript = [ord(x) for x in springscript]

(done, output, program, ip, rb) = ic.evaluate(orgProg.copy(), springscript, 0, 0)

for i in output:
    if i < 256:
        print chr(i),
    else:
        print(i)

#Part 2
springscript = "NOT C J" + nl + "AND D J" + nl + "AND H J" + nl + "NOT A T" + nl + "OR T J" + nl + "NOT B T" + nl + "AND D T" + nl + "OR T J" + nl + "RUN" + nl

springscript = [ord(x) for x in springscript]

(done, output, program, ip, rb) = ic.evaluate(orgProg.copy(), springscript, 0, 0)

for i in output:
    if i < 256:
        print chr(i),
    else:
        print(i)
