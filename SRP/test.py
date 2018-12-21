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

workbook = xlsxwriter.Workbook('EulerPY.xlsx')
worksheet = workbook.add_worksheet()


t=0.1
tid = 0
x = 0
y_0=3
x_0=0
target=40

dy=0
#Haeldning

eksaktlist=[]
eulerlist=[]
timelist=[]
RK4list=[]

class Baumgarten:
    
    def __init__(self,y,x,size,):
        self.y = y_0
        self.v = 0
        self.a = 0
        self.size = size
        self.color = (255,0,0)
        self.x = 0
        self.time= 0
        self.y_n = y_0
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
        self.yr_n = y_0
        

        
        
        
    def skridt(self):
        
        self.time +=t
                
    def Eulers(self):
        

        print("place= " + str(self.y) + " time= " +str(self.time))
        self.y = self.y_n
        
        
        
        
        self.y_n = self.y + t*self.y*self.dy
        
        
        time.sleep(0.1)
        
    def Eksakt(self):
        
        
        print("place2 = " + str(self.y1) + " time2 = " +str(self.time))
        
        
        
        self.ye_n = 3*math.exp(2*self.time)
        self.ye = self.ye_n
        
        
        
        print()
        
    def RK4(self):
    
        self.yr = self.yr_n
        
        
        
        self.k1 = self.dy*self.yr
        self.y1 = self.yr + self.k1*0.5*t
        self.k2 = self.dy*self.y1
        self.y2 = self.yr+self.k2*0.5*t
        self.k3 = self.dy*self.y2
        self.y3 = self.yr+self.k3*t
        self.k4 = self.dy*self.y3
        
        self.M = (1/6)*(self.k1 + (2*self.k2) + (2*self.k3) + self.k4)
        
        self.yr_n = self.yr + self.M*t

        
        
    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.place),int(self.y)),size,0)
    
    def display2(self):
        pygame.draw.circle(screen, self.color, (int(self.place+50),int(self.ye)),size,0)

    def display3(self):
        pygame.draw.circle(screen, self.color, (int(self.place-50),int(self.yr)),size,0)

        
        



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
    
    baum.Eulers()
    baum.Eksakt()
    baum.RK4()
    baum.skridt()
    
    baum.display()
    baum.display2()
    baum.display3()
    

    pygame.display.flip()
    
    
    timelist.append(baum.time)
    eulerlist.append(baum.y)
    eksaktlist.append(baum.ye)
    RK4list.append(baum.yr)
    
i=0

worksheet.write(i,0,"Tid/s")
worksheet.write(i,1,"Eulers")
worksheet.write(i,2,"Eksakt")
worksheet.write(i,3,"RK4")
worksheet.write(i+1,0,0)






while i<len(timelist):
    time = i*t+t
    
    worksheet.write(i+2,0,time)
    
    worksheet.write(i+1,1,eulerlist[i])
    
    worksheet.write((i+1),2,eksaktlist[i])
    
    worksheet.write((i+1),3,RK4list[i])

    
    
    
    i +=1
workbook.close()