import math
target= 40000



i = 0
temp = 0
pres = 0

def tempe():
    if 0 < i <=11000:
        temp = 15.04-0.00649*i
    if  11000 < i <=25100:
        temp = -56.46
    if  25100 < i :
        temp = -131.21+0.00299*i
        
        
def prese():
    
    if 0 < i <=11000:
        pres = 101.29*((((temp+273.1)/288.08)**(5.256)))
    if  11000 < i <=25100:
        pres = 22.56*math.exp(1.73-0.000157*i)
    if  25100 < i :
        pres = 2.488*((temp+273.1)/216.6)**(-11.388)
        
for i in range(0,target):
    tempe
    prese
    print("temp= " + str(temp))

   
    print("pres= " + str(pres))
    print("Run= " + str(i))
    i+1
    