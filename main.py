import pygame, sys, os

pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("PYMusic")

class PLAYER:

    def __init__(self):
        self.track = 0
        self.currenttrack = " "
        self.pause = False
        self.volume = 1.0
        self.volumecounter = 100
        self.musicplay = True
        self.open = False
        self.prev = " "
        self.next = " "
        self.looptext = "Off"
        self.loop = False

    def listcreate(self):
        self.listdirect = os.listdir("MUSIC/")
        print(self.listdirect)

    def file(self):
        self.path = "MUSIC/" + self.listdirect[self.track]
        self.open = True
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
        self.currenttrack = "Now playing " + str(self.listdirect[self.track])
        self.nextsong()
        self.prevsong()

    def nextsong(self):
        if self.track == (len(self.listdirect) - 1):
            self.next = "Next: None"
        else:
            self.next = "Next: " + self.listdirect[(self.track + 1)]


    def prevsong(self):
        if self.track == 0:
            self.prev = "Previous: None"
        else:
            self.prev = "Previous: " + self.listdirect[(self.track - 1)]

    def check_posx(self, mouse_x):
        if 220 < mouse_x < 310 and 175 < mouse_y < 265:
            print(mouse_x)
            player.file()

        elif 310 < mouse_x < 385 and 185 < mouse_y < 260 and self.pause == False:
            print(mouse_x)
            self.pause = True
            pygame.mixer.music.pause()

        elif 310 < mouse_x < 385 and 185 < mouse_y < 260 and self.pause == True:
            print(mouse_x)
            self.pause = False
            pygame.mixer.music.unpause()

        elif 130 < mouse_x < 230 and 170 < mouse_y < 270 and self.track > 0:
            print(mouse_x)
            self.track -= 1
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            player.file()

        elif 385 < mouse_x < 485 and 170 < mouse_y < 270 and self.track < (len(self.listdirect) - 1):
            print(mouse_x)
            self.track += 1
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            player.file()

        elif 500 < mouse_x < 560 and 120 < mouse_y < 180 and self.volume < 1.0:
            print(mouse_x)
            self.volume += 0.01
            self.volumecounter += 1
            pygame.mixer.music.set_volume(self.volume)

        elif 500 < mouse_x < 560 and 210 < mouse_y < 270 and self.volume > 0.0:
            print(mouse_x)
            self.volume -= 0.01
            self.volumecounter -= 1
            pygame.mixer.music.set_volume(self.volume)

        elif 30 < mouse_x < 120 and 175 < mouse_y < 265 and self.loop == False:
            print(mouse_x)
            self.loop = True
            self.looptext = "On"

        elif 30 < mouse_x < 120 and 175 < mouse_y < 265 and self.loop == True:
            print(mouse_x)
            self.loop = False
            self.looptext = "Off"






playimg = pygame.image.load("img/play.png")
playimg = pygame.transform.scale(playimg, (90,90))

pauseimg = pygame.image.load("img/pause.png")
pauseimg = pygame.transform.scale(pauseimg, (75,75))

rewindimg = pygame.image.load("img/rewind.png")
rewindimg = pygame.transform.scale(rewindimg, (90,90))

forwardimg = pygame.image.load("img/next.png")
forwardimg = pygame.transform.scale(forwardimg, (100,100))

backimg = pygame.image.load("img/next.png")
backimg = pygame.transform.flip(backimg, True, False)
backimg = pygame.transform.scale(backimg, (100,100))

volupimg = pygame.image.load("img/play.png")
volupimg = pygame.transform.rotate(volupimg, 90)
volupimg = pygame.transform.scale(volupimg, (60,60))

voldownimg = pygame.image.load("img/play.png")
voldownimg = pygame.transform.rotate(voldownimg, 270)
voldownimg = pygame.transform.scale(voldownimg, (60,60))


text_font = pygame.font.SysFont('Comic Sans MS', 30)
small_font = pygame.font.SysFont('Comic Sans MS', 15)


player = PLAYER()

pygame.display.set_icon(playimg)

player.listcreate()
while True:

    text_surface = text_font.render(str(player.currenttrack), True, (0,0,0))
    volume_surface = text_font.render(str(player.volumecounter), True, (0,0,0))
    next_surface = small_font.render(str(player.next), True, (0,0,0))
    prev_surface = small_font.render(str(player.prev), True, (0,0,0))
    loop_surface = small_font.render(str(player.looptext), True, (0,0,0))

    

    screen.fill((255,255,255))
    screen.blit(playimg, (220,175))
    screen.blit(pauseimg, (310,185))
    screen.blit(rewindimg, (30,175))
    screen.blit(forwardimg, (385,170))
    screen.blit(volupimg, (500,120))
    screen.blit(voldownimg, (500,210))
    screen.blit(backimg, (130,170))
    screen.blit(text_surface, (60,30))
    screen.blit(volume_surface, (505,169))
    screen.blit(next_surface, (60,100))
    screen.blit(prev_surface, (60,80))
    screen.blit(loop_surface, (65,208))


    player.musicplay = pygame.mixer.music.get_busy()
    if player.musicplay == False and player.pause == False and player.track < (len(player.listdirect) - 1) and player.open == True and player.loop == False:
        player.track += 1
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        player.file()

    if player.musicplay == False and player.pause == False and player.open == True and player.loop == True:
        player.file()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            mouse_x = mouse[0]
            mouse_y = mouse[1]
            player.check_posx(mouse_x)

    pygame.display.update()