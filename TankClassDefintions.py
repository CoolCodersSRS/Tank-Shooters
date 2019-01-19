import pygame
import time
import math
from TankSettings import *
vd = pygame.math.Vector2

class Bullet(pygame.sprite.Sprite):
    def __init__(self,game,kind,pos,ang):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.ang = ang
        if kind == 1:
            self.image = pygame.Surface((5,5))
            self.image.fill(RED)
        self.pos = vd(pos.x,pos.y)
        self.rect = self.image.get_rect()
        self.rect.center = (pos.x,pos.y)
        self.vel = vd(BULLET_SPEED * math.cos(math.radians(self.ang)), BULLET_SPEED * math.sin(math.radians(self.ang)))

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        collide = pygame.sprite.spritecollide(self,self.game.platforms,False)
        if self.pos.x > WIDTH:
            self.kill()
        if self.pos.x < 0:
            self.kill()
        if collide:
            self.kill()

class Nozzle(pygame.sprite.Sprite):
    def __init__(self,player,pos):
        pygame.sprite.Sprite.__init__(self)
        self.main_image_nozzle = pygame.image.load('picture.gif')
        self.image = self.main_image_nozzle
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.centerx = pos.x + 15
        self.rect.centery = pos.y - 15
        self.angle = 0
        self.pos = pos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.angle += 2
        if keys[pygame.K_f]:
            self.angle += -2
        self.rect.centerx = self.pos.x + 15
        self.rect.centery = self.pos.y - 15
        self.image = pygame.transform.rotate(self.main_image_nozzle,self.angle)
        self.xx = self.rect.centerx
        self.yy = self.rect.centery
        self.rect = self.image.get_rect()
        self.rect.center = (self.xx,self.yy)


    def Function1(self,pos):
        self.rect.centerx = pos.x + 15
        self.rect.centery = pos.y - 15
        self.pos.x = pos.x
        self.pos.y = pos.y

class Player(pygame.sprite.Sprite):
    def __init__(self,game,sprl):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.sprl = sprl
        self.main_image_player  = pygame.image.load('picture.gif')
        self.image = self.main_image_player
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH * 3/4, HEIGHT / 2)
        self.pos = vd(WIDTH * 3/4, HEIGHT / 2)
        self.vel = vd(0,0)
        self.acc = vd(0,0)
        self.dir = 2
        self.nozzle = Nozzle(self,self.pos)
        self.sprl.add(self.nozzle)
    def jump(self):
        self.rect.x += 1
        collide = pygame.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x += -1
        if collide:
            self.vel.y = JUMP

    def update(self):
        self.acc = vd(0,GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x += -ACCELERATION
            if self.dir == 2:
                self.nozzle.angle += 180
                self.nozzle.pos.x -= 10
            self.dir = 1
        if keys[pygame.K_RIGHT]:
            self.acc.x += ACCELERATION
            if self.dir == 1:
                self.nozzle.angle -= 180
                self.nozzle.pos.x += 10
            self.dir = 2
            
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.midbottom = self.pos
        self.nozzle.Function1(self.pos)

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x  = x
        self.rect.y = y
        



            

















                      
        







                      
