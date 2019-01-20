import pygame
import random
import math
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
from TankClassDefintions import *
from TankSettings import *

class Game(ConnectionListener):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.Connect(('127.0.0.1', 8080))
        self.angleb = 0

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        connection.Pump()
        self.Pump()
        self.sprl.update()
        if self.player.vel.y > 0:
            collide = pygame.sprite.spritecollide(self.player,self.platforms, False)
            if collide:
                self.player.pos.y = collide[0].rect.top + 1
                self.player.vel.y = 0
        if self.kills >= KILLCOUNT:
            self.playing = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(self.bullets) < 2:
                        self.bullet = Bullet(self,1,self.player.nozzle.pos - (20,20),self.angleb)
                        self.bullets.add(self.bullet)
                        self.sprl.add(self.bullet)
                if event.key == pygame.K_UP:
                    self.player.jump()

    def draw(self):
        self.screen.fill(BLACK)
        self.sprl.draw(self.screen)
        pygame.display.flip()

    def new_game(self):
        self.kills = 0
        self.platforms = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.sprl = pygame.sprite.Group()
        self.player = Player(self,self.sprl)
        ground = Platform(0,HEIGHT - 40,WIDTH,40)
        self.sprl.add(ground)
        self.platforms.add(ground)
        self.sprl.add(self.player)
        for p in PLATFORMYS:
            plat = Platform(*p)
            self.sprl.add(plat)
            self.platforms.add(plat)
        self.run()

    def showstartscreen(self):
        pass
    def showgameoverscreen(self):
        pass
    def display_text(self,text,size,color,x,y):
        font = pygame.font.Font('arial',size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)

g = Game()
g.showstartscreen()
while g.running:
    g.new_game()
    if not g.playing:
        g.showgameoverscreen()
pygame.quit()
                
            
