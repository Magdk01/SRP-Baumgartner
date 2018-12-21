from __future__ import division
import pygame
import time
import xlsxwriter
import math
from builtins import str
from cmath import sqrt
from _ast import Str



pygame.init()
pygame.font.init()
background_colour = (255, 255, 235)
(width, height) = (500, 600)
myfont = pygame.font.SysFont('Calibri', 30)
workbook = xlsxwriter.Workbook('Baungarten.xlsx')
worksheet = workbook.add_worksheet()

xplt =[]
yplt=[]
spdlist=[]
dislist = []
rholist = []
Fblist = []
airlist=[]
templist=[]
areslist=[]
g_0 = 9.82 #Gravity
k = 0.005 #Speed of sim
t = 1
runtime = 9999999 #Length of sim in secounds
length = 38969.4
h = length
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




screen = pygame.display.set_mode((width, height))

if 0.1 >= t > 1:
    k = 0.0005
if t <= 1:
    k = 0.05
if t < 0.1:
    k= 0.0005
    
class Ball:
    
    def __init__ (self,y,x,size,):
        self.y = y
        self.size = size
        self.color = (255,0,0)
        self.x = x
        self.t = t
        self.speed = speed
        self.dis = h
        self.rho = 0
        self.F_air = 0
        self.g_h = 0
        self.g_r = 0
        self.vv = 0
        self.p = 0
        self.temp = 0
        self.pres = 0
        
    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y/100)),size,0)

        
    def move1(self):
        self.t += t
        self.vv += self.g_r * t
        self.y += self.vv*t
        self.dis = h-self.y
        
        self.speed = self.vv
        #print("Distance= " + str(self.dis))
        #print("Speed=" + str(self.speed))
        
        print("Time= " + str(self.t))
 
    def Onscreen(self):
        textsurface1 = myfont.render("speed= " + str(self.speed), False, (0, 0, 0))
        screen.blit(textsurface1,(0,0))
        textsurface1_1 = myfont.render("m/s", False, (0, 0, 0))
        screen.blit(textsurface1_1,(430,0))
        textsurface2 = myfont.render("time= " + str(self.t) , False, (0, 0, 0))
        screen.blit(textsurface2,(0,50))
        textsurface2_1 = myfont.render("s", False, (0, 0, 0))
        screen.blit(textsurface2_1,(430,50))
        textsurface3 = myfont.render("place= " + str(self.y), False, (0, 0, 0))
        screen.blit(textsurface3,(0,100))
        textsurface3 = myfont.render("acceleration " + str(self.g_r), False, (0, 0, 0))
        screen.blit(textsurface3,(0,150))
        
    def fysikPT(self):
            if 0 < self.dis <=11000:
                self.pres = (101.29*((((self.temp+273.1)/288.08)**(5.256))))
            if  11000 < self.dis <=25100:
                self.pres = (22.56*math.exp(1.73-0.000157*self.dis))
            if  25100 < self.dis :
                self.pres = (2.488*((self.temp+273.1)/216.6)**(-11.388))
        
            
    def fysik(self):
            #self.rho = 1.3953329106*0.9998570739**self.dis
            
            self.rho = (self.pres*Molarmass)/(8.3145*(self.temp+273.15))
            
            self.F_air = -(0.5*self.rho*(self.speed**2)*A*C_d)
            self.g_air = self.F_air/mass
            #self.g_h = g_0*(re/(re+self.dis))**2
            self.g_h= (6.67*10**(-11))*((m_earth)/((re+self.dis)**2))
            self.g_r = self.g_h + self.g_air
            print("rho= " + str(self.rho))

            
           
            #print("Luftmodstand  " + str(self.g_air))
            #print("RHO  "+str(self.rho))
            #print("GR  " +str(self.g_r))
            print("dis= " + str(self.dis))
            print("pres=" + str(self.pres))
            
            #print("rho = " + str(self.rho))
            
    def air_speed(self):
            if 0 < self.dis <=11000:
                self.temp = 15.04-0.00649*self.dis
            if  11000 < self.dis <=25100:
                self.temp = -56.46
            if  25100 < self.dis :
                self.temp = -131.21+0.00299*self.dis
                
            self.v_air = math.sqrt(gamma*R_spec*(273.15 + self.temp))
            
            #print("v_air+ " + str(self.v_air))
            #print ("luft speed=" + str(self.v_air))
            #print("temp= " + str(self.temp))
            

#ball rules
y = 0
x1 = 250
x2 = 300
size=7
speed = 0
screenpos = 0


ball1 = Ball(y,x1,size,)






running = True
while running: # Keeps the window open until user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(background_colour)
    #if ball1.t >= runtime:
        #break
    if ball1.y >= length:
        break
    
    
    ball1.air_speed() 
    ball1.fysikPT()
    ball1.fysik()
    ball1.move1()
    
    
    if ball1.v_air > ball1.vv:
        background_colour = (255, 255, 235)
    if ball1.v_air < ball1.vv:
        background_colour = (0, 255, 0)
     
    ball1.Onscreen()
    ball1.display()
    
   

    
    
    time.sleep(0.50)
    
    yplt.append(ball1.y)
    spdlist.append(ball1.speed)
    dislist.append(ball1.dis)
    rholist.append(ball1.rho)
    Fblist.append(ball1.F_air)
    airlist.append(ball1.v_air)
    templist.append(ball1.temp)
    areslist.append(ball1.g_r)
    pygame.display.flip()

i=0
worksheet.write(i,0,"Tid/s")
worksheet.write(i,1,"Sted/m")
worksheet.write(i,2,"Fart/(m/s)")
worksheet.write(i,3,"Distance til jorden/m")
worksheet.write(i,4,"Luftdensitet/(kg/m^3)")
worksheet.write(i,5,"Modsatrettet kraft/N")
worksheet.write(i,6,"Luft speed")
worksheet.write(i,7,"Temperatur")
worksheet.set_column('D:F', 20, )
worksheet.set_column('C:C', 12, )
worksheet.write(i,8,"resulterende acceleration")

while i<len(yplt):
    time = i*t+t
    
    worksheet.write(i+1,0,time)
    
    worksheet.write(i+1,1,yplt[i])
    
    worksheet.write((i+1),2,spdlist[i])
    
    worksheet.write(i+1,3,dislist[i])
    
    worksheet.write(i+1,4,rholist[i])
    
    worksheet.write(i+1,5,Fblist[i])
    
    worksheet.write(i+1,6,airlist[i])
    
    worksheet.write(i+1,7,templist[i])
    
    worksheet.write(i+1,8,areslist[i])

    
    i +=1
workbook.close()
    