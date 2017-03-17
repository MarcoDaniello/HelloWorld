import math
print "programma che calcola volume di un cubo o di una sfera in base alla scelta dell'utente" 
s = input ( "Effettua scelta 1=cubo, 2=sfera")

if (s==1):
   lato = input("Inserisci lato del cubo ")
   volume = lato*lato*lato
   print ("Il volume del cubo risulta essere"), volume
elif s==2:
   raggio = input("Inserisci raggio ")
   volume = 4. / 3. * math.pi * raggio * raggio * raggio
   print ("il volume della sfera risulta essere"), volume
   
