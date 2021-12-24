import pygame, random, sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

x = 600
y = 500
z = [x, y]

win = pygame.display

bad_block_reload = 20  # delay of frames per bad block

rocks = ['pixel_ship_red_small.png', 'pixel_ship_blue_small.png']
player = pygame.image.load('player_walk_1.png')
sprites = pygame.sprite.Group()
bad_sprites = pygame.sprite.Group()  # add


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.x = x // 2
        self.rect.y = 400

    def update(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.rect.x > 5:
                    self.rect.x -= 5
            if event.key == pygame.K_RIGHT:
                if self.rect.x < 542:
                    self.rect.x += 5
            if event.key == pygame.K_UP:
                if self.rect.y > 5:
                    self.rect.y -= 5
            if event.key == pygame.K_DOWN:
                if self.rect.y > 5:
                    self.rect.y += 5


good_block = Block()  # change
sprites.add(good_block)  # change


class Explosion(pygame.sprite.Sprite):
    defaultlife = 12

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snail1.png')
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.life = self.defaultlife

    def update(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()


class Bad_Block(pygame.sprite.Sprite):
    def __init__(self):  # change
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(random.choice(rocks))
        ##        self.image.fill(red)#change
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 550)
        self.rect.y = 0

    def update(self):
        self.rect.centery += 5
        if self.rect.y == 750:
            sprites.add(Explosion(self.rect.center))
            self.kill()


move_x, move_y = 0, 0
change_x, change_y = 0, 0
win.set_caption('My Window')

surface = win.set_mode(z)
python = pygame.image.load('background-black.png')
window = True
clock = pygame.time.Clock()
click = 0
colors = [white, black, red, blue, green]

text_color = black
circle_x, circle_y = x // 2, y // 2
bad_block = bad_block_reload
paused = False
while window:
    for event in pygame.event.get():
        c_x, c_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            window = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
    if paused == True:
        continue
    elif bad_block:
        bad_block -= 1
    else:
        block = Bad_Block()
        bad_sprites.add(block)  # change
        bad_block = bad_block_reload
    sprite_hits = pygame.sprite.spritecollide(good_block, bad_sprites, True)
    for block in sprite_hits:
        sprites.add(Explosion(good_block.rect.center))
        sprites.add(Explosion(block.rect.center))
        good_block.kill()
        block.kill()

    font = pygame.font.Font('Pixeltype.ttf', 20)
    text = font.render('Start', 0, white)

    surface.fill(black)
    movement = pygame.mouse.get_pos()
    sprites.update()
    sprites.draw(surface)
    bad_sprites.update()
    bad_sprites.draw(surface)
    win.update()
    clock.tick(40)
pygame.quit()
