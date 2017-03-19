print "Programma che risolve un'equazione di primo grado nella forma Ax+B=0"
A = input ("Inserisci A ")
B = input ("Inserisci B ")

if A==0 and B==0:
    print "L'equazione ammette infinite soluzioni"

elif A==0:
    print "L'equazione non ammette soluzioni"


else :

     x = float(B) / float (A)
     
     print "L'equazione ha come soluzione :", x
