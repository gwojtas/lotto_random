import random
import math
from time import sleep



zestaw_liczb=[]
zestaw_szesciu=[]
wylosowane_zestawy=[]
temp=[]
x=1
ilosc_losowanych = 3
ilosc_wszystkich  = 5

silnia = (ilosc_wszystkich)

for i in range (1,(ilosc_wszystkich+1)):
    zestaw_liczb.append(i)
   # print (zestaw_liczb)



#for i in range (1,10):
while len(wylosowane_zestawy) < (math.factorial(ilosc_wszystkich))/((math.factorial(ilosc_losowanych))*(math.factorial(ilosc_wszystkich - ilosc_losowanych))):
 
    
    for i in range (1,(ilosc_losowanych+1)):  

        wylosowana = random.choice(zestaw_liczb)
        zestaw_szesciu.append(wylosowana)
        zestaw_liczb.remove(wylosowana)
        zestaw_szesciu.sort()
        
        
    temp=zestaw_szesciu.copy()
    zestaw_liczb.sort()
    #print(x,' ',zestaw_szesciu,' pozostale: ',zestaw_liczb)
    zestaw_szesciu.clear()
    zestaw_liczb = zestaw_liczb + temp   
    x +=1
    if temp not in wylosowane_zestawy:
        wylosowane_zestawy.append(temp)
        #print (wylosowane_zestawy)
    continue
#wylosowane_zestawy.sort()    
print ('ilosc wylosowanych zestawow: ',len(wylosowane_zestawy))
print ('te zestawy to: ') 
z=1
for Q in wylosowane_zestawy:
    print (z,' :',Q)
    sleep(0.3)

    z+=1
    