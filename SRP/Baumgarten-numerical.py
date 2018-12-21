import pygame
from builtins import range
import time
import math
import xlsxwriter
from scipy.special.basic import euler



pygame.init()
pygame.font.init()
background_colour = (255, 255, 235)
myfont = pygame.font.SysFont('Calibri', 30)
(width, height) = (500, 600)

screen = pygame.display.set_mode((width, height))

workbook = xlsxwriter.Workbook('BaumgartenNUM.xlsx')
worksheet = workbook.add_worksheet()


t=0.1
tid = 0
x = 0

x_0=0
target=40
BK = 0.0051

height = 38969.4

y_0= height
A = 0.6
C_d = 1.1
v = 0
re = 6371000
mass = 140
gamma = 1.4
R = 8.3145
R_spec = 286
m_earth = 5.972*10**24
Molarmass = 28.9644
skridt = 10

dy=0
#Haeldning


eulerspeedlist=[]
dis1list=[]
RK4list=[]

class Baumgarten:
    
    def __init__(self,y,x,size,):
        self.y = 0
        self.v = 0
        self.a = 0
        self.size = size
        self.color = (255,0,0)
        self.x = 0
        self.time= 0
        self.y_n = 0
        self.y1 = 0
        self.place = x
        self.ye_n = y_0
        self.dy = 2
        self.k1 = 0
        self.k2 = 0
        self.k3 = 0
        self.k4 = 0
        self.M = 0
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.yr = 0
        self.yr_n = 0
        
        self.temp1 = 0
        self.pres1 = 0
        self.rho1 = 0
        self.F_air1 = 0
        self.g_h1 = 0
        self.g_r1 = 0
        self.v_air1 = 0
        self.dis1 = height
        self.speed1 = 0.1
        
        self.dis2 = height
        self.speed2 = 0.1
        self.temp2 = 0
        self.pres2 = 0
        self.rho2 = 0
        self.F_air2 = 0
        self.g_h2 = 0
        self.g_r2 = 0
        self.v_air2 = 0
        
        
        
    def skridt(self):
        
        self.dis1 = self.dis1-skridt
        self.dis2 = self.dis2-skridt        
    def Eulers(self):
        
        
        
        #print("speed= " + str(self.speed1) + " time= " +str(self.time))
        #print("place= " + str(self.dis1) )
        
        self.y_n = (BK*self.y*self.rho1-(2*self.g_h1))
        
        self.y = self.y-(self.y_n*skridt)
        
        
        self.speed1 = math.sqrt(self.y)
        
        #print("haeldning= " + str(self.y_n))
        print()
        
    def RK4(self):
    
     
        
        self.k1 = (BK*self.yr*self.rho2-(2*self.g_h2))
        self.y1 = self.yr - (self.k1*0.5*skridt)
        
        self.k2 = (BK*self.y1*self.rho2-(2*self.g_h2))
        self.y2 = self.yr - (self.k2*0.5*skridt)
        
        self.k3 = (BK*self.y2*self.rho2-(2*self.g_h2))
        self.y3 = self.yr  - (self.k3*skridt)
        
        self.k4 = (BK*self.y3*self.rho2-(2*self.g_h2))
        
        self.M = (1/6)*(self.k1 + (2*self.k2) + (2*self.k3) + self.k4)
        
        self.yr = self.yr - (self.M*skridt)
        
        self.speed2 = math.sqrt(self.yr)
        
        print("haeldning= " + str(self.yr))
        
        
    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.place+50),int(self.speed1)),size,0)
    

    def display3(self):
        pygame.draw.circle(screen, self.color, (int(self.place-50),int(self.speed2)),size,0)
    
    def fysik1(self):
        if 0 < self.dis1 <=11000:
            self.temp1 = 15.04-0.00649*self.dis1
        if  11000 < self.dis1 <=25100:
            self.temp1 = -56.46
        if  25100 < self.dis1 :
            self.temp1 = -131.21+0.00299*self.dis1

        if 0 < self.dis1 <=11000:
            self.pres1 = (101.29*((((self.temp1+273.1)/288.08)**(5.256))))
        if  11000 < self.dis1 <=25100:
            self.pres1 = (22.56*math.exp(1.73-0.000157*self.dis1))
        if  25100 < self.dis1 :
            self.pres1 = (2.488*((self.temp1+273.1)/216.6)**(-11.388))
                
        #self.rho1 = (self.pres1*Molarmass)/(8.3145*(self.temp1+273.15))
        self.rho1 = 1.3953329106*0.9998570739**self.dis1
        self.g_h1 = (6.67*10**(-11))*((m_earth)/((re+self.dis1)**2))
        print("rho= " + str(self.rho1))
        print("grav= " + str(self.g_h1))

        
        self.v_air1 = math.sqrt(gamma*R_spec*(273.15 + self.temp1))
        
    def fysik2(self):
        if 0 < self.dis2 <=11000:
            self.temp2 = 15.04-0.00649*self.dis2
        if  11000 < self.dis2 <=25100:
            self.temp2 = -56.46
        if  25100 < self.dis2 :
            self.temp2 = -131.21+0.00299*self.dis2

        if 0 < self.dis2 <=11000:
            self.pres2 = (101.29*((((self.temp2+273.1)/288.08)**(5.256))))
        if  11000 < self.dis2 <=25100:
            self.pres2 = (22.56*math.exp(1.73-0.000157*self.dis2))
        if  25100 < self.dis2 :
            self.pres2 = (2.488*((self.temp2+273.1)/216.6)**(-11.388))
                
        self.rho2 = (self.pres2*Molarmass)/(8.3145*(self.temp2+273.15))
        
        self.g_h2= (6.67*10**(-11))*((m_earth)/((re+self.dis2)**2))

        
        
        self.v_air = math.sqrt(gamma*R_spec*(273.15 + self.temp2))
        
        



y = 0
x1 = 250
x2 = 300
size=7
baum = Baumgarten(y,x1,size,)




running = True
while running: # Keeps the window open until user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(background_colour)
    
    if baum.dis2 <= 0:
        break
    
    baum.fysik1()
    baum.fysik2()
    
    baum.Eulers()

    baum.RK4()
    baum.skridt()
    
    
    baum.display()
    baum.display3()
    
    #time.sleep(0.00005)
    pygame.display.flip()
    
    
    dis1list.append(baum.dis1)
    eulerspeedlist.append(baum.speed1)
    RK4list.append(baum.speed2)
    
i=0

worksheet.write(i,0,"Hoejde")
worksheet.write(i,1,"Eulers")
worksheet.write(i,2,"RK4")







while i<len(dis1list):
    time = i*t+t
    
    worksheet.write(i+1,0,dis1list[i])
    
    worksheet.write(i+1,1,eulerspeedlist[i])
    
    
    worksheet.write((i+1),2,RK4list[i])

    
    
    
    i +=1
workbook.close()