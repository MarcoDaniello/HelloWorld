import math

print "Risolve equazioni di secondo grado"


A = input('A: ')
B = input('B: ')
C = input('C: ')

if A==0 and B==0 and C==0:
    print "L'equazione 0 = 0 ammette infinite soluzioni"

elif A==0 and B==0:
    print "L'equazione non ammette soluzioni"

elif A==0:
    print "L'equazione si riduce al primo grado"
    print  -float(C) / float(B)

else:
    delta = B * B - 4 * A * C
    if delta < 0:
        print " L'equazione ammette due soluzioni"
        rad_delta = math.sqrt(-delta)
        re = -float(B) / (2.0 * float(A))
        imm = abs(rad_delta / (2.0 * float (A)))
        print "x1 =", re, "-i", imm
        print "x2 =", re, "+i", imm
    elif delta == 0:
        print " L'equazione ammette due soluzioni coincidenti"
        print "x1 = x2 =", -float(B) / (2.0 * float(A))
    else:
        print "L'equazione ammette due soluzioni distinte"
        rad_delta = math.sqrt(delta)
        print "x1 =", (-float(B) - rad_delta) / (2.0 * float(A))
        print "x2 =", (-float(A) + rad_delta) / (2.0 * float(A))
