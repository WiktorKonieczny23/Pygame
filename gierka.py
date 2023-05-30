import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Gierka")

clock = pygame.time.Clock()

def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)
    rect = surface.get_rect(center=position)

    return [image, surface, rect]

def print_image(img_list):
    image, surface, rect = img_list
    screen_surface.blit(surface,rect)

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_LSHIFT]:
        speed*=2
    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    if keys[pygame.K_d]:
        delta_x += speed
    
    return [delta_x, delta_y] 

def limit_position(position):
    x, y = position
    


player_pos = [SCREEN_WIDTH //2, SCREEN_HEIGHT //2]
player = load_image("player.png", player_pos)

game_status = True
background_color = [10, 69, 22]

while game_status: 
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False

    pressed_key = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_key)
    player_pos[0] += delta_x
    player_pos[1] += delta_y
    player = set_position_image(player, player_pos)
    if player_pos[0]>800:
        player_pos[0]=800
    if player_pos[0]<0:
        player_pos[0]=0
    if player_pos[1]>600:
        player_pos[1]=600
    if player_pos[1]<0:
        player_pos[1]=0

    screen_surface.fill(background_color)
    print_image(player)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()