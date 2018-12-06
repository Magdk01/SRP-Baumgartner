import pygame
import time
import xlsxwriter
import math


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

g_0 = 9.82 #Gravity
k = 0.005 #Speed of sim
t = 1
runtime = 9999999 #Length of sim in secounds
length = 39000
h = length
A = 0.6
C_d = 1.3
v = 0
re = 6371000
mass = 140

screen = pygame.display.set_mode((width, height))

if 0.1 >= t > 1:
    k = 0.05
if t <= 1:
    k = 0.05
if t < 0.1:
    k= 0.05
    
class Ball:
    
    def __init__ (self,y,x,size,):
        self.y = y
        self.size = size
        self.color = (255,0,0)
        self.x = x
        self.t = t
        self.speed = speed
        self.dis = 0
        self.rho = 0
        self.F_air = 0
        self.g_h = 0
        self.g_r = 0
        self.vv = 0
    
    def display(self):
        ball = pygame.draw.circle(screen, self.color, (int(self.x),int(self.y/100)),size,0)
        #line = pygame.draw.circle(screen, self.color, (int(self.x+50),int(self.y/100)),size,0)
        #man = line + ball
        #man
        
    def move1(self):
        #if self.g_r > 0:
        self.vv += self.g_r * t
        
        self.y += self.vv/t
        self.dis = h-self.y
        self.t += t
        self.speed = self.vv/t
        print("Distance= " + str(self.dis))
        print("Speed=" + str(self.speed))
 
    def loop(self):
        if self.y == 600:
            self.y = 0
        elif self.y > 600:
            self.y = 0
    
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
    
    def fysik(self):
            self.rho = 1.3953329106*0.9998570739**self.dis
            #self.rho = 1
            self.F_air = -(0.5*self.rho*(self.speed**2)*A*C_d)
            self.g_air = self.F_air/mass
            self.g_h = g_0*(re/(re+self.dis))**2
            #self.g_h = g_0
            self.g_r = self.g_h + self.g_air
            
            print("Luftmodstand  " + str(self.g_air))
            print("RHO  "+str(self.rho))
            print("GR  " +str(self.g_r))
            
    

#Ball Rules
y = 0
x1 = 250
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
        
    if ball1.dis < 2000:
        C_d = 7
    else:
        C_d = 1.3  
    ball1.fysik()
    ball1.move1()   
    
    ball1.Onscreen()
    ball1.display()
    
    time.sleep(k)
    
    yplt.append(ball1.y)
    spdlist.append(ball1.speed)
    dislist.append(ball1.dis)
    rholist.append(ball1.rho)
    Fblist.append(ball1.F_air)
    #if ball1.g_r < 0:
    #   break
    pygame.display.flip()

i=0
worksheet.write(i,0,"Tid/s")
worksheet.write(i,1,"Sted/m")
worksheet.write(i,2,"Fart/(m/s)")
worksheet.write(i,3,"Distance til jorden/m")
worksheet.write(i,4,"Luftdensitet/(kg/m^3)")
worksheet.write(i,5,"Modsatrettet kraft/N")
worksheet.set_column('D:F', 20, )
worksheet.set_column('C:C', 12, )
while i<len(yplt):
    time = i*t+t
    
    worksheet.write(i+1,0,time)
    
    worksheet.write(i+1,1,yplt[i])
    
    worksheet.write((i+1),2,spdlist[i])
    
    worksheet.write(i+1,3,dislist[i])
    
    worksheet.write(i+1,4,rholist[i])
    
    worksheet.write(i+1,5,Fblist[i])
    
    i +=1
workbook.close()
    