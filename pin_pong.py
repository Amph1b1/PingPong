from pygame import *

font.init()

which_hite = (623, 415)

class GameSprite(sprite.Sprite): #создали класс родитель

    def __init__(self, player_image, image_x, image_y, x, y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (image_x,image_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, image_x, image_y, x, y, player_speed, player_num):
        super().__init__(player_image, image_x, image_y, x, y, player_speed)
        self.num = player_num
        self.image = transform.scale(image.load(player_image), (image_x,image_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def update(self):
        key_pressed = key.get_pressed()
        if self.num == 1:
            if key_pressed[K_k]:
                if self.rect.y <= 210:
                    self.rect.y += self.speed
            if key_pressed[K_i]:
                if self.rect.y >= 0:
                    self.rect.y -= self.speed
        elif self.num == 0:
            if key_pressed[K_s]:
                if self.rect.y <= 210:
                    self.rect.y += self.speed
            if key_pressed[K_w]:
                if self.rect.y >= 0:
                    self.rect.y -= self.speed

class Ball(GameSprite):
    def __init__(self, player_image, image_x, image_y, x, y, player_speed, speed_x, speed_y):
        super().__init__(player_image, image_x, image_y, x, y, player_speed)
        self.sp_x = speed_x
        self.sp_y = speed_y
        self.image = transform.scale(image.load(player_image), (image_x,image_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    
    def update(self):
        
        if self.rect.x >= 623:
            return 1
            #self.sp_x *= -1
        elif self.rect.x <= 0:
            return 2
            #self.sp_x *= -1
        
        if self.rect.y >= 370:
            self.sp_y *= -1
        elif self.rect.y <= 0:
            self.sp_y *= -1

        if sprite.collide_rect(ball, player1):
            self.sp_x *= -1
        if sprite.collide_rect(ball, player2):
            self.sp_x *= -1

        self.rect.x += self.sp_x
        self.rect.y += self.sp_y

        

        '''if a == 0:
            print(a)
            self.rect.x += self.speed
            self.rect.y += self.speed
            if self.rect.y <= 370:
                a += 1
        elif a == 1:
            self.rect.x += self.speed
            self.rect.y -= self.speed'''
            


window = display.set_mode(which_hite)
display.set_caption('Пин Понг')

background = transform.scale(image.load('bonk.jpg'), which_hite)

player1 = Player('dai5.jpeg', 20, 200, 100, 110, 10, 0)
player2 = Player('dai5.jpeg', 20, 200, 500, 110, 10, 1)

ball = Ball('kalbasa_png.png', 50, 50, 270, 140, 3, 3, 3)

score = '0:0'

score_oneplayer = 0
score_twoplayer = 0
score_slash = ':'

score_sum = ''

font = font.Font(None, 80)

score_text = font.render(score, True, (0, 0, 0))

display.update()


game = True
clock = time.Clock()
fps = 60

failplayer = ''

score_if = True

while game:
    window.blit(background, (0, 0))
    
    if score_if == True:
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ballBool = ball.update()
        ball.reset()
        if ballBool:
            score_if = False
            if ballBool == 1:
                failplayer = 1
                score_oneplayer += 1
            elif ballBool == 2:
                failplayer = 2
                score_twoplayer += 1
    elif score_if == False:
        score_sum = str(score_oneplayer) + score_slash + str(score_twoplayer)
        score_text = font.render(score_sum, True, (0, 0, 0))
        ball.rect.x = 270
        ball.rect.y = 140
        score_if = True

    clock.tick(fps)

    window.blit(score_text, (270, 140))
    
    display.update()

    

    for i in event.get():
        if i.type == QUIT:
            game = False
