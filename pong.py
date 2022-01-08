import pygame, sys, local, random
from pygame.locals import *
from local import *

def initialize():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    random.seed()

    pygame.display.set_caption("Pong")
    icon = pygame.image.load("pixil-frame-0(1).png")
    pygame.display.set_icon(icon)

def main_menu():
    mainmenu = True
    titleText = myFont.render("P O N G", False, white)
    titleText = pygame.transform.scale(titleText, (titleText.get_width()*5, titleText.get_height()*5))
    
    playText = myFont.render("PLAY", False, white)
    playText = pygame.transform.scale(playText, (playText.get_width()*2, playText.get_height()*2))

    exitText = myFont.render("EXIT", False, white)
    exitText = pygame.transform.scale(exitText, (exitText.get_width()*2, exitText.get_height()*2))

    playButton = playText.get_rect()
    playButton.x, playButton.y = SCREEN_SIZE[0]/2 - playText.get_width()/2, 250

    exitButton = exitText.get_rect()
    exitButton.x, exitButton.y = SCREEN_SIZE[0]/2 - exitText.get_width()/2, 330

    pygame.mixer.music.load("170170__timgormly__8-bit-pickup.mp3")

    while mainmenu:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if playButton.collidepoint(mousePos):
                        pygame.mixer.music.play()
                        pygame.time.wait(1000)
                        mainmenu = False
                    if exitButton.collidepoint(mousePos):
                        pygame.quit()
                        pygame.font.quit()
                        sys.exit(0)
        screen.fill(black)
        screen.blit(titleText, (SCREEN_SIZE[0]/2 - titleText.get_width()/2, 40))
        screen.blit(playText, (SCREEN_SIZE[0]/2 - playText.get_width()/2, 250))
        screen.blit(exitText, (SCREEN_SIZE[0]/2 - exitText.get_width()/2, 330))
        pygame.display.update()
        Clock.tick(60)

def random1digitnumber():
    if random.randrange(1, 2) == 1:
        return 1
    if random.randrange(1, 2) == 2:
        return -1

def game_loop(player1score, player2score):
    vyAcc = 0
    vyMin = 0
    vyMax = 5
    vyAcc2 = 0
    vyMin2 = 0
    vyMax2 = 5
    ballvxMax = random1digitnumber()*5
    ballvyMax = random1digitnumber()*5
    player1pad = pygame.Rect(0, 300, 15, 70)
    player2pad = pygame.Rect(SCREEN_SIZE[0]-15, 300, 15, 70)
    ball = pygame.Rect(SCREEN_SIZE[0]/2 - 10, SCREEN_SIZE[1]/2 - 10, 20, 20)
    speed = 5
    lasttick = pygame.time.get_ticks()
    pygame.mixer.music.load("pong.wav")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_w:
                    vyAcc = -1
                if event.key == K_s:
                    vyAcc = 1
                if event.key == K_LSHIFT:
                    vyMax = 10
                if event.key == K_UP:
                    vyAcc2 = -1
                if event.key == K_DOWN:
                    vyAcc2 = 1
                if event.key == K_RSHIFT:
                    vyMax2 = 10
                if event.key == K_ESCAPE:
                    pause = True
                    pausedText = myFont.render("P A U S E D", False, white)
                    pausedText = pygame.transform.scale(pausedText, (pausedText.get_width()*5, pausedText.get_height()*5))

                    playText = myFont.render("RESUME", False, white)
                    playText = pygame.transform.scale(playText, (playText.get_width()*2, playText.get_height()*2))

                    exitText = myFont.render("EXIT", False, white)
                    exitText = pygame.transform.scale(exitText, (exitText.get_width()*2, exitText.get_height()*2))

                    playButton = playText.get_rect()
                    playButton.x, playButton.y = SCREEN_SIZE[0]/2 - playText.get_width()/2, 250

                    exitButton = exitText.get_rect()
                    exitButton.x, exitButton.y = SCREEN_SIZE[0]/2 - exitText.get_width()/2, 330

                    pygame.mixer.music.load("170170__timgormly__8-bit-pickup.mp3")

                    while pause:
                        mousePos = pygame.mouse.get_pos()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                pygame.font.quit()
                                pygame.mixer.quit()
                                sys.exit(0)
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    if playButton.collidepoint(mousePos):
                                        pygame.mixer.music.play()
                                        pygame.time.wait(1000)
                                        pygame.mixer.music.load("pong.wav")
                                        pause = False                                        
                                    if exitButton.collidepoint(mousePos):
                                        pygame.quit()
                                        pygame.font.quit()
                                        sys.exit(0)
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    pygame.mixer.music.load("pong.wav")
                                    pause = False

                        screen.fill(black)
                        screen.blit(pausedText, (SCREEN_SIZE[0]/2 - pausedText.get_width()/2, 40))
                        screen.blit(playText, (SCREEN_SIZE[0]/2 - playText.get_width()/2, 250))
                        screen.blit(exitText, (SCREEN_SIZE[0]/2 - exitText.get_width()/2, 330))
                        pygame.display.update()
                        Clock.tick(60)  

            if event.type == KEYUP:
                if event.key == K_w:
                    vyAcc = 0
                    break
                if event.key == K_s:
                    vyAcc = 0
                    break
                if event.key == K_LSHIFT:
                    vyMax = 5
                if event.key == K_UP:
                    vyAcc2 = 0
                if event.key == K_DOWN:
                    vyAcc2 = 0
                if event.key == K_RSHIFT:
                    vyMax2 = 5
        screen.fill(black)
        pygame.draw.rect(screen, white, player1pad)
        pygame.draw.rect(screen, white, player2pad)
        pygame.draw.rect(screen, white, ball)
        score1 = myFont.render(str(player1score), False, white)
        score2 = myFont.render(str(player2score), False, white)
        screen.blit(score1, (SCREEN_SIZE[0]/3 - score1.get_width()/2, 20))
        screen.blit(score2, (SCREEN_SIZE[0]/3 - score2.get_width()/2 + SCREEN_SIZE[0]/3, 20))
        player2pad.y = ball.y
        if vyAcc != 0:
            vyMin += vyAcc
            if vyMin >= vyMax:
                vyMin = vyMax
            if vyMin <= -vyMax:
                vyMin = -vyMax
            player1pad.y += vyMin
        elif vyAcc == 0:
            if vyMin > 0:
                vyMin -= 1
                if vyMin <= 0:
                    vyMin = 0
            if vyMin < 0:
                vyMin += 1
                if vyMin >= 0:
                    vyMin = 0
            player1pad.y += vyMin
        if player1pad.y > SCREEN_SIZE[1]-player1pad.h:
            player1pad.y = SCREEN_SIZE[1]-player1pad.h
        if player1pad.y < 0:
            player1pad.y = 0
        
        if vyAcc2 != 0:
            vyMin2 += vyAcc2
            if vyMin2 >= vyMax2:
                vyMin2 = vyMax2
            if vyMin2 <= -vyMax2:
                vyMin2 = -vyMax2
            player2pad.y += vyMin2
        elif vyAcc2 == 0:
            if vyMin2 > 0:
                vyMin2 -= 1
                if vyMin2 <= 0:
                    vyMin2 = 0
            if vyMin2 < 0:
                vyMin2 += 1
                if vyMin2 >= 0:
                    vyMin2 = 0
            player2pad.y += vyMin2
        if player2pad.y > SCREEN_SIZE[1]-player2pad.h:
            player2pad.y = SCREEN_SIZE[1]-player2pad.h
        if player2pad.y < 0:
            player2pad.y = 0

        ball.x += ballvxMax
        ball.y += ballvyMax
        if ball.y >= SCREEN_SIZE[1]-20:
            ballvyMax = -random.randrange(1, 5)
        if ball.y <= 0:
            ballvyMax = random.randrange(1, 5)
        if ball.x >= SCREEN_SIZE[0]-20:
            pygame.mixer.music.load("435413__v-ktor__explosion12.wav")
            pygame.mixer.music.play()
            pygame.time.wait(1000)
        if ball.x < 0:
            pygame.mixer.music.load("435413__v-ktor__explosion12.wav")
            pygame.mixer.music.play()
            player2score += 1
            pygame.time.wait(1000)
            game_loop(player1score, player2score)
        if player2pad.colliderect(ball):
            pygame.mixer.music.play()
            ballvxMax = -speed
            ballvyMax = random.randrange(-5, 5)
        if player1pad.colliderect(ball):
            pygame.mixer.music.play()
            ballvxMax = speed
            ballvyMax = random.randrange(-5, 5)
        curtick = pygame.time.get_ticks()
        if curtick > lasttick + 5000:
            speed += 1
            lasttick = curtick
        pygame.display.update()
        Clock.tick(60)

def main():
    initialize()

    main_menu()
    game_loop(player1score, player2score)

main()