import math

print "Calcolo della superficie e del volume di una sfera"
raggio = input("inserisci il valore del raggio")
superficie = 4. * math.pi *  raggio * raggio
volume = 4. / 3. * math.pi * raggio * raggio * raggio
print "La sfera di raggio", raggio , "ha una superficie di", superficie, "ha volume", volume 
