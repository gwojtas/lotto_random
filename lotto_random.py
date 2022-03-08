import random
import math
from time import sleep



set_of_numbers=[]
drawn_numbers=[]
drawn_sets=[]
temp=[]
x=1

number_of_balls = int(input('Select number of balls to be drawn:'))
size_of_cart  = int(input('Select number of balls in the cart:'))



for i in range (1,(size_of_cart+1)):
    set_of_numbers.append(i)

  

while len(drawn_sets) < (math.factorial(size_of_cart))/((math.factorial(number_of_balls))*(math.factorial(size_of_cart - number_of_balls))):
 
    
    for i in range (1,(number_of_balls+1)):  

        drawn = random.choice(set_of_numbers)
        drawn_numbers.append(drawn)
        set_of_numbers.remove(drawn)
        drawn_numbers.sort()
        
        
    temp=drawn_numbers.copy()
    set_of_numbers.sort()
    drawn_numbers.clear()
    set_of_numbers = set_of_numbers + temp   
    x +=1
    if temp not in drawn_sets:
        drawn_sets.append(temp)
        #print (drawn_sets)
    continue
#drawn_sets.sort()    
print ('Number of sets: ',len(drawn_sets))
print ('Drawn sets: ') 
z=1
for Q in drawn_sets:
    print (z,' :',Q)
    sleep(0.3)
    z+=1






