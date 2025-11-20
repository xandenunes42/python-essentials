# Lei de Morgan
 

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

i = 15
j = 22

#imagem bit a bit 
# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110

log = i and j
#true 

bit = i & j
# 000000000000000000000000000 00110 -> valor 6

logneg = not i

#negacao bit a bit 
bitneg = ~i
# i:  00000000000000000000000000001111 
# ~i: 11111111111111111111111111110000 -> valor -16



 


