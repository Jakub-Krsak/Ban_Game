import pygame
import random

pygame.mixer.init()
pygame.init()
screen_width = 500
screen_height = 650 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("BAN_GAME")

explode_img = pygame.image.load("./img/tile021.png")
ban_image = pygame.transform.scale(pygame.image.load("./img/ban_user.png"), [60,60])
restart_img = pygame.transform.scale(pygame.image.load("./img/Quick_restart.png"), [150,150])
walkLeft = [pygame.image.load("./img/hero4.png"),pygame.image.load("./img/hero5.png"),pygame.image.load("./img/hero6.png")]
walkRight = [pygame.image.load("./img/hero7.png"),pygame.image.load("./img/hero8.png"),pygame.image.load("./img/hero9.png")]
img_standing = pygame.image.load("./img/hero10.png")
bg = pygame.image.load("./img/2d_bg_game.png")
tary = pygame.transform.scale(pygame.image.load("./img/tary_icon.png"), [65,78])
fizistyle = pygame.transform.scale(pygame.image.load("./img/fizistyle.png"), [74,77])
datel = pygame.transform.scale(pygame.image.load("./img/datel.png"), [65,87])
kajumi = pygame.transform.scale(pygame.image.load("./img/Adam_Kajumi.png"), [83,94])
ondra = pygame.transform.scale(pygame.image.load("./img/ondra_vlcek.png"), [65,87])
fanfun = pygame.transform.scale(pygame.image.load("./img/fan_fun.png"), [70,80])

label = pygame.image.load("./img/Label.png")
health = pygame.transform.scale(pygame.image.load("./img/health_2.png"), [30,30])

ale_ban = pygame.mixer.Sound("./sounds/sound16bit.wav")
music = pygame.mixer.music.load("./sounds/Dusan_Ac_Ci_Koky.mp3")

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

clock = pygame.time.Clock()
running_game = True

class dusan(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 20
        self.left = False
        self.right = False
        self.standing = True
        self.walkCount = 0

    def draw(self, screen): 
        if self.walkCount + 1 >= 10:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            screen.blit(img_standing, (self.x,self.y + 8))

class BAN(object):
    def __init__(self,x,y,width,height,radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.shot = False
        self.radius = radius
        #self.hit_box = (self.x, self.y, 60, 60)

    def draw(self,screen):
        self.y -= self.speed
        screen.blit(ban_image, (self.x, self.y))
        #self.hit_box = (self.x, self.y, 60, 60)
        #pygame.draw.rect(screen, (0,0,179), self.hit_box, 2)

class youtuberi(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.shot = False
        self.nahodne = random.randint(1,7)
        #self.hit_box = (self.x, self.y, 65, 76)
    
    def draw(self,screen):
        self.y += self.speed
        if self.nahodne == 1:
            screen.blit(tary, (self.x, self.y))
        if self.nahodne == 2:
            screen.blit(fanfun, (self.x, self.y))
        if self.nahodne == 3:
            screen.blit(fizistyle, (self.x, self.y))
        if self.nahodne == 4:
            screen.blit(kajumi, (self.x, self.y))
        if self.nahodne == 5:
            screen.blit(datel, (self.x, self.y))
        if self.nahodne == 6 or self.nahodne == 7:
            screen.blit(ondra, (self.x, self.y))
        #self.hit_box = (self.x, self.y, 65, 76)
        #pygame.draw.rect(screen, (0,0,179), self.hit_box, 2)


def redrawGameWindow(killed, zivoty):
    screen.blit(bg, (0,0))
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render('Banned: '+str(killed), True, (255, 255, 50))
    screen.blit(label, (50,-155))
    screen.blit(text, (185,25))

    if zivoty == 3:
        for i in range(20,140,40):
            screen.blit(health, (i, screen_height - 35))
    elif zivoty == 2:
        for i in range(20,100,40):
            screen.blit(health, (i,screen_height-35))
    elif zivoty == 1:
        screen.blit(health, (20,screen_height-35))
    man.draw(screen)
    for banik in banik_list:
        if banik.y > 0:
            banik.draw(screen)
        else:
            banik_list.pop(banik_list.index(banik))
    
    for youtuber in youtuberi_list:
        if youtuber.y < 520:
            youtuber.draw(screen)
        else:
            youtuberi_list.pop(youtuberi_list.index(youtuber))
    pygame.display.update()

#MainLoop
man = dusan(50, 480, 64, 64)
banik_list = []
youtuberi_list = []
shot_Loop = 0
zivoty = 3
killed = 0
while running_game:
    youtuberi_choice = random.randint(1,15)
    timer = random.randint(1,2)
    
    
    if youtuberi_choice == 1:
        youtuberi_list.append(youtuberi(random.randint(20,screen_width-80), 10, 50, 50))
    else:
            None
    
    #youtuberi_list.append(youtuberi(random.randint(20,480), 10, 50, 50))
    
    if shot_Loop > 0:
        shot_Loop += 1 
    if shot_Loop > 5:
        shot_Loop = 0

    for banik in banik_list:
        for youtuber in youtuberi_list:
            if abs(banik.y - youtuber.y) < banik.width and abs(banik.x - youtuber.x) < banik.width:
                #print('Hitol som ta cavo!')
                ale_ban.play()
                screen.blit(explode_img, (banik.x,banik.y-20))
                pygame.display.update()
                banik_list.pop(banik_list.index(banik))
                youtuberi_list.pop(youtuberi_list.index(youtuber))
                killed += 1
    for youtuber in youtuberi_list:
        if youtuber.y > man.y:
            zivoty -= 1
            screen.blit(explode_img, (youtuber.x,youtuber.y))
            pygame.display.update()
            youtuberi_list.pop(youtuberi_list.index(youtuber))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and man.x > 9.5:
        man.x -= man.speed # x=x-vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_d] and man.x < 495-man.width - man.speed:
        man.x += man.speed # x=x+vel
        man.left = False
        man.right = True
        man.standing = False
    elif keys[pygame.K_SPACE] and shot_Loop == 0:
        banik_list.append(BAN(man.x, man.y, 50, 50, 30))
        shot_Loop = 1
    
    else:
        man.standing = True
        man.walkCount = 0

    if event.type == pygame.MOUSEBUTTONUP:
        mouse = pygame.mouse.get_pos()
        zivoty = 3
        killed = 0
        youtuberi_list = []
        banik_list = []
        pygame.mixer.music.play(-1)
    
    if zivoty > 0:
        redrawGameWindow(killed, zivoty)
    
    else:
        screen.blit(bg, (0,0))
        font = pygame.font.SysFont("comicsansms", 94)
        text = font.render('GAME OVER!!!', True, (255, 0, 0))
        screen.blit(text, (20, 50))
        pygame.mixer.music.pause()
        screen.blit(restart_img, (160,200))
        pygame.display.update()
     
    clock.tick(60)
pygame.mixer.music.stop()
pygame.quit()










"""KONEC"""