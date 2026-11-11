from pygame import *

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
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]:
            self.rect.y += self.speed



window = display.set_mode((623, 415))
display.set_caption('Пин Понг')

background = transform.scale(image.load('bonk.jpg'), (623, 415))

player = Player('dai5.jpeg', 20, 200, 100, 200, 10)  

display.update()


game = True
clock = time.Clock()
fps = 60

while game:
    window.blit(background, (0, 0))
    
    player.update()
    player.reset()

    clock.tick(fps)
    
    display.update()

    

    for i in event.get():
        if i.type == QUIT:
            game = False