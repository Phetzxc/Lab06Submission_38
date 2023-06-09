class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(250,0,0),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        if (pg.mouse.get_pos()[0]>=20 and pg.mouse.get_pos()[0]<=120) and (pg.mouse.get_pos()[1]>=20 and pg.mouse.get_pos()[1]<=120):
            return True
        else:
            return False
    def get_pressed(self):
        if (pg.mouse.get_pressed()[0]==1):
            return True
        else:
            return False
import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
# firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา


while(run):
    screen.fill((255, 255, 255))
    # firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    
    pg.draw.rect(screen,(220,220,220),(btn.x,btn.y,btn.w,btn.h))
    pg.display.update()
    for event in pg.event.get():
        
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D down")
            btn.x+=10
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม A
            print("Key A down")
            btn.x-=10
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
            print("Key W down")
            btn.y-=10
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม S
            print("Key S down")
            btn.y+=10
        # if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
        #     print("Key A up")
        
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False